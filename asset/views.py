from django.shortcuts import render
from .models import Benar

def test(request):
    banner = Benar.objects.all()

    img = Benar.objects.filter(id__in=banner)
   
    context = {'banner': banner}      
    
    return render(request, 'categorie/test.html', context)