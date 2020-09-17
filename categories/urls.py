from django.urls import path
from . import views
from .views import product_category

app_name = 'category'

urlpatterns = [
    path('<str:slug>/', views.categorie, name='categorie'),
    path('', product_category, name='product-category'),
    # path('<str:slug>/', product_detail,name='product-detail')
]