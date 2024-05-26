from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import (
    JsonResponse,
    HttpResponseNotAllowed,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import (
    Product,
    Supplier,
    ProductSupplier,
    Warehouse,
    Inventory,
    Order,
    OrderDetail,
    Customer,
    CustomerOrder,
    CustomerOrderDetail,
    Shipment,
    ShipmentDetail,
    StockAdjustment,
    InventoryTransaction,
)
from .serializers import (
    UserSerializer,
    ProductSerializer,
    SupplierSerializer,
    ProductSupplierSerializer,
    WarehouseSerializer,
    InventorySerializer,
    OrderSerializer,
    OrderDetailSerializer,
    CustomerSerializer,
    CustomerOrderSerializer,
    CustomerOrderDetailSerializer,
    ShipmentSerializer,
    ShipmentDetailSerializer,
    StockAdjustmentSerializer,
    InventoryTransactionSerializer,
)
from .forms import (
    UserForm,
    ProductForm,
    SupplierForm,
    ProductSupplierForm,
    WarehouseForm,
    InventoryForm,
    OrderForm,
    OrderDetailForm,
    CustomerForm,
    CustomerOrderForm,
    CustomerOrderDetailForm,
    ShipmentForm,
    ShipmentDetailForm,
    StockAdjustmentForm,
    InventoryTransactionForm,
)


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products": products})


@login_required
def supplier_list(request):
    supplier = Supplier.objects.all()
    return render(request, "inventory/supplier_list.html", {"supplier": supplier})


@login_required
def product_supplier_list(request):
    product_supplier = ProductSupplier.objects.all()
    return render(
        request,
        "inventory/product_supplier.html",
        {"product_supplier": product_supplier},
    )


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=201)
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        return HttpResponseNotAllowed(["POST"])


@login_required
def search_product(request):
    query = request.GET.get("query", "")
    products = Product.objects.filter(product_name__icontains=query)
    return JsonResponse({"products": products})


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get("product_name")
            # Check if the product already exists
            if Product.objects.filter(product_name=product_name).exists():
                return JsonResponse(
                    {"success": False, "error": "Product already exists"}, status=400
                )
            form.save()
            # HTTP 201 Created
            return JsonResponse({"success": True}, status=201)
        else:
            # HTTP 400 Bad Request
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        form = ProductForm()
    return render(request, "inventory/add_product.html", {"form": form})


@login_required
def update_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product_name = form.cleaned_data.get("product_name")
                # Check if the product already exists excluding the current one being updated
                if (
                    Product.objects.filter(product_name=product_name)
                    .exclude(pk=product_id)
                    .exists()
                ):
                    return JsonResponse(
                        {"success": False, "error": "Product name already exists"},
                        status=400,
                    )
                form.save()
                # HTTP 200 OK by default
                return JsonResponse({"success": True})
            else:
                # HTTP 400 Bad Request
                return JsonResponse(
                    {"success": False, "errors": form.errors}, status=400
                )
        else:
            form = ProductForm(instance=product)
        return render(
            request, "inventory/update_product.html", {
                "form": form, "product": product}
        )
    except Product.DoesNotExist:
        # HTTP 404 Not Found
        return JsonResponse(
            {"success": False, "error": "Product not found"}, status=404
        )


@login_required
def delete_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return JsonResponse({"success": True})  # HTTP 200 OK by default
    except Product.DoesNotExist:
        # HTTP 404 Not Found
        return JsonResponse(
            {"success": False, "error": "Product not found"}, status=404
        )


@login_required
def search_product(request):
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        products = Product.objects.filter(product_name__icontains=query)
        return render(
            request,
            "inventory/search_product.html",
            {"products": products, "query": query},
        )
    else:
        return render(request, "inventory/search_product.html")


@login_required
def add_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier_name = form.cleaned_data.get("supplier_name")
            try:
                Supplier.objects.get(supplier_name=supplier_name)
                return JsonResponse(
                    {"success": False, "error": "Supplier already exists"}, status=400
                )
            except ObjectDoesNotExist:
                form.savee()
                return JsonResponse({"success": True}, status=201)
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        return HttpResponseBadRequest("Invalid Method")


@login_required
def search_supplier(request):
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        suppliers = Supplier.objects.filter(supplier_name__icontains=query)
        return render(
            request,
            "inventory/search_supplier.html",
            {"suppliers": suppliers, "query": query},
        )
    else:
        return render(request, "inventory/search_supplier.html")


@login_required
def update_supplier(request):
    if request.method == "POST":
        supplier_name = request.POST.get("supplier_name")
        try:
            supplier = Supplier.objects.get(supplier_name=supplier_name)
            form = SupplierForm(request.POST, instance=supplier)
            if form.is_valid():
                updated_supplier_name = form.cleaned_data("supplier_name")
                if (
                    updated_supplier_name != supplier_name
                    and Supplier.objects.filter(
                        supplier_name=updated_supplier_name
                    ).exists()
                ):
                    return JsonResponse(
                        {"success": False, "error": "Supplier name already exists"},
                        status=400,
                    )
                form.save()
                return JsonResponse({"success": True})
            else:
                return JsonResponse(
                    {"success": False, "errors": form.errors}, status=400
                )
        except Supplier.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Supplier not found"}, status=404
            )
    else:
        return render(request, "inventory/search_supplier.html")


@login_required
def add_product_supplier(request):
    if request.method == "POST":
        form = ProductSupplierForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data.get("product_id")
            supplier_id = form.cleaned_data.get("supplier_id")

            if ProductSupplier.objects.filter(
                product_id - product_id, supplier_id=supplier_id
            ).exists():
                return JsonResponse(
                    {
                        "success": False,
                        "error": "Product-Supplier relationship already exists",
                    },
                    status=400,
                )
            form.save()
            return JsonResponse({"success": True}, status=201)
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        form = ProductSupplierForm()
    return render(request, "inventory/add_product_supplier.html", {"form": form})


@login_required
def update_product_supplier(request, productsupplier_id):
    try:
        productsupplier = ProductSupplier.objects.get(pk=productsupplier_id)
        if request.method == "POST":
            form = ProductSupplierForm(request.POST, instance=productsupplier)
            if form.is_valid():
                product_id = form.cleaned_data.get("product_id")
                supplier_id = form.cleaned_data.get("supplier_id")

                # Check if the product-supplier relationship already exists
                if (
                    ProductSupplier.objects.filter(
                        product_id=product_id, supplier_id=supplier_id
                    )
                    .exclude(pk=productsupplier_id)
                    .exists()
                ):
                    return JsonResponse(
                        {
                            "success": False,
                            "error": "Product-Supplier relationship already exists",
                        },
                        status=400,
                    )

                form.save()
                # HTTP 200 OK by default
                return JsonResponse({"success": True})
            else:
                # HTTP 400 Bad Request
                return JsonResponse(
                    {"success": False, "errors": form.errors}, status=400
                )
        else:
            form = ProductSupplierForm(instance=productsupplier)
        return render(
            request,
            "inventory/update_product_supplier.html",
            {"form": form, "productsupplier": productsupplier},
        )
    except ProductSupplier.DoesNotExist:
        return JsonResponse(
            {"success": False, "error": "Product-Supplier relationship not found"},
            status=404,
        )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Invalid credentials"})
    else:
        return render(request, "inventory/login.html")


def user_logout(request):
    logout(request)
    return JsonResponse({"success": True})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductSupplierViewSet(viewsets.ModelViewSet):
    queryset = ProductSupplier.objects.all()
    serializer_class = ProductSupplierSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer


class CustomerOrderDetailViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrderDetail.objects.all()
    serializer_class = CustomerOrderDetailSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentDetailViewSet(viewsets.ModelViewSet):
    queryset = ShipmentDetail.objects.all()
    serializer_class = ShipmentDetailSerializer


class StockAdjustmentViewSet(viewsets.ModelViewSet):
    queryset = StockAdjustment.objects.all()
    serializer_class = StockAdjustmentSerializer


class InventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer
