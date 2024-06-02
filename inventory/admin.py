"""
@Description: Admin for Product, Supplier, ProductSupplier, Warehouse, Inventory, Order, OrderDetail, Customer, CustomerOrder, CustomerOrderDetail, Shipment, ShipmentDetail, StockAdjustment, and InventoryTransaction.
@Author: Jobet P. Casquejo
@Last Date Modified: 2024-5-26
@Last Modified By: Jobet P. Casquejo
Modification Log
Version     Author           Date                Logs
1.0         Jobet Casquejo   2024-5-26           Initial Version
"""

from django.contrib import admin
from .models import (
    User,
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
    Task,
    Event,
    EmailAttachment,
    SalesTransaction,
    Accountant
)

from .forms import (
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
    AccountantForm
)

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(ProductSupplier)
admin.site.register(Warehouse)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Customer)
admin.site.register(CustomerOrder)
admin.site.register(CustomerOrderDetail)
admin.site.register(Shipment)
admin.site.register(ShipmentDetail)
admin.site.register(StockAdjustment)
admin.site.register(InventoryTransaction)
admin.site.register(EmailAttachment)
admin.site.register(Accountant)
admin.site.register(SalesTransaction)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "due_date", "completed", "assigned_to")
    search_fields = ("title", "description")
    list_filter = ("completed", "due_date", "assigned_to")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time", "location")
    search_fields = ("name", "description", "location")
    list_filter = ("start_time", "end_time")
    filter_horizontal = ("participants",)


class AccountantAdmin(admin.ModelAdmin):
    form = AccountantForm
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name']
