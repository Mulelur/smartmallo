from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import TrackOrder,Shipping

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TrackOrderForm(forms.ModelForm):
    class Meta:
        model = TrackOrder
        fields = ['Order_number']   

class UserShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['first_name', 'last_name', 'street_address', 'phone', 'city', 'State', 'zip_code']



class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )
class PasswordProfileForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = (
            'password1', 'password2'
        )

    