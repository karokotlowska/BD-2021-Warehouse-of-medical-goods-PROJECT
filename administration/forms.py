from django import forms


class InsertPracownik_stanowisko(forms.Form):
    id_stanowisko = forms.CharField(label = 'id_stanowisko', max_length=1000)
    opis= forms.CharField(label = 'opis', max_length=1000)

class InsertPracownik(forms.Form):
    imie = forms.CharField(label = 'imie', max_length=1000)
    email= forms.CharField(label = 'email', max_length=1000)
    nazwisko= forms.CharField(label = 'nazwisko', max_length=1000)
    login=forms.CharField(label = 'login', max_length=1000)
    haslo=forms.CharField(label = 'haslo', max_length=1000)

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
    id_stanowisko = forms.CharField(label = 'id_stanowisko', max_length=1000)
    opis= forms.CharField(label = 'opis', max_length=1000)

class DeletePracownik_stanowisko(forms.Form):
    id_stanowisko = forms.CharField(label = 'id_stanowisko', max_length=1000)

class DeletePracownik(forms.Form):
    id_pracownik=forms.CharField(label = 'id_pracownik', max_length=1000)