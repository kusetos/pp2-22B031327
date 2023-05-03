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
def csvFile():
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

def addName():
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

def changeData():
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

def tableInfo():
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
                print(row[0], "\t", row[1])



#pattern search
def patternSearch():
    while True:
        print("search by name or number. 'no' to leave ")
        name = input()
        #name = input()
        with open('allData.txt', 'r') as file:
            for line in file:
                if name in line:
                    print(line.strip())


#apdate txt data
def updateTXT():
    cursor.execute("""
            SELECT DISTINCT phone_number
            FROM users;
            """)

    cursor.execute("""SELECT * FROM users""")
    rows = cursor.fetchall()
    with open('allData.txt', 'w') as file:
        for row in rows:
            line = str(row) + '\n;'
            file.write(line)
    #file.close()

# 7.(2) INSERT name and phone / change phone if user exists
def insertUpdateData():
    print("write name and phone number... 'name num' ")
    name, number = input().split()
    cursor.execute(f"SELECT * FROM users WHERE first_name = '{name}'")
    exist = bool(cursor.rowcount)
    if exist:
        cursor.execute(f"UPDATE users SET phone_number = '{number}' WHERE first_name = '{name}'")
    else:
        cursor.execute(f"""INSERT INTO users (first_name, phone_number) VAlUES
            ('{name}', '{number}');""")

# 8 (3) insert users by list
def listInsert():
    listOfUsers = [["diker", "101"], ["doker", "202"], ["daker", "3o3"]]

    for usr in listOfUsers:
        try:
            usr[1] = int(usr[1])
            usr[1] = str(usr[1])
            cursor.execute(f"""INSERT INTO users (first_name, phone_number) VAlUES
                ('{str(usr[0])}', '{str(usr[1])}');""")
        except:
            print(f"mistake in phone number of {usr}")
    input()
#querrying 8 (4)
def querying():
    cursor.execute("""SELECT * FROM users
                    ORDER BY first_name
                    LIMIT 100 OFFSET 10""")
#9 (5)
def deleteInfo():
#DELETE DATA///////////
    while True:
        print("delete by: phone/name? 'no' to leave")
        out = input()
        if out == "no":
            break
        cursor.execute("""SELECT * FROM users""")
        result = cursor.fetchall()
        for row in result:
            print(row)
        if out == 'name':
            print("write user name...")
            name = input()
            cursor.execute(f"""DELETE FROM users WHERE first_name='{name}';""")
        elif out == 'phone':
            print('write user name...')
            phone = input()
            cursor.execute(f"DELETE FROM users WHERE phone_number=st'{phone}'")



while True:
    updateTXT()
    print("""hello what do you whant?
    1. add .csv file
    2. add User
    3. change some info
    4. delete user from name or phone (4)
    5. find user by pattern (1)
    6. view Users
    //7. insert by name and phone/ update phone (2)
    8. insert by list (3)
    9. function to querying data from the tables with pagination (4)
    """)
    out = input();
    if out == "1":
        csvFile()
    elif out == "2":
        addName()
    elif out == "3":
        changeData()
    elif out == "4":
        deleteInfo()
    elif out == '5':
        patternSearch()
    elif out == "6":
        tableInfo()
    elif out == '7':
        insertUpdateData()
    elif out == '8':
        listInsert()
    elif out == '9':
        querying()
    elif out == "stop":
        break
#asdad
n =20