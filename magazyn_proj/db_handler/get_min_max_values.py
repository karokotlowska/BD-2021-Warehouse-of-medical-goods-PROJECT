from magazyn_proj import settings
import psycopg2

def get_min_max_values():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cursor = con.cursor()
    columns = ["kwota"]
    min_max_data = {"kwota":[]}
    for column in columns:
        postgreSQL_select_Query_MAX = "SELECT MAX({}) FROM magazyn.zamowienie".format(column)
        postgreSQL_select_Query_MIN = "SELECT MIN({}) FROM magazyn.zamowienie".format(column)
        cursor.execute(postgreSQL_select_Query_MIN)
        mobile_records = cursor.fetchone()
        min_max_data[column].append(mobile_records[0])
        cursor.execute(postgreSQL_select_Query_MAX)
        mobile_records = cursor.fetchone()
        min_max_data[column].append(mobile_records[0])
    return min_max_data