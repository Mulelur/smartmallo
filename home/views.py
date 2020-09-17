from django.shortcuts import render
from shop.models import Product
from cart.views import get_user_pending_order, Profile
from django.shortcuts import render_to_response
from django.template import RequestContext
from categories.models import Subcategory, Category

def home(request):
    
    category = Category.objects.all()
    product =  Product.objects.all()
    existing_order = get_user_pending_order(request)
    Featured = Product.objects.filter(status='Featured')
    On_Sale = Product.objects.filter(status='On_Sale')
    Best_Rated = Product.objects.filter(status='Best_Rated')
    Best_Seller = Product.objects.filter(status='Best_Seller')
    DOF = Product.objects.filter(status='DOF')
    In_Stock = Product.objects.filter(status='In_Stock')
    # home = Product.objects.filter(Category_id=3)



    
    context = {
        'categories': category,
        'product': product,
        'On_Sale': On_Sale,
        'Featured': Featured,
        'Best_Seller': Best_Seller,
        'DOF': DOF,
        'Best_Rated': Best_Rated,
        'In_Stock': In_Stock,
        'order': existing_order
        
    }
    return render(request, 'home/index.html', context)

def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response
    