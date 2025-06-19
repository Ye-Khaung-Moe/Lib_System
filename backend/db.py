#backend/db.py
#This is file directly indicate to database

import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost', database='web_library', user='root', password='LouisYe2000#')
    return connection