#Testing Database 
#Print out mysql database version 

from db import get_connection
import mysql.connector

def close_connection(connection):
    if connection:
        connection.close()

def read_db_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are now connect to Mysql Version",db_version)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error While Getting Data",error)

print("Current Database version:")
read_db_version()

