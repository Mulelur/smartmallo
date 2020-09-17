from django.shortcuts import render


def help(request):
    template = 'help/help.html'

    category = Category.objects.all()
    context = {'categories': category}
    return render(request, template, context)

def faqs(request):
    template = 'help/faqs.html'

    category = Category.objects.all()
    context = {'categories': category}
    return render(request, template, context)