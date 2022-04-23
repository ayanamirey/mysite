from django import forms

from shop.models import Shop


class ShopForm(forms.ModelForm):
    title = forms.CharField(
        label='Название пота',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название поста'})
    ),
    text = forms.CharField(
        label='Описание продукта',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название поста'
        })
    )

    class Meta:
        model = Shop
        fields = ('title', 'text')
