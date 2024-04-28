from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from products.models import Trainer, Product, Cart, CartItem, Contact
from strongcore import settings


class TrainerListView(LoginRequiredMixin, ListView):
    template_name = 'trainer/list_trainers.html'
    model = Trainer
    context_object_name = 'trainers'

    def get_queryset(self):
        return Trainer.objects.all()


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'products/list_products.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class SubscriptionTemplateView(TemplateView):
    template_name = 'subscriptions/subscriptions.html'


@login_required
def cart_view(request):
    cart = get_open_cart(request)
    return render(request, 'cart.html', {'cart': cart})


@login_required
def get_open_cart(request):
    user = request.user
    open_cart, created = Cart.objects.get_or_create(status='open', user=user)
    return open_cart


@login_required
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id', Product.objects.first().id)
        quantity = request.POST.get('quantity', 1)
        cart = get_open_cart(request)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)
        cart_item.quantity += int(quantity)
        if cart_item.quantity > 0:
            cart_item.save()
        else:
            cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', reverse_lazy('cart')))

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'home/homepage.html'
    fields = '__all__'
    success_url = reverse_lazy('homepage')

def checkout_view(request):
    open_cart = get_open_cart(request)
    open_cart.status = 'closed'
    open_cart.save()
    send_mail(subject='subiect', message='mesaj', from_email=settings.EMAIL_HOST_USER , recipient_list=[settings.EMAIL_HOST_USER,open_cart.user.email], fail_silently=False)
    return redirect(request.META.get('HTTP_REFERER'))

