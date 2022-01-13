from magazyn_proj import settings
import psycopg2

class User:
    def __init__(self):
        self.connection = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
        self.is_admin=False
        self.is_mag=False
        self.is_zam=False
        self.is_superUser=False
       

    def __del__(self):
        self.connection.close()

    def check_user_password(self,user_record,password):
        if  password==user_record[1]:
            return [True,'Autoryzacja pomyslna !']
        else:
            return [False,'Zle haslo !']

    def check_user_role(self,user_record):
        cursor = self.connection.cursor()
        get_user_query = "SELECT id_stanowisko FROM magazyn.pracownik_role WHERE id_pracownik = \'{}\'".format(user_record[0])
        cursor.execute(get_user_query)
        user_role = cursor.fetchone() 
        cursor.close()
        print(user_role)
        return user_role
    


    def login(self,login_data):
        cursor = self.connection.cursor()
        get_user_query = "SELECT id_pracownik,login,haslo FROM magazyn.weryfikacja WHERE login = \'{}\'".format(login_data['login'])
        cursor.execute(get_user_query)
        
        user_record = cursor.fetchone() 
        if user_record is None:
            login_status = [False,'Nie ma takiego uzytkownika !']
        else:
            login_status = self.check_user_password(user_record,login_data['password'])
            user_type=self.check_user_role(user_record)   
            self.check_menu(user_type)
            login_status=[True, user_type[0]]
        cursor.close()
        print(login_status)
        return login_status

    def get_staff_id(self,login_data):
        cursor = self.connection.cursor()
        get_staff_member_id_query = "SELECT id_pracownik FROM magazyn.weryfikacja WHERE login = \'{}\'".format(login_data['login'])
        cursor.execute(get_staff_member_id_query)
        staff_member_record = cursor.fetchone() 
        cursor.close()
        return staff_member_record[0]

    def check_menu(self, usertype):
        if usertype[0]=='adm':
            self.is_admin=True
            print(usertype[0],self.is_admin)
        if usertype=='mag':
            self.is_mag=True


        
