from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import (
    ProductForm, SupplierForm, WarehouseForm, InventoryForm, ProductSupplierForm,
    OrderForm, OrderDetailForm, CustomerForm, CustomerOrderForm,
    CustomerOrderDetailForm, ShipmentForm, ShipmentDetailForm,
    StockAdjustmentForm, InventoryTransactionForm
)
from .models import (
    Product, Supplier, Warehouse, Inventory, Order, OrderDetail, ProductSupplier,
    Customer, CustomerOrder, CustomerOrderDetail, Shipment,
    ShipmentDetail, StockAdjustment, InventoryTransaction
)


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/supplier_list.html', {'suppliers': suppliers})


@login_required
def product_supplier_list(request):
    # Assuming ProductSupplier is a model in your app
    product_suppliers = ProductSupplier.objects.all()
    return render(request, 'product_supplier/product_supplier_list.html', {'product_suppliers': product_suppliers})


@login_required
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse/warehouse_list.html', {'warehouses': warehouses})


@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventories': inventories})


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


@login_required
def order_detail_list(request):
    order_details = OrderDetail.objects.all()
    return render(request, 'order_detail/order_detail_list.html', {'order_details': order_details})


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})


@login_required
def customer_order_list(request):
    customer_orders = CustomerOrder.objects.all()
    return render(request, 'customer_order/customer_order_list.html', {'customer_orders': customer_orders})


@login_required
def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipment/shipment_list.html', {'shipments': shipments})


@login_required
def shipment_detail_list(request):
    shipment_details = ShipmentDetail.objects.all()
    return render(request, 'shipment_detail/shipment_detail_list.html', {'shipment_details': shipment_details})


@login_required
def stock_adjustment_list(request):
    stock_adjustments = StockAdjustment.objects.all()
    return render(request, 'stock_adjustment/stock_adjustment_list.html', {'stock_adjustments': stock_adjustments})


@login_required
def inventory_transaction_list(request):
    inventory_transactions = InventoryTransaction.objects.all()
    return render(request, 'inventory_transaction/inventory_transaction_list.html', {'inventory_transactions': inventory_transactions})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})


@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/update_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return JsonResponse({'success': True})


@login_required
def search_product(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        products = Product.objects.filter(product_name__icontains=query)
        return render(request, 'product/search_product.html', {'products': products, 'query': query})
    else:
        return render(request, 'product/search_product.html')


@login_required
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = SupplierForm()
    return render(request, 'supplier/add_supplier.html', {'form': form})


@login_required
def update_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier/update_supplier.html', {'form': form, 'supplier': supplier})


@login_required
def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    supplier.delete()
    return JsonResponse({'success': True})


@login_required
def search_supplier(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        suppliers = Supplier.objects.filter(supplier_name__icontains=query)
        return render(request, 'supplier/search_supplier.html', {'suppliers': suppliers, 'query': query})
    else:
        return render(request, 'supplier/search_supplier.html')
