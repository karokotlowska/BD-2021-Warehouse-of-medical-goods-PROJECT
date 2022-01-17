from magazyn_proj import settings
import psycopg2

def delete_pracownik_stanowisko(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query =  "DELETE FROM magazyn.pracownik_stanowisko WHERE id_stanowisko= \'{}\' ;".format(form['id_stanowisko'])
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
        return 1
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'


def delete_pracownik(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "DELETE FROM magazyn.weryfikacja WHERE id_pracownik= \'{}\' ;".format(form['id_pracownik'])
        insert_query += "DELETE FROM magazyn.pracownik WHERE id_pracownik= \'{}\' ;".format(form['id_pracownik'])
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
        return 1
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'

def delete_produkt(form):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        insert_query = "DELETE FROM magazyn.produkt WHERE id_produkt= \'{}\' ;".format(form['id_produkt'])
        cur.execute(insert_query)
        con.commit()
        cur.close()
        con.close()
        return 1
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'

