from magazyn_proj import settings
import psycopg2

from magazyn_proj import settings
import psycopg2
from db_handler import zam_order




def removal(id_magazynu,form,id_prac):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
        quantity=zam_order.get_product_quantity_in_magazyn(id_magazynu,form['produkt'])

        if quantity-form['ilosc']<0:
            cur.close()
            con.close()
            raise Exception("Date provided can't be in the past")
        else:
            nowa_ilosc=quantity-form['ilosc']
            print("lslsl")
            insert_query = "UPDATE magazyn.magazyn_stan SET ilosc = {} WHERE  id_produkt = {} AND id_magazyn = {}; ".format(nowa_ilosc,form['produkt'], id_magazynu)
            insert_query+="INSERT INTO magazyn.magazyn_operacje (id_produkt, ilosc,rodzaj_operacji, id_magazyn,id_pracownik) VALUES ({},{}, 'wyd', {},{}); ".format(form['produkt'],form['ilosc'],id_magazynu,id_prac)
            cur.execute(insert_query)
            con.commit()
            cur.close()
            con.close()
    except (Exception, psycopg2.Error) as error:
        
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
    