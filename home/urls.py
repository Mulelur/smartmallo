from django.urls import path
from django.conf.urls import handler404
from . import views

handler404 = 'home.views.handler404'
# handler500 = 'my_app.views.handler500'
urlpatterns = [
    path('', views.home, name='home'),
    
]