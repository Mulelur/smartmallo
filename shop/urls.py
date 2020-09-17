from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.list_view, name='shop-list'),
    path('product/<int:pk>/', views.detail_view, name='shop-detail'),
    # path('search/', views.search, name='search-1')
]