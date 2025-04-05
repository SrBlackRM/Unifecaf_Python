from dotenv import load_dotenv
import mysql.connector

load_dotenv()

import os

mydb = mysql.connector.connect(
    host = os.environ['DOMINIO'],
    user = os.environ['USUARIO'],
    password = os.environ['SENHA'],
    database = os.environ['DATABASE']
)

mycursor = mydb.cursor()