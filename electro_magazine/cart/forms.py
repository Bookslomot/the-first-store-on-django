from django import forms

from cart.models import Order


class OrderForm(forms.ModelForm):

    order_date = forms.DateTimeField(label='Дата доставки', widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )


