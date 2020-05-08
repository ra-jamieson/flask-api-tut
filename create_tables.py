import sqlite3

connection = sqlite3.connect('data-Sec6.sqlite')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text NOT NULL, password text NOT NULL)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text NOT NULL, price float NOT NULL)"
cursor.execute(create_table)

connection.commit()
connection.close()