from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
import datetime

from .models import *
from . utils import cookieCart, cartData, guestOrder
from .forms import OrderForm, CreateUserForm
# Create your views here.


# @login_required(login_url='login')
def store(request):

    data = cartData(request)
    cartItems = data['cartItems']

    categories = Category.objects.all()
    products = Product.objects.all()[:6]
    
    context = {'products':products, 'cartItems':cartItems, 'categories': categories}
    return render(request, 'store/store.html', context)


def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    quantity = data['quantity'] # HELLO

    print('Action:', action)
    print('product:', productId)
    print('Quantity:', quantity) # HELLO

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)  # HELLO

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + quantity) # HELLO
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
            order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            )

    return JsonResponse('Payment complete!', safe=False)



def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user_acc = form.save()
            Customer.objects.create(user=user_acc)
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт был успешно создан' + user)

            return redirect('login')

    context = {'form':form}
    return render(request, 'store/register.html', context)


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Вы ввели неправильное имя пользователя или пароль, попробуйте снова')
            
    context = {}
    return render(request, 'store/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('store')


def personalPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}
    
    return render(request, 'store/personal.html', context)


def actionPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/action.html', context)


def proizvodstvoPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    categories = Category.objects.all()
    context = {'categories': categories, 'cartItems': cartItems}   
    
    return render(request, 'store/nashe_proizvodstvo.html', context)


def receipsPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/receips.html', context)


def contactsPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/contacts.html', context)


def search_page(request):

    data = cartData(request)
    cartItems = data['cartItems']

    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)

        context = {'searched':searched, 'products':products, 'cartItems': cartItems}

        return render(request, 'store/search_page.html', context)
    else:
        context = {}

        return render(request, 'store/search_page.html', context)


def helpPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/help.html', context)


def paymentPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/payment.html', context)


def faqPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/faq.html', context)


def deliveryPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/delivery.html', context)
    
    
def servicesPage(request):

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems': cartItems}

    return render(request, 'store/services.html', context) 
    



    
