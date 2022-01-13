from magazyn_proj import settings
import psycopg2



def zam_create_order(form,id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO magazyn.zamowienie (numer_kolejny_zamowienia,id_zamowienia, id_magazyn,data_stworzenia, status, id_pracownik, id_firmy) VALUES(DEFAULT, \'{}\',{}, current_date, 'aktywne',{}, \'{}\') RETURNING numer_kolejny_zamowienia;".format(form['id_zamowienia'],form['id_magazyn'],id,form['company'], )
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
    return table_data

def storehouse_order_select(resource):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT * FROM magazyn.zamowienie WHERE id_zamowienia = \'{}\';'.format(resource)
    cur.execute(query_db)
    table_data = cur.fetchall()
    cur.close()
    con.close()
    return table_data

def get_kwota(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = 'SELECT kwota FROM magazyn.zamowienie WHERE numer_kolejny_zamowienia = {};'.format(int(id))
    cur.execute(query_db)
    kwota= cur.fetchone()[0]
    con.commit()
    cur.close()
    con.close()
    if kwota:
        return kwota
    else:
        return 0

def zam_insert_product(form,id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    kwota=int(form['ilosc'])*int(form['cena'])
    old_kwota=kwota+get_kwota(id)
    query_db='UPDATE magazyn.zamowienie SET kwota = {} WHERE numer_kolejny_zamowienia = {}; '.format(old_kwota,id)
    query_db += 'INSERT INTO magazyn.zamowienie_szczegoly (numer_kolejny_zamowienia, id_produkt, ilosc,cena) VALUES ({}, {} , {} ,{});'.format(int(id),form['produkt'], form['ilosc'], form['cena'])
    cur.execute(query_db)
    con.commit()
    cur.close()
    con.close()
    
def get_order_id(id_zamowienia):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT numer_kolejny_zamowienia FROM magazyn.zamowienie WHERE id_zamowienia =  \'{}\';".format(id_zamowienia)
    cur.execute(insert_query)
    con.commit()
    id= cur.fetchone()[0]
    cur.close()
    con.close()
    return id

def zam_chenge_status(form,id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "UPDATE magazyn.zamowienie SET status = \'{}\' WHERE numer_kolejny_zamowienia = {};".format(form['status'],id)
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

def zam_del_product(form, id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "DELETE FROM magazyn.zamowienie_szegoly WHERE id_pracownik= \'{}\' ;".format(form['id_pracownik'])
    insert_query += "DELETE FROM magazyn.pracownik WHERE id_pracownik= \'{}\' ;".format(form['id_pracownik'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()