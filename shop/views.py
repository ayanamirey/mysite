from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.forms import ShopForm
from shop.models import Shop


def home(request):
    qs = Shop.objects.all()
    context = {'qs': qs}
    return render(request, 'shop/home.html', context)


def about(request):
    return render(request, 'shop/about.html')


class ShopCreateView(CreateView):
    model = Shop
    # fields = ['title', ]
    form_class = ShopForm
    template_name = 'shop/create.html'
    success_url = reverse_lazy('home')
