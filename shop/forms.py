from django.forms import models
from .models import Review

class ReviewForm(models.ModelForm):
    class Meta:
        model = Review
        fileds = ['review','stars']
