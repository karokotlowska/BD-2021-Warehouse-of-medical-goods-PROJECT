from django import forms
from db_handler import admin_select
from db_handler import zam_order

class SearchOrder(forms.Form):
    id_zamowienia = forms.CharField(required=False,label = 'id_zamowienia', max_length=1000)

class SelectProductToReceive(forms.Form):
    ilosc=forms.IntegerField(required=False,label = 'ilosc')
    cena=forms.IntegerField(required=False,label = 'cena')
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)

class SelectProductToPurchase(forms.Form):
    ilosc=forms.IntegerField(required=False,label = 'ilosc')
    magazyn=forms.IntegerField(required=False,label = 'id_magazyn')
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)

class SelectProductToPurchase2(forms.Form):
    ilosc=forms.IntegerField(required=False,label = 'ilosc')
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)