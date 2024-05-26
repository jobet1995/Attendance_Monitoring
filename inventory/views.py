from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import (
    User, Product, Supplier, ProductSupplier, Warehouse, Inventory,
    Order, OrderDetail, Customer, CustomerOrder, CustomerOrderDetail,
    Shipment, ShipmentDetail, StockAdjustment, InventoryTransaction
)
from .forms import (
    UserForm, ProductForm, SupplierForm, ProductSupplierForm, WarehouseForm, InventoryForm,
    OrderForm, OrderDetailForm, CustomerForm, CustomerOrderForm, CustomerOrderDetailForm,
    ShipmentForm, ShipmentDetailForm, StockAdjustmentForm, InventoryTransactionForm
)
from .serializers import (
    UserSerializer, ProductSerializer, SupplierSerializer, ProductSupplierSerializer,
    WarehouseSerializer, InventorySerializer, OrderSerializer, OrderDetailSerializer,
    CustomerSerializer, CustomerOrderSerializer, CustomerOrderDetailSerializer,
    ShipmentSerializer, ShipmentDetailSerializer, StockAdjustmentSerializer,
    InventoryTransactionSerializer
)
@login_required
def product_list(request):
    product = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': product})

@login_required
def supplier_list(request):
    supplier = Supplier.objects.all()
    return render(request, 'supplier/supplier_list.html', {'supplier': supplier})

@login_required
def product_supplier_list(request):
    product_supplier = ProductSupplier.objects.all()
    return render(request, 'product_supplier/product_list.html', {'product_supplier': product_supplier})

@login_required
def warehouse_list(request):
    warehouse = Warehouse.objects.all()
    return render(request, 'warehouse/warehouse_list.html', {'warehouse_list': warehouse})

@login_required
def inventory_list(request):
    inventory = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventory': inventory})

@login_required
def order_list(request):
    order = Order.objects.all()
    return render(request, 'order/order_list.html', {'order': order})

@login_required
def order_detail_list(request):
    order_detail = OrderDetail.objects.all()
    return render(request, 'order_detail/order_detail_list.html', {'order_detail': order_detail})

@login_required
def customer_list(request):
    customer = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customer': customer})

@login_required
def customer_order_list(request):
    customer_order = CustomerOrder.objects.all()
    return render(request, 'customer_order/customer_order_list.html', {'customer_order': customer_order})

@login_required
def order_detail_list(request):
    order_detail = CustomerOrderDetail.objects.all()
    return render(request, 'order_detail/order_detail_list.html', {'order_detail': order_detail})

@login_required
def shipment_list(request):
    shipment = Shipment.objects.all()
    return render(request, 'shipment/shipment_list.html', {'shipment': shipment})

@login_required
def shipment_detail_list(request):
    shipment_list = ShipmentDetail.objects.all()
    return render(request, 'shipment_detail/shipment_detail_list.html', {'shipment_detail': shipment_detail})

@login_required
def stock_adjustment(request):
    stock_adjustment = StockAdjustment.objects.all()
    return render(request, 'stock_adjustment/stock_adjustment_list.html', {'stock_adjustment': stock_adjustment})

@login_required
def inventory_transaction(request):
    inventory_transaction = InventoryTransaction.objects.all()
    return render(request, 'inventory_transaction/inventory_transaction_list.html', {'inventory_transaction': inventory_transaction})

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        error_response = validate_form(form)

        if error_response:
            return error_response
        else:
            product_name = form.cleaned_data.get('product_name')
        
        if Product.objects.filter(product_name=product_name).exists():
            existing_product = Product.objects.get(product_name=product_name)
            return JsonResponse({'success': False, 'error': 'Product already exists', 'product': existing_product.id}, status=400)
        else:
            form.save()
            return JsonResponse({'success': True}, status=201)
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})
    
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