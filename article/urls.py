from django.urls import path
from . import views
from .views import returns_exchange

app_name = 'article'

urlpatterns = [
    path('returns-exchange/', returns_exchange, name='returns_exchange'),
    path('<str:category_slug>/', views.article_list, name='article_list'),
    path('<str:category_slug>/<str:sub_category_slug>/', views.article_list_detail, name='article_list_detail'),
    # path('<str:category_slug>/<str:sub_category_slug>/', views.article_list_detail, name='article_list_detail'),
    path('<str:category_slug>/<str:sub_category_slug>/<str:article_slug>/', views.article_detail, name='article_detail'),
]