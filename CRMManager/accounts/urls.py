from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name="product"),
    path('create_products/', views.product_create_view, name="productcreate"),

    ###customer###
    path('customer/', views.indexView),
    path('post/ajax/customer', views.postCustomer, name="post_customer"),
    path('get/ajax/validate/name', views.checkCustomerName, name="validate_name"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    ###Order##
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.UpdateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('post/ajax/order/', views.postOrder, name="post_order"),

    ##Tasks##
    path('post/ajax/task/<int:id>', views.postTask, name="post_task"),

    ##services##
    path('post/ajax/service/<int:id>', views.postService, name="post_service"),
    path(r'delete_service/', views.deleteService, name="delete_service"),

    #file
    path(r'^upload/(?P<id>\d+)/$', views.upload_files, name='upload_picture'),

    #info
     path(r'^info/(?P<id>\d+)/$', views.order_info, name='order_info'),
]
