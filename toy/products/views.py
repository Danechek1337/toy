from django.core import paginator
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import EmptyPage, Paginator

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
import datetime

from .models import *
from store.models import Product
from store.models import Category
from store.utils import cartData

# Create your views here.

def categoriesPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    categories = Category.objects.all()
    context = {'categories': categories, 'cartItems': cartItems}   
    
    return render(request, 'products/categories.html', context)


def category_products(request, pk):
  sort_by = request.GET.get('sort', None)
  sorting_list = ['price', '-price', 'name', '-name']
  if sort_by and sort_by in sorting_list:
    products = Product.objects.filter(category__id=pk).order_by(sort_by)
  else:
    products = Product.objects.filter(category__id=pk)
  
  data = cartData(request)
  cartItems = data['cartItems']

  paginator = Paginator(products, 6)
  page_number = request.GET.get('page', 1)

  try:
      page = paginator.page(page_number)
  except EmptyPage:
      page = page_number.page(1)


  context = {'cartItems': cartItems, 'page': page, 'categoryid': pk, 'products': products}

  return render(request, 'products/category_products.html', context)


def product_details(request, slug):
    
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    product = get_object_or_404(Product, slug=slug)

    context = {'cartItems': cartItems, 'product': product, 'items':items}

    return render(request, 'products/product_details.html', context)
