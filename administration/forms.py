from django import forms


class InsertPracownik_stanowisko(forms.Form):
    id_stanowisko = forms.CharField(label = 'id_stanowisko', max_length=1000)
    opis= forms.CharField(label = 'opis', max_length=1000)

class InsertPracownik(forms.Form):
    imie = forms.CharField(label = 'imie', max_length=1000)
    email= forms.CharField(label = 'email', max_length=1000)
    nazwisko= forms.CharField(label = 'nazwisko', max_length=1000)
    rola= forms.CharField(label = 'rola: adm/zam/mag', max_length=1000)
    login=forms.CharField(label = 'login', max_length=1000)
    haslo=forms.CharField(label = 'haslo', max_length=1000)


class InsertProdukt(forms.Form):
    opis=forms.CharField(label = 'nazwa produktu', max_length=1000)
    kategoria=forms.CharField(label = 'id kategorii', max_length=1000)


class InsertKategoria(forms.Form):
    id_kategoria=forms.CharField(label = 'id kategorii', max_length=1000)
    opis=forms.CharField(label = 'opis', max_length=1000)


class InsertLokalizacja(forms.Form):
    id_magazyn=forms.IntegerField(label = 'id magazynu', min_value=1)
    nr_magazynu=forms.IntegerField(label = 'numer magazynu', min_value=1)
    ulica=forms.CharField(label = 'ulica', max_length=6)
    kod_pocztowy=forms.CharField(label = 'kod pocztowy', max_length=1000)
    miasto=forms.CharField(label = 'miasto', max_length=1000)


class UpdateWeryfikacja(forms.Form):
    id_pracownik=forms.CharField(label = 'id_pracownik', max_length=1000)
    login=forms.CharField(label = 'login', max_length=1000)
    haslo=forms.CharField(label = 'haslo', max_length=1000)


class UpdatePracownik(forms.Form):
    id_pracownik=forms.CharField(label = 'id_pracownik', max_length=1000)
    imie = forms.CharField(label = 'imie', max_length=1000)
    email= forms.CharField(label = 'email', max_length=1000)
    nazwisko= forms.CharField(label = 'nazwisko', max_length=1000)
    login=forms.CharField(label = 'login', max_length=1000)
    haslo=forms.CharField(label = 'haslo', max_length=1000)

class UpdatePracownik_stanowisko(forms.Form):
    id_stanowisko = forms.CharField(label = 'id_stanowisko', max_length=3)
    opis= forms.CharField(label = 'opis', max_length=1000)

class DeletePracownik_stanowisko(forms.Form):
    id_stanowisko = forms.CharField(label = 'id_stanowisko', max_length=1000)

class DeletePracownik(forms.Form):
    id_pracownik=forms.CharField(label = 'id_pracownik', max_length=1000)

class DeleteProduct(forms.Form):
    id_produkt=forms.IntegerField(label = 'id_produkt', min_value=1)


class UpdateLokalizacja(forms.Form):
    id_magazyn=forms.IntegerField(label = 'id magazynu', min_value=1)
    ulica=forms.CharField(label = 'ulica', max_length=1000)
    kod_pocztowy=forms.CharField(label = 'kod pocztowy', max_length=6)
    miasto=forms.CharField(label = 'miasto', max_length=1000)
