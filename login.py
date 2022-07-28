import datetime
from mydatabase import conection
import getpass
import base64

class login:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.get_login_acess()
        self.token = ''

    def get_login_acess(self):
        self.username = input("Username: ")
        self.password = getpass.getpass('Password: ')
        self.decoder()

    def decoder(self):
        self.username = base64.b64encode(self.username.encode('ascii'))    
        self.password = base64.b64encode(self.password.encode('ascii'))
        self.token = f"{self.username}%x%{self.password}%x%"
        self.validation()

    def validation(self):
        mydatabase = conection()
        cursor = mydatabase.mydb.cursor()
        cursor.execute(f"""SELECT * FROM `registers` WHERE user = "{self.username}" AND password = "{self.password}" """)
        result = cursor.fetchall()
        # print(result)
        if result:
            msg = "Successful Login!"
            print(msg)
            self.sucess_login()   
        else:
            print("User or Password Incorrect!")
        cursor.close()        

    def sucess_login(self):
        logfile = open ("log.txt" , "a")
        logfile.write("---New Session!---" + "\n")
        logfile.write(self.token + str(datetime.datetime.now().isoformat(timespec='seconds')) + "\n")
        logfile.close()
    
    def login_by_token(self, token):
        token = ''

new_session = login()