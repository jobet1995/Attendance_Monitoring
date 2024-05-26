from rest_framework import serializers
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "description",
            "category",
            "unit_price",
            "reorder_level",
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "id",
            "supplier_name",
            "contact_name",
            "address",
            "city",
            "postal_code",
            "country",
            "phone",
        ]


class ProductSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSupplier
        fields = ["id", "product", "supplier"]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["id", "warehouse_name", "location"]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["id", "product", "warehouse", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "order_date", "supplier", "status"]


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ["id", "order", "product", "quantity", "unit_price"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "customer_name",
            "contact_name",
            "address",
            "city",
            "postal_code",
            "country",
            "phone",
        ]


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ["id", "customer", "order_date", "status"]


class CustomerOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrderDetail
        fields = ["id", "customer_order", "product", "quantity", "unit_price"]


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ["id", "shipment_date", "carrier", "tracking_number", "status"]


class ShipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentDetail
        fields = ["id", "shipment", "order", "customer_order", "product", "quantity"]


class StockAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockAdjustment
        fields = ["id", "product", "warehouse", "adjustment_date", "quantity", "reason"]


class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = [
            "id",
            "product",
            "warehouse",
            "quantity",
            "transaction_type",
            "transaction_date",
        ]
