#Adding new data into database 
#Mandatroy requirement Title / Author /Years

from db import get_connection
import mysql.connector

def close_connection(connection):
    if connection:
        connection.close()

def add_book():
    try:
        #Setting up user variable 
        title = input("Enter the name of data you want to insert:").strip()
        author = input("Enter the name of author:").strip()
        year_input = input("Enter the publish year: ").strip()

        if not year_input.isdigit():
            print("This must be number !!!")
            return

        published_year = int(year_input)

        #Connect to DB and insert data 
        connection = get_connection()
        cursor = connection.cursor()
        sql_query = "INSERT INTO books (title, author,  published_year) VALUES (%s, %s, %s)"
        cursor.execute(sql_query, (title,author, published_year))
        print("You successfully add the data")
        connection.commit()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error While Getting Data",error)

add_book()
