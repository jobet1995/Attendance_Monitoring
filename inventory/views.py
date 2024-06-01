"""
@Description: This module contains view functions for managing various entities in the system.
@Author: Jobet P. Casquejo
@Last Date Modified: 2024-5-26
@Last Modified By: Jobet P. Casquejo
Modification Log
Version     Author           Date                Logs
1.0         Jobet Casquejo   2024-5-26           Initial Version
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .forms import (
    ProductForm,
    SupplierForm,
    WarehouseForm,
    InventoryForm,
    ProductSupplierForm,
    OrderForm,
    OrderDetailForm,
    CustomerForm,
    CustomerOrderForm,
    CustomerOrderDetailForm,
    ShipmentForm,
    ShipmentDetailForm,
    StockAdjustmentForm,
    InventoryTransactionForm,
    TaskForm,
    EventForm,
    LoginForm,
    UserForm,
    EmailAttachmentForm
)
from .models import (
    Product,
    Supplier,
    Warehouse,
    Inventory,
    Order,
    OrderDetail,
    ProductSupplier,
    Customer,
    CustomerOrder,
    CustomerOrderDetail,
    Shipment,
    ShipmentDetail,
    StockAdjustment,
    InventoryTransaction,
    Task,
    Event,
    EmailAttachment
)


def register(request):
    """
    @Description: View function for user registration
    @Attributes:
        form (LoginForm): A form for Login users
    @Return:
        On POST: saves the user
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            return redirect("login")
    else:
        form = UserForm()
    return render(request, "registration.html", {"form": form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return HttpResponse('Username and password are required')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'login.html')


@login_required
def product_list(request):
    """
    @Description: This function retrieves a list of products from the database and renders them in the product list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered product list page containing the products.
    """
    products = Product.objects.all()
    return render(request, "product/product_list.html", {"products": products})


@login_required
def supplier_list(request):
    """
    @Description: This function retrieves a list of suppliers from the database and renders them in the supplier list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered supplier list page containing the suppliers.
    """
    suppliers = Supplier.objects.all()
    return render(request, "supplier/supplier_list.html", {"suppliers": suppliers})


@login_required
def product_supplier_list(request):
    """
    @Description: This function retrieves a list of product suppliers from the database and renders them in the product supplier list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered product supplier list page containing the product suppliers.
    """
    product_suppliers = ProductSupplier.objects.all()
    return render(
        request,
        "product_supplier/product_supplier_list.html",
        {"product_suppliers": product_suppliers},
    )


@login_required
def warehouse_list(request):
    """
    @Description: This function retrieves a list of warehouses from the database and renders them in the warehouse list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered warehouse list page containing the warehouses.
    """
    warehouses = Warehouse.objects.all()
    return render(request, "warehouse/warehouse_list.html", {"warehouses": warehouses})


@login_required
def inventory_list(request):
    """
    @Description: This function retrieves a list of inventories from the database and renders them in the inventory list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered inventory list page containing the inventories.
    """
    inventories = Inventory.objects.all()
    return render(
        request, "inventory/inventory_list.html", {"inventories": inventories}
    )


@login_required
def order_list(request):
    """
    @Description: This function retrieves a list of orders from the database and renders them in the order list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered order list page containing the orders.
    """
    orders = Order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})


@login_required
def order_detail_list(request):
    """
    @Description: This function retrieves a list of order details from the database and renders them in the order detail list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered order detail list page containing the order details.
    """
    order_details = OrderDetail.objects.all()
    return render(
        request, "order_detail/order_detail_list.html", {
            "order_details": order_details}
    )


@login_required
def customer_list(request):
    """
    @Description: This function retrieves a list of customers from the database and renders them in the customer list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered customer list page containing the customers.
    """
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})


@login_required
def customer_order_list(request):
    """
    @Description: This function retrieves a list of customer orders from the database and renders them in the customer order list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered customer order list page containing the customer orders.
    """
    customer_orders = CustomerOrder.objects.all()
    return render(
        request,
        "customer_order/customer_order_list.html",
        {"customer_orders": customer_orders},
    )


@login_required
def shipment_list(request):
    """
    @Description: This function retrieves a list of shipments from the database and renders them in the shipment list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered shipment list page containing the shipments.
    """
    shipments = Shipment.objects.all()
    return render(request, "shipment/shipment_list.html", {"shipments": shipments})


@login_required
def shipment_detail_list(request):
    """
    @Description: This function retrieves a list of shipment details from the database and renders them in the shipment detail list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered shipment detail list page containing the shipment details.
    """
    shipment_details = ShipmentDetail.objects.all()
    return render(
        request,
        "shipment_detail/shipment_detail_list.html",
        {"shipment_details": shipment_details},
    )


@login_required
def stock_adjustment_list(request):
    """
    @Description: This function retrieves a list of stock adjustments from the database and renders them in the stock adjustment list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered stock adjustment list page containing the stock adjustments.
    """
    stock_adjustments = StockAdjustment.objects.all()
    return render(
        request,
        "stock_adjustment/stock_adjustment_list.html",
        {"stock_adjustments": stock_adjustments},
    )


@login_required
def inventory_transaction_list(request):
    """
    @Description: This function retrieves a list of inventory transactions from the database and renders them in the inventory transaction list template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered inventory transaction list page containing the inventory transactions.
    """
    inventory_transactions = InventoryTransaction.objects.all()
    return render(
        request,
        "inventory_transaction/inventory_transaction_list.html",
        {"inventory_transactions": inventory_transactions},
    )


def error_404_view(request, exception):
    """
    @Description: This function handles the 404 error and renders the 404.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: exception (Exception): The exception object.
    @Return: HttpResponse: The rendered 404.html template.
    """
    return render(request, "404.html", status=404)


@login_required
def add_product(request):
    """
    @Description: This function handles the product creation form submission and renders the add_product.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_product.html template with the form.
    """
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ProductForm()
    return render(request, "product/add_product.html", {"form": form})


@login_required
def update_product(request, product_id):
    """
    @Description: This function handles the product update form submission and renders the update_product.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: product_id (int): The ID of the product to be updated.
    @Return: HttpResponse: The rendered update_product.html template with the form.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ProductForm(instance=product)
    return render(
        request, "product/update_product.html", {
            "form": form, "product": product}
    )


@login_required
def delete_product(request, product_id):
    """
    @Description: This function handles the product deletion and renders the product_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: product_id (int): The ID of the product to be deleted.
    @Return: HttpResponse: The rendered product_list.html template.
    """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return JsonResponse({"success": True})


@login_required
def search_product(request):
    """
    @Description: This function handles the product search and renders the search_product.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_product.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        products = Product.objects.filter(product_name__icontains=query)
        return render(
            request,
            "product/search_product.html",
            {"products": products, "query": query},
        )
    else:
        return render(request, "product/search_product.html")


@login_required
def add_supplier(request):
    """
    @Description: This function handles the supplier creation form submission and renders the add_supplier.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_supplier.html template with the form.
    """
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = SupplierForm()
    return render(request, "supplier/add_supplier.html", {"form": form})


@login_required
def update_supplier(request, supplier_id):
    """
    @Description: This function handles the supplier update form submission and renders the update_supplier.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: supplier_id (int): The ID of the supplier to be updated.
    @Return: HttpResponse: The rendered update_supplier.html template with the form.
    """
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = SupplierForm(instance=supplier)
    return render(
        request, "supplier/update_supplier.html", {
            "form": form, "supplier": supplier}
    )


@login_required
def delete_supplier(request, supplier_id):
    """
    @Description: This function handles the supplier deletion and renders the supplier_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: supplier_id (int): The ID of the supplier to be deleted.
    @Return: HttpResponse: The rendered supplier_list.html template.
    """
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    supplier.delete()
    return JsonResponse({"success": True})


@login_required
def search_supplier(request):
    """
    @Description: This function handles the supplier search and renders the search_supplier.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_supplier.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        suppliers = Supplier.objects.filter(supplier_name__icontains=query)
        return render(
            request,
            "supplier/search_supplier.html",
            {"suppliers": suppliers, "query": query},
        )
    else:
        return render(request, "supplier/search_supplier.html")


@login_required
def add_warehouse(request):
    """
    @Description: This function handles the warehouse creation form submission and renders the add_warehouse.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_warehouse.html template with the form.
    """
    if request.method == "POST":
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = WarehouseForm()
    return render(request, "warehouse/add_warehouse.html", {"form": form})


@login_required
def update_warehouse(request, warehouse_id):
    """
    @Description: This function handles the warehouse update form submission and renders the update_warehouse.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: warehouse_id (int): The ID of the warehouse to be updated.
    @Return: HttpResponse: The rendered update_warehouse.html template with the form.
    """
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    if request.method == "POST":
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = WarehouseForm(instance=warehouse)
    return render(
        request,
        "warehouse/update_warehouse.html",
        {"form": form, "warehouse": warehouse},
    )


@login_required
def delete_warehouse(request, warehouse_id):
    """
    @Description: This function handles the warehouse deletion and renders the warehouse_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: warehouse_id (int): The ID of the warehouse to be deleted.
    @Return: HttpResponse: The rendered warehouse_list.html template.
    """
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    warehouse.delete()
    return JsonResponse({"success": True})


@login_required
def search_warehouse(request):
    """
    @Description: This function handles the warehouse search and renders the search_warehouse.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_warehouse.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        warehouses = Warehouse.objects.filter(warehouse_name__icontains=query)
        return render(
            request,
            "warehouse/search_warehouse.html",
            {"warehouses": warehouses, "query": query},
        )
    else:
        return render(request, "warehouse/search_warehouse.html")


@login_required
def add_inventory(request):
    """
    @Description: This function handles the inventory creation form submission and renders the add_inventory.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_inventory.html template with the form.
    """
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = InventoryForm()
    return render(request, "inventory/add_inventory.html", {"form": form})


@login_required
def update_inventory(request, inventory_id):
    """
    @Description: This function handles the inventory update form submission and renders the update_inventory.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: inventory_id (int): The ID of the inventory to be updated.
    @Return: HttpResponse: The rendered update_inventory.html template with the form.
    """
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = InventoryForm(instance=inventory)
    return render(
        request,
        "inventory/update_inventory.html",
        {"form": form, "inventory": inventory},
    )


@login_required
def delete_inventory(request, inventory_id):
    """
    @Description: This function handles the inventory deletion and renders the inventory_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: inventory_id (int): The ID of the inventory to be deleted.
    @Return: HttpResponse: The rendered inventory_list.html template.
    """
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    inventory.delete()
    return JsonResponse({"success": True})


@login_required
def search_inventory(request):
    """
    @Description: This function handles the inventory search and renders the search_inventory.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_inventory.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        inventories = Inventory.objects.filter(
            product__product_name__icontains=query)
        return render(
            request,
            "inventory/search_inventory.html",
            {"inventories": inventories, "query": query},
        )
    else:
        return render(request, "inventory/search_inventory.html")


@login_required
def add_order(request):
    """
    @Description: This function handles the order creation form submission and renders the add_order.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_order.html template with the form.
    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = OrderForm()
    return render(request, "order/add_order.html", {"form": form})


@login_required
def update_order(request, order_id):
    """
    @Description: This function handles the order update form submission and renders the update_order.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: order_id (int): The ID of the order to be updated.
    @Return: HttpResponse: The rendered update_order.html template with the form.
    """
    order = get_object_or_404(Order, pk=order_id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = OrderForm(instance=order)
    return render(request, "order/update_order.html", {"form": form, "order": order})


@login_required
def delete_order(request, order_id):
    """
    @Description: This function handles the order deletion and renders the order_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: order_id (int): The ID of the order to be deleted.
    @Return: HttpResponse: The rendered order_list.html template.
    """
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return JsonResponse({"success": True})


@login_required
def search_order(request):
    """
    @Description: This function handles the order search and renders the search_order.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_order.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        orders = Order.objects.filter(order_number__icontains=query)
        return render(
            request, "order/search_order.html", {
                "orders": orders, "query": query}
        )
    else:
        return render(request, "order/search_order.html")


@login_required
def add_order_detail(request):
    """
    @Description: This function handles the order detail creation form submission and renders the add_order_detail.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_order_detail.html template with the form.
    """
    if request.method == "POST":
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = OrderDetailForm()
    return render(request, "order_detail/add_order_detail.html", {"form": form})


@login_required
def update_order_detail(request, order_detail_id):
    """
    @Description: This function handles the order detail update form submission and renders the update_order_detail.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: order_detail_id (int): The ID of the order detail to be updated.
    @Return: HttpResponse: The rendered update_order_detail.html template with the form.
    """
    order_detail = get_object_or_404(OrderDetail, pk=order_detail_id)
    if request.method == "POST":
        form = OrderDetailForm(request.POST, instance=order_detail)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = OrderDetailForm(instance=order_detail)
    return render(
        request,
        "order_detail/update_order_detail.html",
        {"form": form, "order_detail": order_detail},
    )


@login_required
def delete_order_detail(request, order_detail_id):
    """
    @Description: This function handles the order detail deletion and renders the order_detail_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: order_detail_id (int): The ID of the order detail to be deleted.
    @Return: HttpResponse: The rendered order_detail_list.html template.
    """
    order_detail = get_object_or_404(OrderDetail, pk=order_detail_id)
    order_detail.delete()
    return JsonResponse({"success": True})


@login_required
def search_order_detail(request):
    """
    @Description: This function handles the order detail search and renders the search_order_detail.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_order_detail.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        order_details = OrderDetail.objects.filter(
            order__order_number__icontains=query)
        return render(
            request,
            "order_detail/search_order_detail.html",
            {"order_details": order_details, "query": query},
        )
    else:
        return render(request, "order_detail/search_order_detail.html")


@login_required
def add_product_supplier(request):
    """
    @Description: This function handles the product supplier creation form submission and renders the add_product_supplier.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_product_supplier.html template with the form.
    """
    if request.method == "POST":
        form = ProductSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ProductSupplierForm()
    return render(request, "product_supplier/add_product_supplier.html", {"form": form})


@login_required
def update_product_supplier(request, product_supplier_id):
    """
    @Description: This function handles the product supplier update form submission and renders the update_product_supplier.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: product_supplier_id (int): The ID of the product supplier to be updated.
    @Return: HttpResponse: The rendered update_product_supplier.html template with the form.
    """
    product_supplier = get_object_or_404(
        ProductSupplier, pk=product_supplier_id)
    if request.method == "POST":
        form = ProductSupplierForm(request.POST, instance=product_supplier)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ProductSupplierForm(instance=product_supplier)
    return render(
        request,
        "product_supplier/update_product_supplier.html",
        {"form": form, "product_supplier": product_supplier},
    )


@login_required
def delete_product_supplier(request, product_supplier_id):
    """
    @Description: This function handles the product supplier deletion and renders the product_supplier_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: product_supplier_id (int): The ID of the product supplier to be deleted.
    @Return: HttpResponse: The rendered product_supplier_list.html template.
    """
    product_supplier = get_object_or_404(
        ProductSupplier, pk=product_supplier_id)
    product_supplier.delete()
    return JsonResponse({"success": True})


@login_required
def search_product_supplier(request):
    """
    @Description: This function handles the product supplier search and renders the search_product_supplier.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_product_supplier.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        product_suppliers = ProductSupplier.objects.filter(
            product__product_name__icontains=query
        )
        return render(
            request,
            "product_supplier/search_product_supplier.html",
            {"product_suppliers": product_suppliers, "query": query},
        )
    else:
        return render(request, "product_supplier/search_product_supplier.html")


@login_required
def add_customer(request):
    """
    @Description: This function handles the customer creation form submission and renders the add_customer.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_customer.html template with the form.
    """
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = CustomerForm()
    return render(request, "customer/add_customer.html", {"form": form})


@login_required
def update_customer(request, customer_id):
    """
    @Description: This function handles the customer update form submission and renders the update_customer.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: customer_id (int): The ID of the customer to be updated.
    @Return: HttpResponse: The rendered update_customer.html template with the form.
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = CustomerForm(instance=customer)
    return render(
        request, "customer/update_customer.html", {
            "form": form, "customer": customer}
    )


@login_required
def delete_customer(request, customer_id):
    """
    @Description: This function handles the customer deletion and renders the customer_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: customer_id (int): The ID of the customer to be deleted.
    @Return: HttpResponse: The rendered customer_list.html template.
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return JsonResponse({"success": True})


@login_required
def search_customer(request):
    """
    @Description: This function handles the customer search and renders the search_customer.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_customer.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        customers = Customer.objects.filter(name__icontains=query)
        return render(
            request,
            "customer/search_customer.html",
            {"customers": customers, "query": query},
        )
    else:
        return render(request, "customer/search_customer.html")


@login_required
def add_customer_order(request):
    """
    @Description: This function handles the customer order creation form submission and renders the add_customer_order.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_customer_order.html template with the form.
    """
    if request.method == "POST":
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = CustomerOrderForm()
    return render(request, "customer_order/add_customer_order.html", {"form": form})


@login_required
def update_customer_order(request, customer_order_id):
    """
    @Description: This function handles the customer order update form submission and renders the update_customer_order.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: customer_order_id (int): The ID of the customer order to be updated.
    @Return: HttpResponse: The rendered update_customer_order.html template with the form.
    """
    customer_order = get_object_or_404(CustomerOrder, pk=customer_order_id)
    if request.method == "POST":
        form = CustomerOrderForm(request.POST, instance=customer_order)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = CustomerOrderForm(instance=customer_order)
    return render(
        request,
        "customer_order/update_customer_order.html",
        {"form": form, "customer_order": customer_order},
    )


@login_required
def delete_customer_order(request, customer_order_id):
    """
    @Description: This function handles the customer order deletion and renders the customer_order_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: customer_order_id (int): The ID of the customer order to be deleted.
    @Return: HttpResponse: The rendered customer_order_list.html template.
    """
    customer_order = get_object_or_404(CustomerOrder, pk=customer_order_id)
    customer_order.delete()
    return JsonResponse({"success": True})


@login_required
def search_customer_order(request):
    """
    @Description: This function handles the customer order search and renders the search_customer_order.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_customer_order.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        customer_orders = CustomerOrder.objects.filter(
            order_number__icontains=query)
        return render(
            request,
            "customer_order/search_customer_order.html",
            {"customer_orders": customer_orders, "query": query},
        )
    else:
        return render(request, "customer_order/search_customer_order.html")


@login_required
def add_shipment(request):
    """
    @Description: This function handles the shipment creation form submission and renders the add_shipment.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_shipment.html template with the form.
    """
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ShipmentForm()
    return render(request, "shipment/add_shipment.html", {"form": form})


@login_required
def update_shipment(request, shipment_id):
    """
    @Description: This function handles the shipment update form submission and renders the update_shipment.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: shipment_id (int): The ID of the shipment to be updated.
    @Return: HttpResponse: The rendered update_shipment.html template with the form.
    """
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    if request.method == "POST":
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ShipmentForm(instance=shipment)
    return render(
        request, "shipment/update_shipment.html", {
            "form": form, "shipment": shipment}
    )


@login_required
def delete_shipment(request, shipment_id):
    """
    @Description: This function handles the shipment deletion and renders the shipment_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: shipment_id (int): The ID of the shipment to be deleted.
    @Return: HttpResponse: The rendered shipment_list.html template.
    """
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    shipment.delete()
    return JsonResponse({"success": True})


@login_required
def search_shipment(request):
    """
    @Description: This function handles the shipment search and renders the search_shipment.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_shipment.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        shipments = Shipment.objects.filter(shipment_number__icontains=query)
        return render(
            request,
            "shipment/search_shipment.html",
            {"shipments": shipments, "query": query},
        )
    else:
        return render(request, "shipment/search_shipment.html")


@login_required
def add_shipment_detail(request):
    """
    @Description: This function handles the shipment detail creation form submission and renders the add_shipment_detail.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_shipment_detail.html template with the form.
    """
    if request.method == "POST":
        form = ShipmentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ShipmentDetailForm()
    return render(request, "shipment_detail/add_shipment_detail.html", {"form": form})


@login_required
def update_shipment_detail(request, shipment_detail_id):
    """
    @Description: This function handles the shipment detail update form submission and renders the update_shipment_detail.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: shipment_detail_id (int): The ID of the shipment detail to be updated.
    @Return: HttpResponse: The rendered update_shipment_detail.html template with the form.
    """
    shipment_detail = get_object_or_404(ShipmentDetail, pk=shipment_detail_id)
    if request.method == "POST":
        form = ShipmentDetailForm(request.POST, instance=shipment_detail)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = ShipmentDetailForm(instance=shipment_detail)
    return render(
        request,
        "shipment_detail/update_shipment_detail.html",
        {"form": form, "shipment_detail": shipment_detail},
    )


@login_required
def delete_shipment_detail(request, shipment_detail_id):
    """
    @Description: This function handles the shipment detail deletion and renders the shipment_detail_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: shipment_detail_id (int): The ID of the shipment detail to be deleted.
    @Return: HttpResponse: The rendered shipment_detail_list.html template.
    """
    shipment_detail = get_object_or_404(ShipmentDetail, pk=shipment_detail_id)
    shipment_detail.delete()
    return JsonResponse({"success": True})


@login_required
def search_shipment_detail(request):
    """
    @Description: This function handles the shipment detail search and renders the search_shipment_detail.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_shipment_detail.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        shipment_details = ShipmentDetail.objects.filter(
            shipment__shipment_number__icontains=query
        )
        return render(
            request,
            "shipment_detail/search_shipment_detail.html",
            {"shipment_details": shipment_details, "query": query},
        )
    else:
        return render(request, "shipment_detail/search_shipment_detail.html")


@login_required
def add_stock_adjustment(request):
    """
    @Description: This function handles the stock adjustment creation form submission and renders the add_stock_adjustment.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_stock_adjustment.html template with the form.
    """
    if request.method == "POST":
        form = StockAdjustmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = StockAdjustmentForm()
    return render(request, "stock_adjustment/add_stock_adjustment.html", {"form": form})


@login_required
def add_inventory_transaction(request):
    """
    @Description: This function handles the inventory transaction creation form submission and renders the add_inventory_transaction.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_inventory_transaction.html template with the form.
    """
    if request.method == "POST":
        form = InventoryTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = InventoryTransactionForm()
    return render(
        request, "inventory_transaction/add_inventory_transaction.html", {
            "form": form}
    )


@login_required
def add_customer_order_detail(request):
    """
    @Description: This function handles the customer order detail creation form submission and renders the add_customer_order_detail.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered add_customer_order_detail.html template with the form.
    """
    if request.method == "POST":
        form = CustomerOrderDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = CustomerOrderDetailForm()
    return render(
        request, "customer_order_detail/add_customer_order_detail.html", {
            "form": form}
    )


@login_required
def update_customer_order_detail(request, customer_order_detail_id):
    """
    @Description: This function handles the customer order detail update form submission and renders the update_customer_order_detail.html template with the form.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: customer_order_detail_id (int): The ID of the customer order detail to be updated.
    @Return: HttpResponse: The rendered update_customer_order_detail.html template with the form.
    """
    customer_order_detail = get_object_or_404(
        CustomerOrderDetail, pk=customer_order_detail_id
    )
    if request.method == "POST":
        form = CustomerOrderDetailForm(
            request.POST, instance=customer_order_detail)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        form = CustomerOrderDetailForm(instance=customer_order_detail)
    return render(
        request,
        "customer_order_detail/update_customer_order_detail.html",
        {"form": form, "customer_order_detail": customer_order_detail},
    )


@login_required
def delete_customer_order_detail(request, customer_order_detail_id):
    """
    @Description: This function handles the customer order detail deletion and renders the customer_order_detail_list.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Param: customer_order_detail_id (int): The ID of the customer order detail to be deleted.
    @Return: HttpResponse: The rendered customer_order_detail_list.html template.
    """
    customer_order_detail = get_object_or_404(
        CustomerOrderDetail, pk=customer_order_detail_id
    )
    customer_order_detail.delete()
    return JsonResponse({"success": True})


@login_required
def search_customer_order_detail(request):
    """
    @Description: This function handles the customer order detail search and renders the search_customer_order_detail.html template.
    @Param: request (HttpRequest): The HTTP request object.
    @Return: HttpResponse: The rendered search_customer_order_detail.html template.
    """
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        customer_order_details = CustomerOrderDetail.objects.filter(
            order__order_number__icontains=query
        )
        return render(
            request,
            "customer_order_detail/search_customer_order_detail.html",
            {"customer_order_details": customer_order_details, "query": query},
        )
    else:
        return render(
            request, "customer_order_detail/search_customer_order_detail.html"
        )


@login_required
def task_list(request):
    """
    @Description: View function to display a list of tasks.
    @Parameters:
        - request: The HTTP request object.
    @Returns:
    A rendered HTML page displaying a list of tasks.
    """
    task = Task.objects.all()
    return render(request, "task/task_list.html", {"tasks": task})


@login_required
def task_detail(request, pk):
    """
    @Description: View function to display details of a specific task.
    @Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the task to be displayed.
    @Returns:
    A rendered HTML page displaying the details of the specified task.
    """
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task/task_detail.html", {"task": task})


@login_required
def task_create(request):
    """
    @Description: View function to create a new task.
    @Parameters:
        - request: The HTTP request object.
    @Returns:
    A rendered HTML page with a form to create a new task.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "task/task_form.html", {"form": form})


@login_required
def task_update(request, pk):
    """
    @Description: View function to update a task
    @Parameters:
        -request: The Http request object.
    @Return:
    A rendered HTML page with a form to updating task.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task/task_form.html", {"form": form})


@login_required
def event_list(request):
    """
    @Description: A view function to display all the events
    @Return:
    A rendered HTML page to display the event
    """
    event = Event.objects.all()
    return render(request, "event/event_list.html", {"event": event})


@login_required
def event_details(request, pk):
    """
    @Description: A view function to display the event details
    @Return:
    A rendered HTML page to display the event details
    """
    event = get_object_or_404(Event, pk=pk)
    return render(request, "event/event_detail.html", {"event": event})


@login_required
def event_create(request, pk):
    """
    @Description: A view function to create the new event
    @Parameters:
        -request: The Http request object
    @Return:
    A rendered HTML page to display the form
    """
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm(instance=event)
    return render(request, "event/event_form.html", {"form": form})


@login_required
def event_update(request, pk):
    """
    @Description: A view function to update the existing event
    @Parameters:
        -request: The Http request object
    @Return:
    A rendered HTML page to display the form
    """
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm(instance=event)
    return render(request, "event/event_form.html", {"form": form})


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def admin_compose_email(request):
    if request.method == 'POST':
        form = EmailAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            email_instance = form.save(commit=False)
            email_instance.sender = request.user
            email_instance.save()

            email = EmailMessage(
                subject=email_instance.subject,
                body=email_instance.message,
                from_email=request.user.email,
                to=[email_instance.recipient],
            )

            if email_instance.attachment:
                email.attach(email_instance.attachment.name, email_instance.attachment.read(
                ), email_instance.attachment.content_type)

            email.send()
            # Redirect to a success page or wherever you want
            return redirect('success')

    else:
        form = EmailAttachmentForm()

    return render(request, 'admin_compose_email.html', {'form': form})
