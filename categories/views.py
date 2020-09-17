from django.shortcuts import render, get_object_or_404
from shop.models import Product
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Category

def categorie(request, slug):
    template = 'categorie/category-detail.html'

    category = get_object_or_404(Category.objects.all(), slug=slug)

    # paginator = Paginator(product_cat, 20) # Show 25 contacts per page.
    
    # product = Product.objects.all()
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # categorys = Category.objects.all()
    # context = {
    #     'cat': category,
     
    #     'categories': categorys,
    #     'page_obj': page_obj,
    #     'product': product
    #     # 'images': Images.objects.filter(slug__iexact=img)

    # }
    return render(request, template)

def search(request):
    
    # try:
    #     q = request.GET.get('q')
    #     c = request.GET.get('c')
    # except:
    #     q = None
    #     C = None 

    # if q or c :
    #     
    #     product = Product.objects.filter(Q(name__icontains=q) | Q(category__icontains=c)) 
    categorys = Category.objects.all()

    queryset = Product.objects.order_by('-list_date')

    if 'q' in request.GET:
        qs = request.GET['q']
        if qs:
            query_set = queryset.filter(Q(name__icontains=qs))

        paginator = Paginator(query_set, 20) # Show 25 contacts per page.
    
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        template = 'categorie/search_results.html'
        context = {'query': qs, 'products': query_set, 'categories': categorys, 'page_obj': qs}
    else:
        template = 'categorie/search.html'
        context = {}    
    return render(request, template, context)    

def product_category(request):

    template = 'categorie/product-category.html'
    category = Category.objects.all()
    categorys = Category.objects.all()

    context = {

        'category': category,
        'categories': categorys,

    }
    return render(request, template, context)    
   
def product_detail(request, slug):
    template = 'categorie/product-detail.html'

    return render(request, template)