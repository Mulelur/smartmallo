from django.urls import path
from . import views as help_views

urlpatterns = [
    path('', help_views.help, name='help'),
    path('faqs/', help_views.faqs, name='faqs'),
]