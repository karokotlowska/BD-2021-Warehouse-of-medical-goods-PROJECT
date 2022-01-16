from magazyn_proj import settings
import psycopg2



def update_pracownik(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "UPDATE magazyn.pracownik SET imie = \'{}\', email = \'{}\', nazwisko = \'{}\'  WHERE id_pracownik = {} ;".format(form['imie'],form['email'], form['nazwisko'],form['id_pracownik'], )
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

def update_pracownik_stanowisko(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "UPDATE magazyn.pracownik_stanowisko SET opis = \'{}\' WHERE id_stanowisko = \'{}\' ;".format(form['opis'],form['id_stanowisko'], )
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

def update_weryfikacja(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    update_query = "UPDATE magazyn.weryfikacja SET login = \'{}\' WHERE id_pracownik = {} ;".format(form['login'], form['id_pracownik'])
    update_query += "UPDATE magazyn.weryfikacja SET haslo = \'{}\' WHERE id_pracownik = {} ;".format(form['haslo'], form['id_pracownik'])
    cur.execute(update_query)
    con.commit()
    cur.close()
    con.close()

