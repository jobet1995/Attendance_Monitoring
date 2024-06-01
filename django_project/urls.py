"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from inventory import views
from inventory.views import user_login

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', user_login, name="login"),
    path("product/add_product", views.add_product, name="add_product"),
    path("product/<int:pk>/update/", views.update_product, name="update_product"),
    path("product/search_product", views.search_product, name="search_product"),
    path("supplier/add_supplier/", views.add_supplier, name="add_supplier"),
]
