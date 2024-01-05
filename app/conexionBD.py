
#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host ="frenoux1.mysql.pythonanywhere-services.com",
        user ="frenoux1",
        passwd ="mica2013*",
        database = "frenoux1$leloir"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")
    

    
    
    