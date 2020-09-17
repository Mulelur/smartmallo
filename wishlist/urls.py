from django.urls import path
from . import views as wishlist_views

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_views.wishlist, name='wishlist'),
    path('add-to-cart/<int:item_id>/', wishlist_views.add_to_wishlist, name="add_to_wishlist"),
    path('wishlist-item/delete/<int:item_id>/', wishlist_views.delete_from_wishlist, name='delete_wishlist_item'),
]