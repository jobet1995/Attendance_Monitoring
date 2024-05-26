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


@login_required
def add_warehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = WarehouseForm()
    return render(request, 'warehouse/add_warehouse.html', {'form': form})


@login_required
def update_warehouse(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'warehouse/update_warehouse.html', {'form': form, 'warehouse': warehouse})


@login_required
def delete_warehouse(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    warehouse.delete()
    return JsonResponse({'success': True})


@login_required
def search_warehouse(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        warehouses = Warehouse.objects.filter(warehouse_name__icontains=query)
        return render(request, 'warehouse/search_warehouse.html', {'warehouses': warehouses, 'query': query})
    else:
        return render(request, 'warehouse/search_warehouse.html')


@login_required
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = InventoryForm()
    return render(request, 'inventory/add_inventory.html', {'form': form})


@login_required
def update_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'inventory/update_inventory.html', {'form': form, 'inventory': inventory})


@login_required
def delete_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    inventory.delete()
    return JsonResponse({'success': True})


@login_required
def search_inventory(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        inventories = Inventory.objects.filter(
            product__product_name__icontains=query)
        return render(request, 'inventory/search_inventory.html', {'inventories': inventories, 'query': query})
    else:
        return render(request, 'inventory/search_inventory.html')


@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})


@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = OrderForm(instance=order)
    return render(request, 'order/update_order.html', {'form': form, 'order': order})


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return JsonResponse({'success': True})


@login_required
def search_order(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        orders = Order.objects.filter(order_number__icontains=query)
        return render(request, 'order/search_order.html', {'orders': orders, 'query': query})
    else:
        return render(request, 'order/search_order.html')


@login_required
def add_order_detail(request):
    if request.method == 'POST':
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = OrderDetailForm()
    return render(request, 'order_detail/add_order_detail.html', {'form': form})


@login_required
def update_order_detail(request, order_detail_id):
    order_detail = get_object_or_404(OrderDetail, pk=order_detail_id)
    if request.method == 'POST':
        form = OrderDetailForm(request.POST, instance=order_detail)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = OrderDetailForm(instance=order_detail)
    return render(request, 'order_detail/update_order_detail.html', {'form': form, 'order_detail': order_detail})


@login_required
def delete_order_detail(request, order_detail_id):
    order_detail = get_object_or_404(OrderDetail, pk=order_detail_id)
    order_detail.delete()
    return JsonResponse({'success': True})


@login_required
def search_order_detail(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        order_details = OrderDetail.objects.filter(
            order__order_number__icontains=query)
        return render(request, 'order_detail/search_order_detail.html', {'order_details': order_details, 'query': query})
    else:
        return render(request, 'order_detail/search_order_detail.html')


@login_required
def add_product_supplier(request):
    if request.method == 'POST':
        form = ProductSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ProductSupplierForm()
    return render(request, 'product_supplier/add_product_supplier.html', {'form': form})


@login_required
def update_product_supplier(request, product_supplier_id):
    product_supplier = get_object_or_404(
        ProductSupplier, pk=product_supplier_id)
    if request.method == 'POST':
        form = ProductSupplierForm(request.POST, instance=product_supplier)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ProductSupplierForm(instance=product_supplier)
    return render(request, 'product_supplier/update_product_supplier.html', {'form': form, 'product_supplier': product_supplier})


@login_required
def delete_product_supplier(request, product_supplier_id):
    product_supplier = get_object_or_404(
        ProductSupplier, pk=product_supplier_id)
    product_supplier.delete()
    return JsonResponse({'success': True})


@login_required
def search_product_supplier(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        product_suppliers = ProductSupplier.objects.filter(
            product__product_name__icontains=query)
        return render(request, 'product_supplier/search_product_supplier.html', {'product_suppliers': product_suppliers, 'query': query})
    else:
        return render(request, 'product_supplier/search_product_supplier.html')


@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = CustomerForm()
    return render(request, 'customer/add_customer.html', {'form': form})


@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/update_customer.html', {'form': form, 'customer': customer})


@login_required
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return JsonResponse({'success': True})


@login_required
def search_customer(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        customers = Customer.objects.filter(name__icontains=query)
        return render(request, 'customer/search_customer.html', {'customers': customers, 'query': query})
    else:
        return render(request, 'customer/search_customer.html')


@login_required
def add_customer_order(request):
    if request.method == 'POST':
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = CustomerOrderForm()
    return render(request, 'customer_order/add_customer_order.html', {'form': form})


@login_required
def update_customer_order(request, customer_order_id):
    customer_order = get_object_or_404(CustomerOrder, pk=customer_order_id)
    if request.method == 'POST':
        form = CustomerOrderForm(request.POST, instance=customer_order)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = CustomerOrderForm(instance=customer_order)
    return render(request, 'customer_order/update_customer_order.html', {'form': form, 'customer_order': customer_order})


@login_required
def delete_customer_order(request, customer_order_id):
    customer_order = get_object_or_404(CustomerOrder, pk=customer_order_id)
    customer_order.delete()
    return JsonResponse({'success': True})


@login_required
def search_customer_order(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        customer_orders = CustomerOrder.objects.filter(
            order_number__icontains=query)
        return render(request, 'customer_order/search_customer_order.html', {'customer_orders': customer_orders, 'query': query})
    else:
        return render(request, 'customer_order/search_customer_order.html')


@login_required
def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ShipmentForm()
    return render(request, 'shipment/add_shipment.html', {'form': form})


@login_required
def update_shipment(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'shipment/update_shipment.html', {'form': form, 'shipment': shipment})


@login_required
def delete_shipment(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    shipment.delete()
    return JsonResponse({'success': True})


@login_required
def search_shipment(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        shipments = Shipment.objects.filter(shipment_number__icontains=query)
        return render(request, 'shipment/search_shipment.html', {'shipments': shipments, 'query': query})
    else:
        return render(request, 'shipment/search_shipment.html')


@login_required
def add_shipment_detail(request):
    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ShipmentDetailForm()
    return render(request, 'shipment_detail/add_shipment_detail.html', {'form': form})


@login_required
def update_shipment_detail(request, shipment_detail_id):
    shipment_detail = get_object_or_404(ShipmentDetail, pk=shipment_detail_id)
    if request.method == 'POST':
        form = ShipmentDetailForm(request.POST, instance=shipment_detail)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ShipmentDetailForm(instance=shipment_detail)
    return render(request, 'shipment_detail/update_shipment_detail.html', {'form': form, 'shipment_detail': shipment_detail})


@login_required
def delete_shipment_detail(request, shipment_detail_id):
    shipment_detail = get_object_or_404(ShipmentDetail, pk=shipment_detail_id)
    shipment_detail.delete()
    return JsonResponse({'success': True})


@login_required
def search_shipment_detail(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')
        shipment_details = ShipmentDetail.objects.filter(
            shipment__shipment_number__icontains=query)
        return render(request, 'shipment_detail/search_shipment_detail.html', {'shipment_details': shipment_details, 'query': query})
    else:
        return render(request, 'shipment_detail/search_shipment_detail.html')


@login_required
def add_stock_adjustment(request):
    if request.method == 'POST':
        form = StockAdjustmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = StockAdjustmentForm()
    return render(request, 'stock_adjustment/add_stock_adjustment.html', {'form': form})


@login_required
def add_inventory_transaction(request):
    if request.method == 'POST':
        form = InventoryTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = InventoryTransactionForm()
    return render(request, 'inventory_transaction/add_inventory_transaction.html', {'form': form})
