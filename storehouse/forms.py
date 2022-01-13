from django import forms
from db_handler import admin_select
from db_handler import zam_order


class SelectProductToPurchase(forms.Form):
    ilosc=forms.IntegerField(required=False,label = 'ilosc')
    cena=forms.IntegerField(required=False,label = 'cena')
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)

class CreateOrder(forms.Form):
    id_zamowienia = forms.CharField(required=False,label = 'id_zamowienia', max_length=1000)
    id_magazyn= forms.IntegerField(required=False,label = 'id_magazyn')
    CHOICES=zam_order.companyList()
    company = forms.ChoiceField(required=False,label = 'id_firmy', widget=forms.Select, choices=CHOICES)

class EditOrder(forms.Form):
    id_zamowienia = forms.CharField(required=False,label = 'id_zamowienia', max_length=1000)


class ProductToDelete(forms.Form):
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)

class OrderStatus(forms.Form):
    CHOICES=(['aktywne','aktywne'], ['w realizacji','w realizacji'],['zrealizowane','zrealizowane'])
    status=forms.ChoiceField(required=False,label = 'status', widget=forms.Select, choices=CHOICES)