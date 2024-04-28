from django.urls import path

from products import views

urlpatterns = [
    path('list_trainers/', views.TrainerListView.as_view(), name='list-trainers'),
    path('list_products/', views.ProductListView.as_view(), name='list-products'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_card/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('subscriptions/', views.SubscriptionTemplateView.as_view(), name='subscriptions'),
    path('contact/', views.ContactCreateView.as_view(), name='contact'),

]
