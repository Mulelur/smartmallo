from django.shortcuts import render, get_object_or_404
from .models import Product, Images, Category, Review, Connection, Subcategory
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from asset.models import Benar
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.models import Order, OrderItem
from cart.views import get_user_pending_order, Profile, generate_order_id


def list_view(request):
    template = 'shop/product_list.html' 

    product = Product.objects.all()
    existing_order = get_user_pending_order(request)
    benar = Benar.objects.all()
    category = Category.objects.all()
    # get_banner = Benar.objects.get(id=benar.id)

    paginator = Paginator(product, 20) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': category,
        'page_obj': page_obj,
        'product': product,
        'benar': benar,
        'order': existing_order,
        
    }

   
    return render(request, template, context)

def detail_view(request, pk):
    template = 'shop/product_detail.html'
    img = Images.objects.filter(product=pk)
    existing_order = get_user_pending_order(request)
    reviews = Review.objects.filter(product=pk)
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    product = get_object_or_404(Product.objects.all(), pk=pk)
    # get ProductOrderItemForm
   
    context = {
        'product': product,
        'img': img,
        'reviews': reviews,
        'order': existing_order,
        'current_order_products': current_order_products,
      
 
        # 'images': Images.objects.filter(slug__iexact=img)

    }
    return render(request, template, context)


# def search(request):
#     template = 'categorie/search_results.html'
#     queryset = Product.objects.order_by('-list_date')

#     if 'q' in request.GET:
#         qs = request.GET['q']
#         if qs:
#             query_set = queryset.filter(name__icontains=qs)
#     context = {'qurey': qs}
#     return render(request, template, context)

