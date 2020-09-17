from django.shortcuts import render, get_object_or_404
from .models import Article, Category, SubCategory, CSA


def article_list(request, category_slug):
    template = 'article/article_list.html'
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = SubCategory.objects.all()
    article = Article.objects.filter(category=category)
    categories = Category.objects.all()
    article_c = Article.objects.all()
    context = {
        'category': category,
        'subcategory': subcategory,
        'article': article,
        'categories': categories,
        'article-c': article_c
    }
    return render(request, template, context)


def article_list_detail(request, sub_category_slug, category_slug):
    template = 'article/article_list_detail.html'
    sub_category = SubCategory.objects.get(slug=sub_category_slug)
    subcategory = SubCategory.objects.filter(slug=sub_category_slug)
    category = get_object_or_404(Category, slug=category_slug)
    # subart = Article.objects.all()
    csa = CSA.objects.all()
    article = Article.objects.filter(subcategory_slug=sub_category_slug)
    categories = Category.objects.all()

    context = {
        'category': category,
        'sub_category': sub_category,
        'article': article,
        'categories': categories,
        'csa': csa,
        'subcategory': subcategory
        # 'subart': subart'
    }
    return render(request, template, context)


def article_detail(request, sub_category_slug, category_slug, article_slug):
    template = 'article/article.html'
    sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
    category = Category.objects.filter(slug=category_slug)
    article = get_object_or_404(Article, slug=article_slug)
    categories = Category.objects.all()
    subcategory = SubCategory.objects.filter(slug=sub_category)

    context = {
        'article': article,
        'category': category,
        'sub_category': sub_category,
        'categories': categories,
        'subcategory': subcategory
    }
    return render(request, template, context)


def returns_exchange(request):
    template = 'account/returns_exchange.html'
    article = Article.objects.all()
    context = {'article': article}
    return render(request, template, context)
