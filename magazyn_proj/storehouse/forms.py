from django import forms
from db_handler import admin_select
from db_handler import zam_order


class SelectProductToPurchase(forms.Form):
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)
    ilosc=forms.IntegerField(required=False,label = 'ilosc',min_value=1)
    cena=forms.DecimalField(required=False,label = 'cena',min_value=1)
    
class CreateOrder(forms.Form):
    CHOICES=([1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10])

    id_zamowienia = forms.CharField(required=False,label = 'id_zamowienia', max_length=1000)
    id_magazyn=forms.ChoiceField(required=False,label = 'id_magazyn',choices=CHOICES)
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

class Payment(forms.Form):
    #CHOICES=(['przelew','przelew'])
    sposob = forms.CharField(required=False,label = 'sposob')
    kwota = forms.DecimalField(required=False,label = 'kwota')

    CHOICES=(['zlecono','zlecono'],['zrealizowano','zrealizowano'])
    status = forms.ChoiceField(required=False,label = 'status', widget=forms.Select, choices=CHOICES)
