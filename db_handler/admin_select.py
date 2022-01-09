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
        print(tables[i])
    return result

def get_order_column_names(cur):
    query_db = ['SELECT * FROM magazyn.{} LIMIT 0;'.format(table) for table in order_tables]
    result = {}
    for i in range(len(order_tables)):
        cur.execute(query_db[i])
        table_data = [desc[0] for desc in cur.description]
        result[tables[i]] = table_data
        print(tables[i])
    return result

def admin_select():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = ['SELECT * FROM magazyn.{};'.format(table) for table in tables]
    column_names = get_column_names(cur)
    result = {}
    for i in range(len(tables)):
        cur.execute(query_db[i])
        table_data = cur.fetchall()
        result[tables[i]] = [column_names[tables[i]],table_data]
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

def productList():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT id_produkt,opis FROM magazyn.produkt ;'
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
    query_db = 'SELECT numer_kolejny_zamowienia, id_zamowienia, id_magazyn, data_stworzenia, status, id_firmy FROM magazyn.zamowienie WHERE numer_kolejny_zamowienia =  {};'.format(int(id))
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['numer_kolejny_zamowienia','id_zamowienia', 'id_magazyn', 'data_stworzenia', 'status', 'id_firmy']
    result['ZAMÓWIENIE'] = [column_names,table_data]
    cur.close()
    con.close()
    return result

def order_details(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    print(id)
    query_db = 'SELECT numer_kolejny_zamowienia, id_produkt, kwota, ilosc, cena FROM magazyn.zamowienie_szczegoly WHERE numer_kolejny_zamowienia = \'{}\';'.format(int(id))
    result = {}
    cur.execute(query_db)
    table_data = cur.fetchall()
    column_names = ['numer_kolejny_zamowienia', 'id_produkt', 'kwota', 'ilosc', 'cena',]
    print(column_names)
    result['PRODUKTY W ZAMÓWIENIU:'] = [column_names,table_data]
    cur.close()
    con.close()
    return result


