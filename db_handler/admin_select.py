from magazyn_proj import settings
import psycopg2



tables = ['kategoria', 'produkt','pracownik_stanowisko','pracownik','weryfikacja', 'pracownik_role', 'kontrahent', 'zamowienie']
order_tables=['zamowienie']    
def get_column_names(cur):
    query_db = ['SELECT * FROM magazyn.{} LIMIT 0;'.format(table) for table in tables]
    result = {}
    for i in range(len(tables)):
        cur.execute(query_db[i])
        table_data = [desc[0] for desc in cur.description]
        result[tables[i]] = table_data
    return result

def get_order_column_names(cur):
    query_db = ['SELECT * FROM magazyn.{} LIMIT 0;'.format(table) for table in order_tables]
    result = {}
    for i in range(len(order_tables)):
        cur.execute(query_db[i])
        table_data = [desc[0] for desc in cur.description]
        result[tables[i]] = table_data
    return result

def admin_zamowienie_view(request):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT zamowienie_view.numer_kolejny_zamowienia,zamowienie_view.id_zamowienia, zamowienie_view.data_stworzenia, zamowienie_view.status, zamowienie_view.kwota, zamowienie_view.waluta_zamowienia FROM magazyn.zamowienie_view;'.format(request)
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['num. kolej. zam.', 'id zamówienia','data stworzenia','status','kwota','waluta']
    result["Zamówienia"] = [column_names,table_data]
    cur.close()
    con.close()
    return result

def admin_dict_select(request):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT * FROM magazyn.pracownik;'.format(request)
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = get_column_names(cur)
    result[request] = [column_names,table_data]
    cur.close()
    con.close()
    return result

def admin_pracownik_view(request):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT * FROM magazyn.pracownik_view;'.format(request)
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['imie','nazwisko','email','stanowisko']
    result["Pracownicy"] = [column_names,table_data]
    cur.close()
    con.close()
    return result

def admin_magazyn_stan_view(request):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT  magazyn_view.id_magazyn,magazyn_view.nr_magazynu,  magazyn_view.ulica,magazyn_view.miasto, magazyn_view.kod_pocztowy,magazyn_view.ilosc  FROM magazyn.magazyn_view;'.format(request)
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['id magaz.','nr. magaz.', 'ulica', 'miasto   ','kod poczt.','ilość prod. na magazynie']
    result['Przepełnione magazyny'] = [column_names,table_data]
    cur.close()
    con.close()
    return result

def admin_produkty_view(request):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT * FROM magazyn.produkty_view;'.format(request)
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['opis','kategoria']
    result[request] = [column_names,table_data]
    cur.close()
    con.close()
    return result


def productList():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT listaproduktow.id_prdukt, listaproduktow.opis FROM ListaProduktow();'
    cur.execute(query_db)
    mobile_records = cur.fetchall()   
    cur.close()
    con.close()


    cur.close()
    con.close()
    return mobile_records

def productListFromMagazyn(id_magazyn):
    
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT ListaProduktowMagazyn.id_produkt, ListaProduktowMagazyn.opis FROM magazyn.ListaProduktowMagazyn({});'.format(id_magazyn)
    cur.execute(query_db)
    table_data = cur.fetchall()   
    cur.close()
    con.close()
    print(table_data)
    return table_data

def admin_order_view_select( id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    print(id)
    query_db = 'SELECT numer_kolejny_zamowienia, id_zamowienia, id_magazyn, data_stworzenia, status, id_firmy, kwota FROM magazyn.zamowienie WHERE numer_kolejny_zamowienia =  {};'.format(int(id))
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['num.kolej.','id_zam.', 'id_mag.', 'data stworz.', 'status', 'id_firmy','kwota']
    result['ZAMÓWIENIE'] = [column_names,table_data]
    cur.close()
    con.close()
    return result

def order_details(id):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        print(id)
        print(id)
        print(id)
        print(id)
        query_db = 'SELECT  SzczegolyZamowienia.opis, SzczegolyZamowienia.ilosc, SzczegolyZamowienia.cena, SzczegolyZamowienia.kwota FROM magazyn.SzczegolyZamowienia({});'.format(int(id))
        result = {}
        cur.execute(query_db)
        table_data = cur.fetchall()
        column_names = [ 'produkt', 'ilosc', 'cena','kwota']
        print(table_data)
        result['PRODUKTY W ZAMÓWIENIU:'] = [column_names,table_data]
        cur.close()
        con.close()
        return result
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'

def edit_order_details(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT z.id_zamowienia, z.numer_kolejny_zamowienia, z.status,  z.id_firmy, zs.ilosc, zs.cena, p.opis, z.kwota FROM magazyn.zamowienie z LEFT JOIN magazyn.zamowienie_szczegoly zs ON z.numer_kolejny_zamowienia = zs.numer_kolejny_zamowienia JOIN magazyn.produkt P USING(id_produkt) WHERE z.id_zamowienia = \'{}\';'.format(id.upper())
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['id_zam.','num.kolej.zam.', 'status','id_firmy', 'ilosc', 'cena','produkt','kwota']
    #print(column_names)
    result['SZCZEGÓŁY ZAMÓWIENIA:'] = [column_names,table_data]
    cur.close()
    con.close()
    print(table_data)
    return result

def admin_profile_select(request,id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT p.imie, p.nazwisko, w.login, ps.opis FROM magazyn.pracownik P LEFT JOIN magazyn.weryfikacja W ON p.id_pracownik = w.id_pracownik LEFT JOIN magazyn.pracownik_role PR ON pr.id_pracownik = p.id_pracownik LEFT JOIN magazyn.pracownik_stanowisko PS ON ps.id_stanowisko = pr.id_stanowisko WHERE p.id_pracownik = {};'.format(id)
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['imie', 'nazwisko','login', 'stanowisko']
    result[request] = [column_names,table_data]
    cur.close()
    con.close()
    return result


def productListForSearch():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT z.numer_kolejny_zamowienia, p.opis, ms.ilosc FROM magazyn.zamowienie_szczegoly Z LEFT JOIN magazyn.produkt P USING (id_produkt) LEFT JOIN magazyn.magazyn_stan MS USING (id_produkt);'
    cur.execute(query_db)
    table_data = cur.fetchall()   
    cur.close()
    con.close()
    return table_data


def productListForSearch2():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT z.numer_kolejny_zamowienia, p.opis FROM magazyn.zamowienie_szczegoly Z LEFT JOIN magazyn.produkt P USING (id_produkt);'
    cur.execute(query_db)
    table_data = cur.fetchall()   
    cur.close()
    con.close()
    return table_data



def storehouse_view(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT p.opis, ilosc FROM magazyn.magazyn_stan JOIN magazyn.produkt P USING (id_produkt) WHERE id_magazyn = {};'.format(id)
    cur.execute(query_db)
    result = {}

    column_names = ['opis', 'ilosc']
    table_data = cur.fetchall()   

    result['Stan magazynu '+str(id)] = [column_names,table_data]
    cur.close()
    con.close()
    return result


def get_orders():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    result={}
    query_db = 'SELECT z.numer_kolejny_zamowienia, z.id_magazyn, z.data_stworzenia, z.kwota, z.waluta_zamowienia, p.status, p.sposob, p.kwota_platnosci FROM magazyn.zamowienie Z LEFT JOIN magazyn.platnosc P USING (numer_kolejny_zamowienia) ORDER BY z.numer_kolejny_zamowienia ASC;'
    cur.execute(query_db)
    column_names=['num. kolej. zam.', 'id_magaz.', 'data stworz. zam.', 'kwota', 'waluta', 'status', 'spos. płatności', 'kwota płatności'] 

    table_data = cur.fetchall()  
    result['PRZEGLĄD']=[column_names,table_data]
    cur.close()
    con.close()
    return result


 


def get_magazyny():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT id_magazyn, nr_magazynu FROM magazyn.magazyn_lokalizacje ORDER BY nr_magazynu;'
    cur.execute(query_db)
    mobile_records = cur.fetchall()   
    cur.close()
    con.close()


    cur.close()
    con.close()
    return mobile_records