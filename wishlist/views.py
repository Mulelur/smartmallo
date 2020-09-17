from django.shortcuts import render, redirect, get_object_or_404
from .models import WishListOrderItem, WishListOrder
from account.models import Profile
from shop.models import Product,Category 
from cart.views import generate_order_id
from django.contrib import messages
from django.urls import reverse


def get_user_pending(request):
    # get order for the correct user
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)
        order = WishListOrder.objects.filter(owner=user_profile, is_ordered=False)
        if order.exists():
            # get the only order in the list of filtered orders
            return order[0]
        return 0
    else:
        return " "    


def add_to_wishlist(request, **kwargs):
   
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.product.all():
        messages.info(request, 'You already added this product')
        return redirect(reverse('shop-list'))     
    # create orderItem of the selected product

    order_item, status = WishListOrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = WishListOrder.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to wishlist")
    return redirect(reverse('shop-list'))
            
    context = {
         
    }

    return render(request, template, context)        



def delete_from_wishlist(request, item_id):
    item_to_delete = WishListOrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('wishlist:wishlist'))

def wishlist(request, **kwargs):

    template = 'wishlist/wishlist.html'
    category = Category.objects.all()
    eo = get_user_pending(request)
    context = {

        'categories': category,
        'eo': eo

    }
    return render(request, template, context)

    



    
