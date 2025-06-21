
import mysql.connector

#importo libreria os y dotenv para cargar las variables de entono . No olvidar cargar desde terminal pip install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv() # carga las variables de entorno desde el archivo .env

def conectar_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
