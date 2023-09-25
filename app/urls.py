from django.urls import path
from .views import *

urlpatterns =[
    path('home/', home, name='home'),
    path('breakfast/', breakfast, name='breakfast'),
    path('lunch/', lunch, name='lunch'),
    path('dinner/', dinner, name='dinner'),
    path('drinks/', drinks, name='drinks'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart' ),
    path('adminhome/', adminhome, name='adminhome'),
    path('edit_food/<uuid>/', edit_food, name='edit_food'),
    path('delete_food/<uuid>/', delete_food, name='delete_food'),
    path('admdrinks/', admdrinks, name='admdrinks'),
    path('admdinner/', admdinner, name='admdinner'),
    path('admbreakfast/', admbreakfast, name='admbreakfast'),
    path('admlunch/', admlunch, name='admlunch'),
    path('edit_admdrinks/<uuid>/', edit_admdrinks, name='edit_admdrinks'),
    path('edit_admdinner/<uuid>/', edit_admdinner, name='edit_admdinner'),
    path('edit_admbreakfast/<uuid>/', edit_admbreakfast, name='edit_admbreakfast'),
    path('edit_admlunch/<uuid>/', edit_admlunch, name='edit_admlunch'),
    path('delete_admdrinks/<uuid>/', delete_admdrinks, name='delete_admdrinks'),
    path('delete_admdinner/<uuid>/', delete_admdinner, name='delete_admdinner'),
    path('delete_admbreakfast/<uuid>/', delete_admbreakfast, name='delete_admbreakfast'),
    path('delete_admlunch/<uuid>/', delete_admlunch, name='delete_admlunch'),
]