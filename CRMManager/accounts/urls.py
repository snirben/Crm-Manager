from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name="product"),
    path('create_products/', views.product_create_view, name="productcreate"),
    path('addtocart/', views.add_to_order, name="addtoorder"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.UpdateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order")
]
