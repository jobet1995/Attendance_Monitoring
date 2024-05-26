"""
@Description: This tests.py file is for testing various functionalities of the Inventory application. It specifically tests CRUD operations for `Product` and `Supplier` instances.
@Author: Jobet P. Casquejo
@Last Date Modified: 2024-5-26
@Last Modified By: Jobet P. Casquejo
Modification Log
Version     Author           Date                Logs
1.0         Jobet Casquejo   2024-5-26           Initial Version
"""

from django.test import TestCase
from .models import Product, User
from django.urls import reverse
from datetime import datetime


class ProductViewsCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            role="Administrator",
        )
        self.client.login(username="testuser", password="password123")

    def test_add_product(self):
        response = self.client.post(
            reverse("add_product"),
            {
                "product_name": "New Product",
                "description": "This is a new product",
                "category": "New Category",
                "unit_price": 12.99,
                "reorder_level": 6,
            },
        )

        self.assertEqual(response.status_code, 302)

    def test_update_product(self):
        Product.objects.create(
            product_name="New Product",
            description="This is a new Product",
            category="New Category",
            unit_price=12.99,
            reorder_level=6,
        )

        response = self.client.put(
            reverse("update_product", kwargs={"pk": 1}),
            {
                "product_name": "Test Product",
                "description": "Updated description",
                "category": "Test Category",
                "unit_price": 12.99,
                "reorder_level": 5,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 302)

        updated_product = Product.objects.get(pk=1)
        self.assertEqual(updated_product.description, "This is a new Product")

    def test_add_supplier(self):
        response = self.client.post(
            reverse("add_supplier"),
            {
                "supplier_name": "Test",
                "contact_name": "Test Contact",
                "address": "Test Address",
                "city": "Test City",
                "post_code": "2201",
                "country": "PH",
                "phone": "123456789",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
        )

        self.assertEqual(response.status_code, 302)
