from base64 import *
import base64
import datetime
from mydatabase import conection

mydatabase = conection()

class register:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.register()
        self.token = ''
        self.new_username = ''
        self.new_password = ''
            
    def register(self):
        self.username = input("Username: ")
        self.password = input("Password: ")
        self.token = self.register_encoder()
        self.save_register(self.token)
        msg = "Successful Register!"
        print(msg)
        
    def register_encoder(self):
        self.new_username = base64.b64encode(self.username.encode('ascii'))    
        self.new_password = base64.b64encode(self.password.encode('ascii'))
        encoded_register = f"{self.new_username}%x%{self.new_password}%x%"
        del(self.username)
        del(self.password)
        return str(encoded_register)

    def save_register(self, token):
        logfile = open ("log.txt" , "a")
        logfile.write("---New Register!---" + "\n")
        logfile.write(token + str(datetime.datetime.now().isoformat(timespec='seconds')) + "\n")
        cursor = mydatabase.mydb.cursor()
        insert = f"""INSERT INTO registers(user, password, creation_time) VALUES("{self.new_username}", "{self.new_password}", "{str(datetime.datetime.now().isoformat(timespec='seconds'))}") """
        cursor.execute(insert)
        mydatabase.mydb.commit()
        logfile.close()
        cursor.close()

    # def decoder(self):
        # print(new_username)
        # print(decode.new_username)

new_user = register()
