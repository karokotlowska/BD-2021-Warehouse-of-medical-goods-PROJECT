from django import forms
from db_handler import admin_select
from db_handler import zam_order

class SearchOrder(forms.Form):
    id_zamowienia = forms.CharField(required=False,label = 'id_zamowienia', max_length=1000)

class SelectIDStorehouse(forms.Form):
    CHOICES=([1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10])
    magazyn=forms.ChoiceField(required=False,label = 'id_magazyn',choices=CHOICES)

class SelectProductToReceive(forms.Form):
    ilosc=forms.IntegerField(required=False,label = 'ilosc',min_value=1)
    cena=forms.DecimalField(required=False,label = 'cena',min_value=1)
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)

class SelectProductToPurchase(forms.Form):
    ilosc=forms.IntegerField(required=False,label = 'ilosc',min_value=1)
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)

class SelectToRemove(forms.Form):
    CHOICES=([1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10])
    magazyn=forms.ChoiceField(required=False,label = 'id_magazyn',choices=CHOICES)
    ilosc=forms.IntegerField(required=False,label = 'ilosc',min_value=1)
    CHOICES=admin_select.productList()
    produkt = forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)


class SearchStorehouse(forms.Form):
    CHOICES=admin_select.get_magazyny()
    magazyn=forms.ChoiceField(required=False,label = 'id_magazyn',choices=CHOICES)
    
class SelectProductToPurchase2(forms.Form):
    #produkt = forms.ChoiceField(required=True,choices=(),label = 'produkt')

    def __init__(self, *args, **kwargs):
       # CHOICES=admin_select.productListFromMagazyn(n)
        choices=kwargs.pop('my_choices')
        super(SelectProductToPurchase2, self).__init__(*args, **kwargs)
        self.fields['produkt'] = forms.ChoiceField(choices=choices,required=False,label = 'produkt')#forms.ChoiceField(required=False,label = 'produkt', widget=forms.Select, choices=CHOICES)
    ilosc=forms.IntegerField(required=False,label = 'ilosc',min_value=1)

    #produkt = forms.ChoiceField(required=False,choices=(),label = 'produkt')


