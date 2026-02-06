from django import forms


class CheckoutForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=128, required=True)
    phone_number = forms.CharField(label="Телефон", max_length=20, required=True)
