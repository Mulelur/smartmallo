from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Shipping, TrackOrder
from django.urls import reverse
from categories.models import Category
from cart.models import Order
from django.forms import inlineformset_factory
from .forms import UserRegisterForm, UserShippingForm, EditProfileForm, PasswordProfileForm, TrackOrderForm
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def profile(request):
    template = 'account/profile.html'

    return render(request, template)

@login_required
def my_account(request):
    template = 'account/my_account.html'

    category = Category.objects.all()
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)

    context = {
        'my_orders': my_orders,
        'categories': category,
    }

    return render(request, template, context)


def order_tracking(request):
    category = Category.objects.all()
    form = TrackOrderForm(request.GET or None)
    if request.method == 'GET':
        get_traking_number = TrackOrder.objects.all()
        # email = User.objects.get(email=request.user)

    template = 'account/order_tracking.html'

    context = {'form': form,'categories': category}
    return render(request, template, context)


def customer_services(request):

    category = Category.objects.all()
    template = 'account/customer_services.html'

    context = {'categories': category,}
    return render(request, template, context)


def delivery(request):
    category = Category.objects.all()
    template = 'account/delivery.html'
    form = UserShippingForm()
    if request.method == 'POST':
        form = UserShippingForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('delivery'))

    context = {'form': form,'categories': category,}
    return render(request, template, context)


def edit_profile(request):
    category = Category.objects.all()
    template = 'account/edit_profile.html'
    if request.method == 'POST':
        editform = EditProfileForm(request.POST, instance=request.user)
        passwordform = PasswordProfileForm(
            data=request.POST, user=request.user)

        if editform.is_valid() or passwordform.is_valid():
            editform.save()
            return redirect(reverse('edit_profile'))
        if passwordform.is_valid():
            passwordform.save()
            update_session_auth_hash(request, passwordform.user)
            return redirect(reverse('edit_profile'))
    else:
        passwordform = PasswordProfileForm(user=request.user)
        editform = EditProfileForm(instance=request.user)
        context = {'editform': editform, 'passwordform': passwordform,'categories': category}
        return render(request, template, context)


def search(request):
    category = Category.objects.all()
    queryset = Order.objects.order_by('-list_date')

    if 'q' in request.GET:
        qs = request.GET['q']
        if qs:
            query_set = query_set.filter(description__icontains=q)

    context = {'qurey': qs,'categories': category}
    return render(request, template, context)
