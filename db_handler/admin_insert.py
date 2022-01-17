from magazyn_proj import settings
import psycopg2

def insert_pracownik_stanowisko(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "INSERT INTO magazyn.pracownik_stanowisko VALUES(\'{}\', \'{}\');".format(form['id_stanowisko'], form['opis'])
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
        return 1
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'


def insert_pracownik(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "INSERT INTO magazyn.pracownik VALUES(DEFAULT, \'{}\',\'{}\', \'{}\'); ".format(form['imie'],form['email'], form['nazwisko'] )
        insert_query += "INSERT INTO magazyn.weryfikacja (id_pracownik, login,haslo) VALUES((SELECT MAX(id_pracownik) FROM magazyn.pracownik),\'{}\', \'{}\');".format( form['login'], form['haslo'])
        insert_query += "INSERT INTO magazyn.Pracownik_role (id_pracownik, id_stanowisko) VALUES((SELECT MAX(id_pracownik) FROM magazyn.pracownik),\'{}\');".format(form['rola'])

        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'


def insert_produkt(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "INSERT INTO magazyn.produkt VALUES(DEFAULT, \'{}\',{}); ".format(form['opis'],form['kategoria'])
       
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'

def insert_lokalizacja(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "INSERT INTO magazyn.magazyn_lokalizacje VALUES({}, {}, \'{}\',\'{}\',\'{}\'); ".format(form['id_magazyn'],form['nr_magazynu'],form['ulica'],form['kod_pocztowy'],form['miasto'])
       
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'


def insert_kategoria(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "INSERT INTO magazyn.kategoria VALUES({}, \'{}\'); ".format(form['id_kategoria'],form['opis'])
       
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
