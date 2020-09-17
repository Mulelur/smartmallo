from django.shortcuts import render
from shop.models import Category
from cart.views import get_user_pending_order, Profile

def contact(request):
    template = 'contact/contact.html'
    category = Category.objects.all()
    existing_order = get_user_pending_order(request)
    context = {
        'categories': category,
        'order': existing_order
    }
    return render(request, template, context)
