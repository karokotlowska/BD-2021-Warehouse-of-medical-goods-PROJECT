from magazyn_proj import settings
import psycopg2



def zam_create_order(form,id):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query ="INSERT INTO magazyn.zamowienie (numer_kolejny_zamowienia, id_zamowienia, id_magazyn,data_stworzenia, status, id_pracownik, id_firmy) VALUES(DEFAULT, UPPER(\'{}\'),{}, current_date, 'aktywne',{}, \'{}\') RETURNING numer_kolejny_zamowienia;".format(form['id_zamowienia'],form['id_magazyn'],id,form['company'], )
        cur.execute(insert_query)
        con.commit()
        id2= cur.fetchone()[0]
        cur.close()
        con.close()
        print("----+++")
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query="INSERT INTO magazyn.platnosc (numer_kolejny_zamowienia, status, sposob, kwota_platnosci, data_zrealizowania) VALUES ({},\'{}\',\'{}\',{}, current_date ); ".format(id2,'nie wybrano', 'nie wybrano',0.0)
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
        return id2
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
    

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
    try:
        product_exists_in_zamowienie=get_product_quantity_in_zamowienie(id,form['produkt'])
        query_db=''

        if product_exists_in_zamowienie!=0:
            cur.close()
            con.close()
            raise Exception("Ten produkt już dodano")
            
        else:
            query_db += 'INSERT INTO magazyn.zamowienie_szczegoly (numer_kolejny_zamowienia, id_produkt, ilosc,cena) VALUES ({}, {} , {} ,{});'.format(int(id),form['produkt'], form['ilosc'], form['cena'])
    
        cur.execute(query_db)
        con.commit()
        cur.close()
        con.close()

    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
    
def get_order_id(id_zamowienia):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "SELECT numer_kolejny_zamowienia FROM magazyn.zamowienie WHERE id_zamowienia =  \'{}\';".format(id_zamowienia.upper())
        cur.execute(insert_query)
        con.commit()
        id= cur.fetchone()[0]
        cur.close()
        con.close()
        if id==0:
            raise Exception("Brak takiego zamowienia")
        else:
            return id
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
        
def get_order_id2(id_zamowienia):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "SELECT numer_kolejny_zamowienia FROM magazyn.zamowienie WHERE id_zamowienia =  \'{}\' AND status != \'aktywne\';".format(id_zamowienia.upper())
        cur.execute(insert_query)
        con.commit()
        id= cur.fetchone()[0]
        cur.close()
        con.close()
        if id==0:
            raise Exception("Brak takiego zamowienia")
        else:
            return id
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
   

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

def get_product_quantity_in_zamowienie(id,id_product):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT ilosc FROM magazyn.zamowienie_szczegoly WHERE id_produkt =  {} AND numer_kolejny_zamowienia = {};".format(id_product,id)
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
        return None
 


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

def check_id_magazyn_in_zamowienie():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT z.id_magazyn FROM magazyn.zamowienie z JOIN magazyn.zamowienie_szczegoly zs USING (numer_kolejny_zamowienia) JOIN magazyn.magazyn_operacje mo USING (numer_kolejny_zamowienia);"
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


def zam_receipt_product(form,numer_kolejny_zamowienia,user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    id_magazyn=get_id_magazyn(numer_kolejny_zamowienia)
    product_exists_in_magazyn=get_product_quantity_in_magazyn(id_magazyn,form['produkt'])
    try:
        if product_exists_in_magazyn!=None:
            query_db="UPDATE magazyn.magazyn_stan SET ilosc =  {} WHERE id_magazyn =  {} AND id_produkt =  {};".format(product_exists_in_magazyn+form['ilosc'],id_magazyn,form['produkt'])
            query_db+="INSERT INTO magazyn.magazyn_operacje (id_produkt,numer_kolejny_zamowienia, ilosc,rodzaj_operacji, id_magazyn,id_pracownik) VALUES ({},{},{}, 'prz', {},{}); ".format(form['produkt'],numer_kolejny_zamowienia,form['ilosc'],id_magazyn,user_id)
            cur.execute(query_db)
            con.commit()
            cur.close()
            con.close()
        else:
            query_db="INSERT INTO magazyn.magazyn_stan (id_produkt,id_magazyn,ilosc) VALUES ({}, {}, {});".format(form['produkt'],id_magazyn,form['ilosc'])
            query_db+="INSERT INTO magazyn.magazyn_operacje (id_produkt,numer_kolejny_zamowienia, ilosc,rodzaj_operacji, id_magazyn,id_pracownik) VALUES ({},{},{}, 'prz', {},{}); ".format(form['produkt'],numer_kolejny_zamowienia,form['ilosc'],id_magazyn,user_id)
            cur.execute(query_db)
            con.commit()
            cur.close()
            con.close()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
        

def check_if_platnosc_exists(id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "SELECT * FROM magazyn.platnosc WHERE numer_kolejny_zamowienia = {};".format(id)
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


def zam_add_payment(form,id):
    '''check=check_if_platnosc_exists(id)'''
    try:
        ''' if check==0:'''
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "INSERT INTO magazyn.platnosc (numer_kolejny_zamowienia, status, sposob, data_zrealizowania, kwota_platnosci)VALUES ({},\'{}\',\'{}\',current_date,{}) ;".format(id,form['status'],form['sposob'], form['kwota'])
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
        '''else:
            con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
            cur = con.cursor()
            insert_query = "UPDATE magazyn.platnosc SET numer_kolejny_zamowienia = {}, status = \'{}\', sposob = \'{}\', data_zrealizowania = current_date ; ".format(id,form['status'],form['sposob'])
            cur.execute(insert_query)
            con.commit()
            cur.close()
            con.close()'''
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'