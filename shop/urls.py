from django.urls import path
from shop.views import home, about, ShopCreateView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('add/', ShopCreateView.as_view(), name='create'),
]
