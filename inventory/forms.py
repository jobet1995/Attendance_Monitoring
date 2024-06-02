"""
@Description: Models for Product, Supplier, ProductSupplier, Warehouse, Inventory, Order, OrderDetail, Customer, CustomerOrder, CustomerOrderDetail, Shipment, ShipmentDetail, StockAdjustment, and InventoryTransaction.
@Author: Jobet P. Casquejo
@Last Date Modified: 2024-5-26
@Last Modified By: Jobet P. Casquejo
Modification Log
Version     Author           Date                Logs
1.0         Jobet Casquejo   2024-5-26           Initial Version
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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


class AccountantForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Accountant
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password', 'permissions']

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "permissions": forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
        }


class UserForm(UserCreationForm):
    """
    @Description: Form for creating or updating user accounts within the inventory system.
    @Attributes:
        username (CharField): The username for the user account.
        password1 (CharField): The password for the user account (first entry).
        password2 (CharField): The password for the user account (confirmation).
        email (EmailField): The email address associated with the user account.
        first_name (CharField): The first name of the user.
        last_name (CharField): The last name of the user.
        role (ChoiceField): The role assigned to the user account within the inventory system.
    """

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "role",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if "@" not in email:
            raise forms.ValidationError("Please enter a valid email address")
        return email

    def cleaned_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data["password1"])
            user.save()
        return user


class LoginForm(forms.ModelForm):
    """
    @description: Form class for user login.
    This form allows users to enter their credentials (username and password) for authentication.
    @Attributes:
        -username (CharField): The field for entering the username.
        -password (CharField): The field for entering the password.
    """

    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_username(self):
        """
        Sanitizes the username entered by the user.
        """
        username = self.cleaned_data["username"]

        if not username.isalnum():
            raise ValidationError(
                "Username must contain only letters and numbers.")

        if len(username) < 4 or len(username) > 20:
            raise ValidationError(
                "Username must be between 4 and 20 characters long.")

        if any(char in username for char in [";", "--"]):
            raise ValidationError("Invalid characters in username.")

        return username


class ProductForm(forms.ModelForm):
    """
    @description: Form for creating or updating product details within the inventory system.

    @attributes:
        product_name (CharField): The name of the product.
        description (TextField): A detailed description of the product.
        category (CharField): The category to which the product belongs.
        unit_price (DecimalField): The price per unit of the product.
        reorder_level (IntegerField): The inventory level at which new stock should be reordered.

    @widgets:
        product_name (TextInput): Rendered as a text input with Bootstrap form control styling.
        description (Textarea): Rendered as a textarea with Bootstrap form control styling.
        category (TextInput): Rendered as a text input with Bootstrap form control styling.
        unit_price (NumberInput): Rendered as a number input with Bootstrap form control styling.
        reorder_level (NumberInput): Rendered as a number input with Bootstrap form control styling.
    """

    class Meta:
        model = Product
        fields = [
            "product_name",
            "description",
            "category",
            "unit_price",
            "reorder_level",
        ]
        widgets = {
            "product_name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control"}),
            "reorder_level": forms.NumberInput(attrs={"class": "form-control"}),
        }


class SupplierForm(forms.ModelForm):
    """
    @description: Form for creating or updating supplier details.

    @attributes:
        supplier_name (CharField): The name of the supplier.
        contact_name (CharField): The name of the contact person at the supplier.
        address (TextField): The address of the supplier.
        city (CharField): The city where the supplier is located.
        postal_code (CharField): The postal code of the supplier's address.
        country (CharField): The country where the supplier is located.
        phone (CharField): The phone number for the supplier.

    @widgets:
        supplier_name (TextInput): Rendered as a text input with Bootstrap form control styling.
        contact_name (TextInput): Rendered as a text input with Bootstrap form control styling.
        address (Textarea): Rendered as a textarea with Bootstrap form control styling.
        city (TextInput): Rendered as a text input with Bootstrap form control styling.
        postal_code (TextInput): Rendered as a text input with Bootstrap form control styling.
        country (TextInput): Rendered as a text input with Bootstrap form control styling.
        phone (TextInput): Rendered as a text input with Bootstrap form control styling.
    """

    class Meta:
        model = Supplier
        fields = [
            "supplier_name",
            "contact_name",
            "address",
            "city",
            "postal_code",
            "country",
            "phone",
        ]
        widgets = {
            "supplier_name": forms.TextInput(attrs={"class": "form-control"}),
            "contact_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProductSupplierForm(forms.ModelForm):
    """
    @description: Form for associating products with suppliers.

    @attributes:
        product (ForeignKey): Reference to the product.
        supplier (ForeignKey): Reference to the supplier.

    @widgets:
        product (Select): Rendered as a select dropdown with Bootstrap form control styling.
        supplier (Select): Rendered as a select dropdown with Bootstrap form control styling.
    """

    class Meta:
        model = ProductSupplier
        fields = ["product", "supplier"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "supplier": forms.Select(attrs={"class": "form-control"}),
        }


class WarehouseForm(forms.ModelForm):
    """
    @description: Form for creating or updating warehouse details.

    @attributes:
        warehouse_name (CharField): The name of the warehouse.
        location (CharField): The location of the warehouse.

    @widgets:
        warehouse_name (TextInput): Rendered as a text input with Bootstrap form control styling.
        location (TextInput): Rendered as a text input with Bootstrap form control styling.
    """

    class Meta:
        model = Warehouse
        fields = ["warehouse_name", "location"]
        widgets = {
            "warehouse_name": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }


class InventoryForm(forms.ModelForm):
    """
    @description: Form for managing inventory records.

    @attributes:
        product (ForeignKey): Reference to the product.
        warehouse (ForeignKey): Reference to the warehouse.
        quantity (IntegerField): The quantity of the product in stock.

    @widgets:
        product (Select): Rendered as a select dropdown with Bootstrap form control styling.
        warehouse (Select): Rendered as a select dropdown with Bootstrap form control styling.
        quantity (NumberInput): Rendered as a number input with Bootstrap form control styling.
    """

    class Meta:
        model = Inventory
        fields = ["product", "warehouse", "quantity"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "warehouse": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }


class OrderForm(forms.ModelForm):
    """
    @description: Form for creating or updating orders.
    @attributes:
        order_date (DateField): The date when the order was placed.
        supplier (ForeignKey): Reference to the supplier.
        status (CharField): The current status of the order.
    @widgets:
        order_date (DateInput): Rendered as a date input with Bootstrap form control styling.
        supplier (Select): Rendered as a select dropdown with Bootstrap form control styling.
        status (Select): Rendered as a select dropdown with Bootstrap form control styling.
    """

    class Meta:
        model = Order
        fields = ["order_date", "supplier", "status"]
        widgets = {
            "order_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }


class OrderDetailForm(forms.ModelForm):
    """
    @description: Form for managing the details of an order.
    @attributes:
        order (ForeignKey): Reference to the order.
        product (ForeignKey): Reference to the product.
        quantity (IntegerField): The quantity of the product ordered.
        unit_price (DecimalField): The price per unit of the product.
    @widgets:
        order (Select): Rendered as a select dropdown with Bootstrap form control styling.
        product (Select): Rendered as a select dropdown with Bootstrap form control styling.
        quantity (NumberInput): Rendered as a number input with Bootstrap form control styling.
        unit_price (NumberInput): Rendered as a number input with Bootstrap form control styling.
    """

    class Meta:
        model = OrderDetail
        fields = ["order", "product", "quantity", "unit_price"]
        widgets = {
            "order": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class CustomerForm(forms.ModelForm):
    """
    @description: Form for creating or updating customer details.

    @attributes:
        customer_name (CharField): The name of the customer.
        contact_name (CharField): The name of the contact person for the customer.
        address (TextField): The address of the customer.
        city (CharField): The city where the customer is located.
        postal_code (CharField): The postal code of the customer's address.
        country (CharField): The country where the customer is located.
        phone (CharField): The phone number for the customer.
    @widgets:
        customer_name (TextInput): Rendered as a text input with Bootstrap form control styling.
        contact_name (TextInput): Rendered as a text input with Bootstrap form control styling.
        address (Textarea): Rendered as a textarea with Bootstrap form control styling.
        city (TextInput): Rendered as a text input with Bootstrap form control styling.
        postal_code (TextInput): Rendered as a text input with Bootstrap form control styling.
        country (TextInput): Rendered as a text input with Bootstrap form control styling.
        phone (TextInput): Rendered as a text input with Bootstrap form control styling.
    """

    class Meta:
        model = Customer
        fields = [
            "customer_name",
            "contact_name",
            "address",
            "city",
            "postal_code",
            "country",
            "phone",
        ]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "contact_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }


class CustomerOrderForm(forms.ModelForm):
    """
    @description: Form for creating or updating customer orders.
    @attributes:
        customer (ForeignKey): Reference to the customer placing the order.
        order_date (DateField): The date when the order was placed.
        status (CharField): The current status of the order.
    @widgets:
        customer (Select): Rendered as a select dropdown with Bootstrap form control styling.
        order_date (DateInput): Rendered as a date input with Bootstrap form control styling.
        status (Select): Rendered as a select dropdown with Bootstrap form control styling.
    """

    class Meta:
        model = CustomerOrder
        fields = ["customer", "order_date", "status"]
        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "order_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
        }


class CustomerOrderDetailForm(forms.ModelForm):
    """
    @description: Form for managing the details of a customer order.
    @attributes:
        customer_order (ForeignKey): Reference to the customer order.
        product (ForeignKey): Reference to the product.
        quantity (IntegerField): The quantity of the product ordered.
        unit_price (DecimalField): The price per unit of the product.
    @widgets:
        customer_order (Select): Rendered as a select dropdown with Bootstrap form control styling.
        product (Select): Rendered as a select dropdown with Bootstrap form control styling.
        quantity (NumberInput): Rendered as a number input with Bootstrap form control styling.
        unit_price (NumberInput): Rendered as a number input with Bootstrap form control styling.
    """

    class Meta:
        model = CustomerOrderDetail
        fields = ["customer_order", "product", "quantity", "unit_price"]
        widgets = {
            "customer_order": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ShipmentForm(forms.ModelForm):
    """
    @description: Form for creating or updating shipment details.
    @attributes:
        shipment_date (DateField): The date when the shipment is made.
        carrier (CharField): The carrier responsible for the shipment.
        tracking_number (CharField): The tracking number for the shipment.
        status (CharField): The current status of the shipment.
    @widgets:
        shipment_date (DateInput): Rendered as a date input with Bootstrap form control styling.
        carrier (TextInput): Rendered as a text input with Bootstrap form control styling.
        tracking_number (TextInput): Rendered as a text input with Bootstrap form control styling.
        status (Select): Rendered as a select dropdown with Bootstrap form control styling.
    """

    class Meta:
        model = Shipment
        fields = ["shipment_date", "carrier", "tracking_number", "status"]
        widgets = {
            "shipment_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "carrier": forms.TextInput(attrs={"class": "form-control"}),
            "tracking_number": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }


class ShipmentDetailForm(forms.ModelForm):
    """
    @description: Form for managing the details of a shipment.
    @attributes:
        shipment (ForeignKey): Reference to the shipment.
        order (ForeignKey): Reference to the order included in the shipment.
        customer_order (ForeignKey): Reference to the customer order included in the shipment.
        product (ForeignKey): Reference to the product being shipped.
        quantity (IntegerField): The quantity of the product being shipped.
    @widgets:
        shipment (Select): Rendered as a select dropdown with Bootstrap form control styling.
        order (Select): Rendered as a select dropdown with Bootstrap form control styling.
        customer_order (Select): Rendered as a select dropdown with Bootstrap form control styling.
        product (Select): Rendered as a select dropdown with Bootstrap form control styling.
        quantity (NumberInput): Rendered as a number input with Bootstrap form control styling.
    """

    class Meta:
        model = ShipmentDetail
        fields = ["shipment", "order", "customer_order", "product", "quantity"]
        widgets = {
            "shipment": forms.Select(attrs={"class": "form-control"}),
            "order": forms.Select(attrs={"class": "form-control"}),
            "customer_order": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }


class StockAdjustmentForm(forms.ModelForm):
    """
    @description: Form for managing stock adjustments.
    @attributes:
        product (ForeignKey): Reference to the product being adjusted.
        warehouse (ForeignKey): Reference to the warehouse where the adjustment is made.
        adjustment_date (DateField): The date when the adjustment is made.
        quantity (IntegerField): The quantity of the adjustment (positive or negative).
        reason (CharField): The reason for the stock adjustment.
    @widgets:
        product (Select): Rendered as a select dropdown with Bootstrap form control styling.
        warehouse (Select): Rendered as a select dropdown with Bootstrap form control styling.
        adjustment_date (DateInput): Rendered as a date input with Bootstrap form control styling.
        quantity (NumberInput): Rendered as a number input with Bootstrap form control styling.
        reason (TextInput): Rendered as a text input with Bootstrap form control styling.
    """

    class Meta:
        model = StockAdjustment
        fields = ["product", "warehouse",
                  "adjustment_date", "quantity", "reason"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "warehouse": forms.Select(attrs={"class": "form-control"}),
            "adjustment_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "reason": forms.TextInput(attrs={"class": "form-control"}),
        }


class InventoryTransactionForm(forms.ModelForm):
    """
    @description: Form for recording inventory transactions.
    @attributes:
        product (ForeignKey): Reference to the product involved in the transaction.
        warehouse (ForeignKey): Reference to the warehouse where the transaction takes place.
        quantity (IntegerField): The quantity involved in the transaction.
        transaction_type (CharField): The type of transaction (e.g., addition, removal).
        transaction_date (DateTimeField): The date and time of the transaction.
    @widgets:
        product (Select): Rendered as a select dropdown with Bootstrap form control styling.
        warehouse (Select): Rendered as a select dropdown with Bootstrap form control styling.
        quantity (NumberInput): Rendered as a number input with Bootstrap form control styling.
        transaction_type (Select): Rendered as a select dropdown with Bootstrap form control styling.
        transaction_date (DateTimeInput): Rendered as a datetime input with Bootstrap form control styling.
    """

    class Meta:
        model = InventoryTransaction
        fields = [
            "product",
            "warehouse",
            "quantity",
            "transaction_type",
            "transaction_date",
        ]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "warehouse": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "transaction_type": forms.Select(attrs={"class": "form-control"}),
            "transaction_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
        }


class TaskForm(forms.ModelForm):
    """
    @Description: Form for creating and updating Task instances.
    @Attributes:
        - title (CharField): The title of the task.
        - description (TextField): A detailed description of the task.
        - due_date (DateField): The date by which the task should be completed.
        - completed (BooleanField): A boolean indicating whether the task has been completed.
        - assigned_to (ForeignKey): A foreign key linking to the User model to indicate who the task is assigned to.
    """

    class Meta:
        model = Task
        fields = ["title", "description",
                  "due_date", "completed", "assigned_to"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "assigned_to": forms.Select(attrs={"class": "form-control"}),
        }


class EventForm(forms.ModelForm):
    """
    @Description: Form for creating and updating Event instances.
    @Attributes:
        - name (CharField): The name of the event.
        - description (TextField): A detailed description of the event.
        - start_time (DateTimeField): The start time of the event.
        - end_time (DateTimeField): The end time of the event.
        - location (CharField): The location where the event will take place.
        - participants (ManyToManyField): A many-to-many relationship with the User model indicating who will participate in the event.
    """

    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "start_time",
            "end_time",
            "location",
            "participants",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "start_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "end_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "participants": forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class EmailAttachmentForm(forms.Form):
    """
    @description: Form for uploading email attachments.
    @attributes:
        attachment (FileField): The attachment file to be uploaded.
    @widgets:
        attachment (FileInput): Rendered as a file input with Bootstrap form control styling.
    """

    model = EmailAttachment
    fields = ["customer_email", "subject", "body", "attachment"]
    widgets = {
        "customer_email": forms.EmailInput(attrs={"class": "form-control"}),
        "subject": forms.TextInput(attrs={"class": "form-control"}),
        "body": forms.Textarea(attrs={"class": "form-control"}),
        "attachment": forms.FileInput(attrs={"class": "form-control"}),
    }


class SalesTransactionForm(forms.Form):
    class Meta:
        model = SalesTransaction
        fields = ['product', 'customer', 'quantity', 'total_amount', 'status']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
