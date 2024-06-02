"""
@Description: Serializers for Product, Supplier, ProductSupplier, Warehouse, Inventory, Order, OrderDetail, Customer, CustomerOrder, CustomerOrderDetail, Shipment, ShipmentDetail, StockAdjustment, and InventoryTransaction.
@Author: Jobet P. Casquejo
@Last Date Modified: 2024-5-26
@Last Modified By: Jobet P. Casquejo
Modification Log
Version     Author           Date                Logs
1.0         Jobet Casquejo   2024-5-26           Initial Version
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
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

User = get_user_model()

class Accountant(serializers.ModelSerializer):
    class Meta:
        model = Accountant
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for User model. Converts User instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the user.
        - username: The username of the user.
        - email: The email address of the user.
        - first_name: The first name of the user.
        - last_name: The last name of the user.
        - role: The role of the user.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for UserSerializer. Defines the fields to be included in the JSON representation of User instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of User instances.
        @Methods: None
        """

        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role"]


class ProductSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for Product model. Converts Product instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the product.
        - product_name: The name of the product.
        - description: The description of the product.
        - category: The category of the product.
        - unit_price: The unit price of the product.
        - reorder_level: The reorder level of the product.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for ProductSerializer. Defines the fields to be included in the JSON representation of Product instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of Product instances.
        @Methods: None
        """

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
    """
    @Descrption: Serializer for Supplier model. Converts Supplier instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the supplier.
        - supplier_name: The name of the supplier.
        - contact_name: The contact name of the supplier.
        - address: The address of the supplier.
        - city: The city of the supplier.
        - postal_code: The postal code of the supplier.
        - country: The country of the supplier.
        - phone: The phone number of the supplier.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for SupplierSerializer. Defines the fields to be included in the JSON representation of Supplier instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of Supplier instances.
        @Methods: None
        """

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
    """
    @Descrption: Serializer for ProductSupplier model. Converts ProductSupplier instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the product supplier.
        - product: The product associated with the product supplier.
        - supplier: The supplier associated with the product supplier.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for ProductSupplierSerializer. Defines the fields to be included in the JSON representation of ProductSupplier instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of ProductSupplier instances.
        @Methods: None
        """

        model = ProductSupplier
        fields = ["id", "product", "supplier"]


class WarehouseSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for Warehouse model. Converts Warehouse instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the warehouse.
        - warehouse_name: The name of the warehouse.
        - location: The location of the warehouse.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for WarehouseSerializer. Defines the fields to be included in the JSON representation of Warehouse instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of Warehouse instances.
        @Methods: None
        """

        model = Warehouse
        fields = ["id", "warehouse_name", "location"]


class InventorySerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for Inventory model. Converts Inventory instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the inventory.
        - product: The product associated with the inventory.
        - warehouse: The warehouse associated with the inventory.
        - quantity: The quantity of the inventory.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for InventorySerializer. Defines the fields to be included in the JSON representation of Inventory instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of Inventory instances.
        @Methods: None
        """

        model = Inventory
        fields = ["id", "product", "warehouse", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for Order model. Converts Order instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the order.
        - order_date: The date of the order.
        - supplier: The supplier associated with the order.
        - status: The status of the order.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for OrderSerializer. Defines the fields to be included in the JSON representation of Order instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of Order instances.
        @Methods: None
        """

        model = Order
        fields = ["id", "order_date", "supplier", "status"]


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for OrderDetail model. Converts OrderDetail instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the order detail.
        - order: The order associated with the order detail.
        - product: The product associated with the order detail.
        - quantity: The quantity of the order detail.
        - unit_price: The unit price of the order detail.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for OrderDetailSerializer. Defines the fields to be included in the JSON representation of OrderDetail instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of OrderDetail instances.
        @Methods: None
        """

        model = OrderDetail
        fields = ["id", "order", "product", "quantity", "unit_price"]


class CustomerSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for Customer model. Converts Customer instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the customer.
        - customer_name: The name of the customer.
        - contact_name: The contact name of the customer.
        - address: The address of the customer.
        - city: The city of the customer.
        - postal_code: The postal code of the customer.
        - country: The country of the customer.
        - phone: The phone number of the customer.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for CustomerSerializer. Defines the fields to be included in the JSON representation of Customer instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of Customer instances.
        @Methods: None
        """

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
    """
    @Descrption: Serializer for CustomerOrder model. Converts CustomerOrder instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the customer order.
        - customer: The customer associated with the customer order.
        - order_date: The date of the customer order.
        - status: The status of the customer order.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for CustomerOrderSerializer. Defines the fields to be included in the JSON representation of CustomerOrder instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of CustomerOrder instances.
        @Methods: None
        """

        model = CustomerOrder
        fields = ["id", "customer", "order_date", "status"]


class CustomerOrderDetailSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for CustomerOrderDetail model. Converts CustomerOrderDetail instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the customer order detail.
        - customer_order: The customer order associated with the customer order detail.
        - product: The product associated with the customer order detail.
        - quantity: The quantity of the customer order detail.
        - unit_price: The unit price of the customer order detail.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for CustomerOrderDetailSerializer. Defines the fields to be included in the JSON representation of CustomerOrderDetail instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of CustomerOrderDetail instances.
        @Methods: None
        """

        model = CustomerOrderDetail
        fields = ["id", "customer_order", "product", "quantity", "unit_price"]


class ShipmentSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for Shipment model. Converts Shipment instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the shipment.
        - shipment_date: The date of the shipment.
        - carrier: The carrier of the shipment.
        - tracking_number: The tracking number of the shipment.
        - status: The status of the shipment.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for ShipmentSerializer. Defines the fields to be included in the JSON representation of Shipment instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of Shipment instances.
        @Methods: None
        """

        model = Shipment
        fields = ["id", "shipment_date",
                  "carrier", "tracking_number", "status"]


class ShipmentDetailSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for ShipmentDetail model. Converts ShipmentDetail instances into JSON representation.
    @Attributes:
        - id: The unique identifier of the shipment detail.
        - shipment: The shipment associated with the shipment detail.
        - order: The order associated with the shipment detail.
        - customer_order: The customer order associated with the shipment detail.
        - product: The product associated with the shipment detail.
        - quantity: The quantity of the shipment detail.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for ShipmentDetailSerializer. Defines the fields to be included in the JSON representation of ShipmentDetail instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of ShipmentDetail instances.
        @Methods: None
        """

        model = ShipmentDetail
        fields = ["id", "shipment", "order",
                  "customer_order", "product", "quantity"]


class StockAdjustmentSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for StockAdjustment model. Converts ShipmentDetail instances into JSON representation.
    @Attributes:
        - id: This is the unique identifier for each stock adjustment entry. It's typically an auto-incrementing integer assigned by the database to uniquely identify each record.
        - product: This field refers to the product being adjusted in the stock. It likely contains a reference or foreign key to the Product model/table, indicating which product this adjustment applies to.
        - warehouse: This field indicates the warehouse where the stock adjustment is being made. It likely contains a reference or foreign key to the Warehouse model/table, specifying the warehouse location where the adjustment occurred.
        - adjustment_date: This field records the date and time when the stock adjustment was made. It typically stores a timestamp indicating the exact moment when the adjustment took place.
        - quantity: This field represents the quantity of the product being adjusted. It could be a positive or negative integer, depending on whether stock is being added or removed. For example, if a positive value is entered, it means stock is being added, and if a negative value is entered, it means stock is being deducted.
        - reason: This field provides a brief explanation or reason for the stock adjustment. It may contain text describing why the adjustment was necessary, such as "damaged goods," "inventory surplus," "customer return," etc. This helps in tracking the rationale behind each adjustment.
    @Methods: None
    """

    class Meta:
        """
        @Descrption: Meta class for StockAdjustmentSerializer. Defines the fields to be included in the JSON representation of StockAdjustment instances.
        @Attributes:
            - model: The model class that the serializer is for.
            - fields: The fields to be included in the JSON representation of StockAdjustment.
        @Methods: None
        """

        model = StockAdjustment
        fields = ["id", "product", "warehouse",
                  "adjustment_date", "quantity", "reason"]


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


class TaskSerializer(serializers.ModelSerializer):
    """
    @Description: Serializer for the Task model.
    @Attributes:
        - id (IntegerField): The unique identifier for the task.
        - title (CharField): The title of the task.
        - description (CharField): A detailed description of the task.
        - due_date (DateField): The date by which the task should be completed.
        - completed (BooleanField): A boolean indicating whether the task has been completed.
        - assigned_to (PrimaryKeyRelatedField): A foreign key linking to the User model to indicate who the task is assigned to.
    """

    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ["id", "title", "description",
                  "due_date", "completed", "assigned_to"]


class EventSerializer(serializers.ModelSerializer):
    """
    @Description: Serializer for the Event model.
    @Attributes:
        - id (IntegerField): The unique identifier for the event.
        - name (CharField): The name of the event.
        - description (CharField): A detailed description of the event.
        - start_time (DateTimeField): The start time of the event.
        - end_time (DateTimeField): The end time of the event.
        - location (CharField): The location where the event will take place.
        - participants (PrimaryKeyRelatedField): A many-to-many relationship with the User model indicating who will participate in the event.
    """

    participants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "start_time",
            "end_time",
            "location",
            "participants",
        ]


class EmailAttachmentSerializer(serializers.Serializer):
    """
    @Description: Serializer for the EmailAttachment model.
    @Attributes:
        - id (IntegerField): The unique identifier for the email attachment.
        - name (CharField): The name of the email attachment.
        - file (FileField): The file of the email attachment.
    """

    class Meta:
        model = EmailAttachment
        fields = [
            "customer_email",
            "subject",
            "body",
            "attachments"
        ]

class SalesTransactionSerializer(serializers.ModelSerializer):
    """
    @Descrption: Serializer for SalesTransaction model. Converts SalesTransaction instances into JSON representation.
    @Attributes:
        - transaction_id: The unique identifier of the sales transaction.
        - product: The product associated with the sales transaction.
        - customer: The customer associated with the sales transaction.
        - quantity: The quantity of the sales transaction.
        - total_amount: The total amount of the sales transaction.
        - status: The status of the sales transaction.
    @Methods: None
    """
    class Meta:
        model = SalesTransaction
        fields = ['transaction_id', 'product', 'customer', 'quantity', 'total_amount', 'status']