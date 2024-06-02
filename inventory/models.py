"""
@Description: Models for Product, Supplier, ProductSupplier, Warehouse, Inventory, Order, OrderDetail, Customer, CustomerOrder, CustomerOrderDetail, Shipment, ShipmentDetail, StockAdjustment, and InventoryTransaction.
@Author: Jobet P. Casquejo
@Last Date Modified: 2024-5-26
@Last Modified By: Jobet P. Casquejo
Modification Log
Version     Author           Date                Logs
1.0         Jobet Casquejo   2024-5-26           Initial Version
"""

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Accountant(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='accountant')

    class Meta:
        permissions = [
            ("view_inventory_report", "Can view inventory reports"),
            ("adjust_inventory_levels", "Can adjust inventory levels"),
            ("audit_inventory", "Can perform audit of inventory"),
            ("manage_suppliers", "Can manage suppliers"),
            ("manage_purchasing", "Can manage purchasing of new inventory"),
            ("add_supplier", "Can add a new supplier"),
            ("update_supplier", "Can update existing supplier information"),
            ("delete_supplier", "Can delete a supplier"),
            ("manage_pricing", "Can set and change prices for products"),
            ("set_discounts", "Can set discounts on products"),
            ("create_invoice", "Can create invoices for transactions"),
            ("manage_returns", "Can manage product returns"),
            ("issue_refunds", "Can issue refunds for returns"),
            ("record_payment", "Can record a payment to a supplier"),
            ("view_payments", "Can view the payments history"),
            ("set_tax_rates", "Can set tax rates for products"),
            ("calculate_taxes", "Can calculate taxes based on set rates")
        ]

    def __str__(self):
        return self.user.username


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

            return self.create_user(username, email, password, **extra_fields)


class InternalUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username


class EmailAttachment(models.Model):
    customer_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachment = models.FileField(upload_to='email_attachments/')

    def __str__(self):
        return self.customer_email


class User(AbstractUser, PermissionsMixin):
    """
    @Description: Custom user model for managing different roles within the inventory system.
    @Attributes:
        role (str): The role of the user within the inventory system. Choices include:
            - Administrator: Has full access and control over the inventory system.
            - Inventory Manager: Responsible for managing inventory-related tasks.
            - Warehouse Staff: Handles operations within the warehouse, such as stocking and shipping.
            - Purchasing Manager: Manages purchasing activities and vendor relationships.
            - Sales Manager: Oversees sales operations and customer relationships.
            - Customer Service Representative: Handles customer inquiries and support requests.
            - Accountant: Manages financial transactions and reporting.
            - Auditor: Conducts audits and ensures compliance with regulations.
            - System User: Internal user for system operations and maintenance.
            - Customer: Represents external customers who interact with the system.
            - Standard User: Basic user with limited access and permissions.
        groups (ManyToManyField): The groups to which the user belongs.
        user_permissions (ManyToManyField): Specific permissions granted to the user.
    """

    ROLE_CHOICES = [
        ("Administrator", "Administrator"),
        ("Inventory Manager", "Inventory Manager"),
        ("Warehouse Staff", "Warehouse Staff"),
        ("Purchasing Manager", "Purchasing Manager"),
        ("Sales Manager", "Sales Manager"),
        ("Customer Service Representative", "Customer Service Representative"),
        ("Technical Service Representative", "Technical Service Representative"),
        ("Accountant", "Accountant"),
        ("Auditor", "Auditor"),
        ("System User", "System User"),
        ("Customer", "Customer"),
        ("Standard User", "Standard User"),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        related_name="inventory_users_groups",  # Unique related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        related_name="inventory_users_permissions",  # Unique related_name
    )


class Product(models.Model):
    """
    @Description: The Product model represents a product with various properties.
    A product has a name, description, category, unit price, reorder level,
    and the timestamp it was created at as characteristics.
    @Fields:
        - product_name: This field is used to store the name of the product. Since it’s a CharField, it's used for shorter strings. The max_length=255 indicates the maximum length of the character field, meaning that the product name can't be longer than 255 characters. This field must be filled since NULL values are not allowed for it.
        - description: The description field is used for holding more detailed information about the product. Unlike product_name, this field can hold a substantial amount of text as it's a TextField. blank=True, null=True allows this field to be blank or NULL, meaning that it is not mandatory to provide a description.
        - category: This field is used to specify the category to which the product belongs. Like product_name, it’s a CharField and can't exceed 255 characters. But with blank=True, null=True, this field can be left blank during product creation/update if the category is not known or relevant.
        - unit_price: This field represents the base price of a single unit of the product. It's a DecimalField, which means it can store a very precise number and is excellent for storing an exact price. The max_digits=10 parameter indicates that no more than 10 digits may be used to represent the number, and decimal_places=2 specifies that 2 of those digits are reserved for representing decimal places.
        - reorder_level: The reorder_level field can be used in inventory management, for instance, to kick off a restocking process. If the amount of product falls below the reorder_level, it might be a good idea to reorder the product. default=0 means that if a reorder level is not specified when a product is created, it defaults to 0.
        - created_at:  This field is used for record-keeping purposes, so you know when each product was created. By default, when a product instance is created, it gets given a created_at value of the current date and time.
    """

    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name


class Supplier(models.Model):
    """
    @Description: Supplier model represents a provider of products.
    This model represents a product supplier. It contains the supplier's name, email and other details. Supplier instances can be related with a product instance, meaning a product instance can reference a supplier that provides the product.
    A Supplier instance has `supplier_name` as unique identifier referring to the name of the supplier. `email` field contains the email address of the supplier. `contact_number` holds phone number of the supplier. `address` is the physical address of the supplier company.
    @Fields:
        - supplier_name: Stores the name of the supplier company.
        - contact_name: Stores the name of a contact person in the supplier's company.
        - address: Contains the physical business address of the supplier.
        - city: Holds the city where the supplier's company is located.
        - postal_code: Stores the postal or ZIP code associated with the supplier's address.
        - country: Contains the country of the supplier's business location.
        - phone: Holds the phone number for contacting the supplier.
        - created_at: Automatically gets the date and time when a new supplier record is created.
    """

    supplier_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.supplier_name


class ProductSupplier(models.Model):
    """
    @Description: The ProductSupplier model represents the relationship between the Product and Supplier models.
    This model is essentially an association or "bridging" model between Product and Supplier, enabling the many-to-many relationship between them.
    @Fields:
        - product: A foreign key field that references an instance of the Product model.
        - supplier: A foreign key field that references an instance of the Supplier model.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("product", "supplier"),)


class Warehouse(models.Model):
    """
    @Description: The Warehouse model represents a storage facility where products are stored.
    It is essential for tracking the physical location of goods and managing logistics. Each warehouse stores multiple products and each product can be stored in multiple warehouses, creating a many-to-many relationship.
    Fields:
        - name: The name of the Warehouse. It can be the location or any identifier for the warehouse.
        - address: The physical location of the warehouse.
        - inventory: Many-to-many field with the Inventory model representing the products stored in the warehouse.
    """

    warehouse_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.warehouse_name


class Inventory(models.Model):
    """
    @Description: The Inventory model represents the available stock of products.
    This model keeps track of available quantities of different products. It is crucial for managing product availability and carrying out inventory checks.
    @Fields:
        - product: A foreign key field that references an instance of the Product model.
        - quantity: An integer field that indicates the number of pieces of a specific product in stock.
        - last_updated: A datetime field which stores the last moment the inventory record was updated.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (("product", "warehouse"),)


class Order(models.Model):
    """
    @Description: The Order model represents a customer's order.
    This model is utilized to manage customer orders for products, track order status, and manage order fulfillment.
    @Fields:
        - customer: A foreign key field linking to an instance of the Customer model.
        - product: A foreign key field linking to an instance of the Product model.
        - quantity: An integer field indicating the order quantity for a specific product.
        - order_date: A datetime field representing when the order was placed.
        - order_status: A choice field indicating the current status of the order.
    """

    ORDER_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Placed", "Placed"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]
    order_date = models.DateField()
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default="Pending"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} from {self.supplier.supplier_name}"

    def can_be_cancelled(self):
        return self.status in ["Pending", "Placed"]

    def cancel(self):
        if self.can_be_cancelled():
            self.status = "Cancelled"
            self.save(update_fields=["status"])
            return True
        return False


class OrderDetail(models.Model):
    """
    @Description: The OrderDetail model represents detailed information for each order.
    This model is used to store individual product line items in an order, including quantity, product, and price.
    @Fields:
        - order: A foreign key field linking to an instance of the Order model.
        - product: A foreign key field linking to an instance of the Product model.
        - quantity: An integer field indicating the quantity of a specific product in the order.
        - price_per_item: A decimal field storing the price for each instance of the product in the order.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class Customer(models.Model):
    """
    @Description: The Customer model represents customers who place orders.
    This model stores customer details like names, contact information and their associated orders.
    @Fields:
        - name: A character field storing the name of the customer.
        - contact_details: A text field saving the contact details of the customer.
        - orders: A many-to-many field linking to the Order model, indicating which orders have been placed by the customer.
    """

    customer_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.customer_name


class CustomerOrder(models.Model):
    """
    @Description: The CustomerOrder model is a bridge between customers and their orders.
    This model connects a customer to their respective orders. It helps in tracking which orders were placed by which customers, their statuses and any other information pertinent to a sales order.
    @Fields:
        - customer: A foreign key field linking to an instance of the Customer model.
        - order_date: A datetime field storing when the order was created.
        - status: A character field indicating the status of the order.
    """

    ORDER_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default="Pending"
    )
    created_at = models.DateTimeField(default=timezone.now)


class CustomerOrderDetail(models.Model):
    """
    @Description: The CustomerOrderDetail model provides detailed information about each order placed by customers.
    This model connects a customer order to the individual items it consists of. It helps in tracking which products were included in each order, their quantities and any extra details, such as special instructions regarding the order.
    @Fields:
        - order: A foreign key field linking to an instance of the CustomerOrder model.
        - product: A foreign key field linking to an instance of the Product model.
        - quantity: An integer field that stores the number of units of the product that were ordered.
        - special_instructions: A text field that can store any special instructions or notes given by the customer regarding a particular product in the order.
    """

    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class Shipment(models.Model):
    """
    @Description: The Shipment model tracks the delivery of each customer order.
    This model details the process of getting an order from the warehouse to the customer's doorstep. It documents critical steps such as the departure from the warehouse, arrival at the courier, and delivery to the customer.
    @Fields:
        - order: A foreign key field linking to an instance of the CustomerOrder model.
        - departure_time: A datetime field recording when the order left the warehouse.
        - courier_arrival_time: A datetime field logging when the shipment arrived at the courier.
        - delivery_time: A datetime field cataloging when the customer received the order.
    """

    SHIPMENT_STATUS_CHOICES = [
        ("In Transit", "In Transit"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]
    shipment_date = models.DateField()
    carrier = models.CharField(max_length=255, blank=True, null=True)
    tracking_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=SHIPMENT_STATUS_CHOICES, default="In Transit"
    )
    created_at = models.DateTimeField(default=timezone.now)


class ShipmentDetail(models.Model):
    """
    @Description: The ShipmentDetail model caters to the need for meticulous record-keeping for each shipment in the system.
    @Fields:
        - shipment: A foreign key field linking to an instance of the Shipment model, effectively allowing the system to correlate a series of packages, tracking numbers, and carriers to each shipment.
        - tracking_number: A char field used to store the unique identification number provided by the carrier. Customers can use these numbers to track their packages in real time, leading to greater customer satisfaction and less scope for confusion about a package's location at any given time.
        - carrier: A char field containing the name or other identifier of the carrier performing the delivery, enabling a clear line of responsibility and contact for each shipped package.
    """

    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    customer_order = models.ForeignKey(
        CustomerOrder, on_delete=models.SET_NULL, null=True, blank=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class StockAdjustment(models.Model):
    """
    @Description: The StockAdjustment model enables the tracking of modifications to product stock quantities.
    @Fields:
        - product: A foreign key field linking to an instance of the Product model.
        - adjustment_reason: A char field describing the motive behind the adjustment.
        - adjustment_date: A datetime field recording when the adjustment happened.
        - adjustment_value: An integer field indicating the amount adjusted.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    adjustment_date = models.DateField()
    quantity = models.IntegerField()
    reason = models.CharField(max_length=255, blank=True, null=True)


class InventoryTransaction(models.Model):
    """
    @Description: The InventoryTransaction model traces all transactions taking place in inventory, ensuring accountability and control over inventory items.
    @Fields:
        - product: A foreign key field linking to an instance of the Product model.
        - transaction_type: A char field capturing the type of transaction, be it inbound, outbound or transfer between warehouses.
        - transaction_date: A datetime field recording when the transaction took place.
        - transaction_quantity: An integer field indicating the number of items included in the transaction.
    """

    TRANSACTION_TYPE_CHOICES = [
        ("IN", "IN"),
        ("OUT", "OUT"),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(
        max_length=50, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateTimeField(default=timezone.now)


class Task(models.Model):
    """
    @Description: Represents a task that can be assigned to a user.
    @Attributes:
        - title (CharField): The title of the task.
        - description (TextField): A detailed description of the task.
        - due_date (DateField): The date by which the task should be completed.
        - completed (BooleanField): A boolean indicating whether the task has been completed.
        - assigned_to (ForeignKey): A foreign key linking to the User model to indicate who the task is assigned to.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    @Description: Represents an event that users can participate in.
    @Attributes:
        - name (CharField): The name of the event.
        - description (TextField): A detailed description of the event.
        - start_time (DateTimeField): The start time of the event.
        - end_time (DateTimeField): The end time of the event.
        - location (CharField): The location where the event will take place.
        - participants (ManyToManyField): A many-to-many relationship with the User model indicating who will participate in the event.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, related_name="events")

    def __str__(self):
        return self.name


class SalesTransaction(models.Model):
    """
    @Description: Represents a sales transaction that can be associated with a product, customer, and quantity.
    @Attributes:
        - transaction_id (AutoField): The unique identifier for the transaction.
        - product (ForeignKey): A foreign key linking to the Product model.
        - customer (ForeignKey): A foreign key linking to the Customer model.
        - quantity (IntegerField): The quantity of the product sold.
        - transaction_date (DateTimeField): The date and time of the transaction.
        - total_amount (DecimalField): The total amount of the transaction.
        - status (CharField): The status of the transaction, such as "Paid", "Pending", or "Cancelled".
    """
    transaction_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.transaction_id)


@receiver(post_save, sender=Order)
def create_task_for_new_order(sender, instance, created, **kwargs):
    if created:
        admin_user = User.objects.filter(role="Administrator").first()
        if admin_user:
            Task.objects.create(
                title=f"New Order #{instance.id} placed",
                description="A new order has been placed with.",
                due_date=timezone.now() + timezone.timedelta(days=1),
                assigned_to=admin_user,
            )


@receiver(post_save, sender=Order)
def create_order_details(sender, instance, created, **kwargs):
    """
    @Description: Signal handler to create order details when an order is confirmed.
    @Parameters:
        sender (Model): The model class that sent the signal.
        instance (Order): The instance of the Order model being saved.
        created (bool): Indicates whether the instance was created or updated.
        kwargs (dict): Additional keyword arguments.
    @Returns:
        None
    """
    if not created and instance.status == "Confirmed":
        for item in instance.items.all():
            OrderDetail.objects.create(
                order=instance,
                product=item.product,
                quantity=item.quantity,
                customer=instance.customer,
            )
