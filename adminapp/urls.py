from django.urls import path
from adminapp.views import categories, products, users

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', users.user_create, name='user_create'),
    path('users/read/', users.users, name='users'),
    path('users/update/<int:pk>/', users.user_update, name='user_update'),
    path('users/delete/<int:pk>/', users.user_delete, name='user_delete'),

    path('categories/create/', categories.category_create, name='category_create'),
    path('categories/read/', categories.categories, name='categories'),
    path('categories/update/<int:pk>/', categories.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', categories.category_delete, name='category_delete'),

    path('products/create/category/<int:pk>/', products.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', products.products, name='products'),
    path('products/read/<int:pk>/', products.product_read, name='product_read'),
    path('products/update/<int:pk>/', products.product_update, name='product_update'),
    path('products/delete/<int:pk>/', products.product_delete, name='product_delete'),
]