from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('search_page', views.search_page, name="search-page"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('personal/', views.personalPage, name="personal"),

    path('action/', views.actionPage, name="action"),
    path('nashe_proizvodstvo/', views.proizvodstvoPage, name="nashe_proizvodstvo"),
    path('receips/', views.receipsPage, name="receips"),
    path('contacts/', views.contactsPage, name="contacts"),
    

    path('help/', views.helpPage, name="help"), 
    path('payment/', views.paymentPage, name="payment"),
    path('faq/', views.faqPage, name="faq"), 
    path('delivery/', views.deliveryPage, name="delivery"),
    path('services/', views.servicesPage, name="services"), 
    
]