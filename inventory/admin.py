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
