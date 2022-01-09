from magazyn_proj import settings
import psycopg2



def zam_create_order(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    print(form['id_zamowienia'])
    insert_query = "INSERT INTO magazyn.zamowienie (numer_kolejny_zamowienia,id_zamowienia, id_magazyn,data_stworzenia, status, id_pracownik, id_firmy) VALUES(DEFAULT, \'{}\',{}, current_date, 'aktywne',1, \'{}\') RETURNING numer_kolejny_zamowienia;".format(form['id_zamowienia'],form['id_magazyn'],form['company'], )
    cur.execute(insert_query)
    con.commit()
    id= cur.fetchone()[0]
    cur.close()
    con.close()
    return id
    

def companyList():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT id_firmy, nazwa FROM magazyn.kontrahent ;'
    cur.execute(query_db)
    table_data = cur.fetchall()   
    cur.close()
    con.close()
    print(table_data)
    return table_data

def storehouse_order_select(resource):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT * FROM magazyn.zamowienie WHERE id_zamowienia = \'{}\';'.format(resource)
    cur.execute(query_db)
    table_data = cur.fetchall()
    cur.close()
    con.close()
    print(table_data)
    return table_data

def zam_insert_product(form,id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    kwota=int(form['ilosc'])*int(form['cena'])
    query_db = 'INSERT INTO magazyn.zamowienie_szczegoly (numer_kolejny_zamowienia, id_produkt, ilosc,cena, kwota) VALUES ({}, {} , {} ,{},{});'.format(int(id),form['produkt'], form['ilosc'], form['cena'],kwota )
    cur.execute(query_db)
    con.commit()
    cur.close()
    con.close()
    