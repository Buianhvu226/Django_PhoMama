from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('index', views.home, name='index'),
    path('food/<int:food_id>/', views.detail_food, name='detail_food'),
    path('cart/<int:customer_id>/', views.cart, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('my_order/', views.my_order, name='my_order'),
    path('order_detail/', views.order_detail, name='order_detail'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('login_view/', views.login_view, name='login_view'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('add_plus_1/', views.add_plus_1, name='add_plus_1'),
    path('minus_plus_1/', views.minus_plus_1, name='minus_plus_1'),
    path('get-wards/<int:district_id>', views.get_wards, name='get_wards'),
    path('detail_order/<int:order_id>/', views.detail_order, name='detail_order'),
    # admin
    path('admin_menu/', views.admin_menu, name='admin_menu'),
    path('add_food/', views.add_food, name='add_food'),
    path('delete_food/<int:food_id>/', views.delete_food, name='delete_food'),
    path('order_admin/', views.order_admin, name='order_admin'),
    
    path('template/', views.template, name='template'),
]