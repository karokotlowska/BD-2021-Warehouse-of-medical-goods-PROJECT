from magazyn_proj import settings
import psycopg2

def insert_pracownik_stanowisko(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO magazyn.pracownik_stanowisko VALUES(\'{}\', \'{}\');".format(form['id_stanowisko'], form['opis'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()


def insert_pracownik(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO magazyn.pracownik VALUES(DEFAULT, \'{}\',\'{}\', \'{}\'); ".format(form['imie'],form['email'], form['nazwisko'], )
    insert_query += "INSERT INTO magazyn.weryfikacja (id_pracownik, login,haslo) VALUES((SELECT MAX(id_pracownik) FROM magazyn.pracownik),\'{}\', \'{}\');".format( form['login'], form['haslo'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

