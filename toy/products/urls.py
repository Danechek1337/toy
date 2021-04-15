from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categoriesPage, name="categories"),
    path('category/<int:pk>/', views.category_products, name="category_products"),
    path('product_details/<slug:slug>', views.product_details, name="product_details"),
]