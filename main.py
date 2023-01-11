print('Hello')

import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

# create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            nick_name varchar(50) NOT NULL);"""
        )
        print("[INFO] Table created successfully")

# insert data into a table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """INSERT INTO users (first_name, nick_name) VALUES
#             ('Bob', 'barracuda');"""
#         )
#         print("[INFO] Data was successfully inserted")

# get data from a table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """SELECT nick_name FROM users WHERE first_name = 'Bob';"""
#         )
#         print(cursor.fetchone())

# delete a table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """DROP TABLE users;"""
#         )
#         print("[INFO] Table was deleted")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")