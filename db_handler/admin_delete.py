from magazyn_proj import settings
import psycopg2

def delete_pracownik_stanowisko(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query =  "DELETE FROM magazyn.pracownik_stanowisko WHERE id_stanowisko= \'{}\' ;".format(form['id_stanowisko'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()


def delete_pracownik(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "DELETE FROM magazyn.weryfikacja WHERE id_pracownik= \'{}\' ;".format(form['id_pracownik'])
    insert_query += "DELETE FROM magazyn.pracownik WHERE id_pracownik= \'{}\' ;".format(form['id_pracownik'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

