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


def get_product_quantity_in_order(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT ilosc FROM magazyn.zamowienie_szczegoly WHERE numer_kolejny_zamowienia =  \'{}\';".format(id)
    cur.execute(insert_query)
    con.commit()
    if cur.rowcount !=0:
        ilosc=cur.fetchone()[0]
        cur.close()
        con.close()
        return ilosc  
    else:
        cur.close()
        con.close()
        return 0

def get_product_quantity_in_magazyn(id,id_product):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT ilosc FROM magazyn.magazyn_stan WHERE id_magazyn =  {} AND id_produkt = {};".format(id,id_product)
    cur.execute(insert_query)
    con.commit()
    if cur.rowcount !=0:
        ilosc=cur.fetchone()[0]
        cur.close()
        con.close()
        return ilosc  
    else:
        cur.close()
        con.close()
        return 0
 


def get_price(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT cena FROM magazyn.zamowienie_szczegoly WHERE numer_kolejny_zamowienia =  \'{}\';".format(id)
    cur.execute(insert_query)
    con.commit()
    cena= cur.fetchone()[0]
    cur.close()
    con.close()
    print(cena)
    return cena

def get_id_magazyn(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT id_magazyn FROM magazyn.zamowienie WHERE numer_kolejny_zamowienia =  \'{}\';".format(id)
    cur.execute(insert_query)
    con.commit()
    id_magazyn= cur.fetchone()[0]
    cur.close()
    con.close()
    print(id_magazyn)
    return id_magazyn

def zam_receipt_product(form,id,user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cena=get_price(id)
    kwota=int(form['ilosc'])*int(cena)
    old_kwota=get_kwota(id)-kwota
    id_magazyn=get_id_magazyn(id)



    quantity=get_product_quantity_in_order(id)
    quantity2=get_product_quantity_in_magazyn(id_magazyn,form['produkt'])
    try:
        if quantity>form['ilosc']:
            pass
        else:
            query_db='UPDATE magazyn.zamowienie SET kwota = {} WHERE numer_kolejny_zamowienia = {}; '.format(old_kwota,id)
            query_db += 'UPDATE magazyn.zamowienie_szczegoly SET ilosc = {} WHERE numer_kolejny_zamowienia = {} AND id_produkt = \'{}\';'.format( quantity-form['ilosc'],int(id),form['produkt'])
            if quantity2 !=0:
                query_db+="UPDATE magazyn.magazyn_stan SET ilosc =  {} WHERE id_magazyn =  {} AND id_produkt =  {};".format(quantity2+form['ilosc'],id_magazyn,form['produkt'])
            else:
                query_db+="INSERT INTO magazyn.magazyn_stan (id_produkt,id_magazyn,ilosc) VALUES ({}, {}, {});".format(form['produkt'],id_magazyn,form['ilosc'])
                print("pppppp")

            query_db+="INSERT INTO magazyn.magazyn_operacje (id_produkt,numer_kolejny_zamowienia,data_operacji, ilosc,rodzaj_operacji, id_magazyn,id_pracownik) VALUES ({},{},current_date,{}, 'prz', {},{})".format(form['produkt'],id,form['ilosc'],id_magazyn,user_id)
            cur.execute(query_db)
            con.commit()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
        
        cur.close()
        con.close()