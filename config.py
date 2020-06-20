# -*- coding: utf-8 -*-
# Токен
token = '866512327:AAERXFoGjH1Y-MNCLKnIIIci3mshASXysE0'

import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "E9bujic888",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "database_note")

    cursor = connection.cursor() #через cursor происходит общение с базой
    # cursor.execute('SELECT * FROM note.users')
    # # for row in cursor:
    # #     print(row)
    # records = cursor.fetchall() #возвращает все строки
    print(connection.get_dsn_parameters(), "\n");
    cursor.execute('SELECT name, password FROM note.users')
    users = cursor.fetchall()

    # print(records)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    connection = psycopg2.connect(user="postgres",
                                  password="E9bujic888",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    # closing database connection.
    # if (connection):
    #     cursor.close()
    #     connection.close()
    #     print("PostgreSQL connection is closed")

