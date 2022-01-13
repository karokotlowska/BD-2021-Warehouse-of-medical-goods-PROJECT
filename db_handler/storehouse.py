from magazyn_proj import settings
import psycopg2

from magazyn_proj import settings
import psycopg2
from db_handler import zam_order




def removal(id_magazynu,ilosc,produkt,id_pracownik):
    try:
        con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        cur = con.cursor()
    
        quantity=zam_order.get_product_quantity_in_magazyn(id_magazynu,produkt)
        insert_query = "UPDATE magazyn.magazyn_stan SET ilosc = {} WHERE  id_produkt = {}; ".format(quantity-ilosc,produkt)
        insert_query+="INSERT INTO magazyn.magazyn_operacje (id_produkt,numer_kolejny_zamowienia,data_operacji, ilosc,rodzaj_operacji, id_magazyn,id_pracownik) VALUES ({},{},current_date,{}, 'wyd', {},{}); ".format(produkt,1,ilosc,id_magazynu,id_pracownik)

        cur.execute(insert_query)
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print ("Error while fetching data from PostgreSQL", error)
        return 'error'
    cur.close()
    con.close()