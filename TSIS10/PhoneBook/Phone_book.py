import psycopg2
from config import host, user, password, db_name
import json
import csv


connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
)
connection.autocommit = True
cursor = connection.cursor()

cursor.execute(
        "SELECT version();"
    )
print(f"Server version: {cursor.fetchone()}")

    #create table
    # with connection.cursor() as cursor:\\

#Design tables for PhoneBook.////////////////
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
        first_name varchar(50),
        phone_number varchar(20));"""
)
    #connection.commit()
print(f"[INFO] table created!!!")

#Implement two ways of inserting data into the PhoneBook./////
out = "yes"
while True:
    print("insert .csv file? yes/no")
    out = input()
    if out == "no":
        break
    with open('db_phones.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO users VALUES (%s,%s)", row)
while True:
    print("insert yaur phone and name? yes/no")
    out = input()
    if out == "no":
        break
    print("write your name: ")
    name = input()
    print("write your number: ")
    phone = input()
    cursor.execute(f"""INSERT INTO users (first_name, phone_number) VAlUES
('{name}', '{phone}');""")
    break
#Implement updating data in the table (change user first name or phone)//////
while True:
    print("change some data? yes/no")
    out = input()
    if out == "no":
        break
    print("change name or number: name/number")
    out = input()
    if out == "name":
        print("write phone number to change name: ")
        phone = input()
        print("write name of user:")
        name = input()
        cursor.execute(f"""UPDATE users
            SET first_name = '{name}'
            WHERE phone_number = '{phone}';""")
    else:
        print("write name to change number: ")
        phone = input()
        print("write phone number:")
        name = input()
        cursor.execute(f"""UPDATE users
            SET phone_number = '{name}'
            WHERE first_name = '{phone}';""")


#Querying data from the tables (with different filters)///////////
while True:
    print("show table? yes/no")
    out = input()
    if out == "no":
        break
    print("phones or names? phone/name/all")
    out = input()
    if out == "name":
        cursor.execute("""SELECT * FROM users""")
        result = cursor.fetchall()
        for row in result:
            print(row[0])
    if out == "phone":
        cursor.execute("""SELECT * FROM users""")
        result = cursor.fetchall()
        for row in result:
            print(row[1])
    if out == "all":
        cursor.execute("""SELECT * FROM users""")
        result = cursor.fetchall()
        for row in result:
            print(row[0], "phone -", row[1])


#DELETE DATA//////////////

while True:
    print("delete more users? yes/no")
    if input() == "no":
        break
    cursor.execute("""SELECT * FROM users""")
    result = cursor.fetchall()
    for row in result:
        print(row[0])
    print("write user name?")
    name = input()
    cursor.execute(f"""DELETE FROM users WHERE first_name='{name}';""")