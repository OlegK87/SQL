import psycopg2

def create_db(conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        email VARCHAR(60) NOT NULL,
        phones VARCHAR(60) 
    );
    """)
def add_client(conn, first_name, last_name, email, phones=None):
    cur.execute("""
        INSERT INTO clients(first_name, last_name, email) VALUES(%s, %s, %s);
        """, (first_name[i], last_name[i], email[i]))
    cur.execute("""
        SELECT last_name FROM clients;
            """)
    print(cur.fetchall())
    cur.execute("""
        SELECT * FROM clients;
           """)
    print('fetchall', cur.fetchall())

def add_phone(conn, client_id, phone):
    cur.execute("""
         UPDATE clients SET phones=%s WHERE id=%s;
         """, (phone, client_id))
    cur.execute("""
        SELECT * FROM clients;
             """)
    print(cur.fetchall())


def change_client1(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    cur.execute("""
         UPDATE clients SET first_name=%s WHERE id=%s;
         """, (first_name, client_id))
    cur.execute("""
         SELECT * FROM clients;
                """)
    print(cur.fetchall())
def change_client2(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    cur.execute("""
          UPDATE clients SET last_name=%s WHERE id=%s;
          """, (last_name, client_id))
    cur.execute("""
          SELECT * FROM clients;
                 """)
    print(cur.fetchall())
def change_client3(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    cur.execute("""
          UPDATE clients SET email=%s WHERE id=%s;
          """, (email, client_id))
    cur.execute("""
          SELECT * FROM clients;
                """)
    print(cur.fetchall())
def change_client4(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    cur.execute("""
          UPDATE clients SET phones=%s WHERE id=%s;
          """, (phones, client_id))
    cur.execute("""
          SELECT * FROM clients;
                 """)
    print(cur.fetchall())
def delete_phone(conn, client_id, phones):
    cur.execute("""
              UPDATE clients SET phones=%s WHERE id=%s;
              """, (phones, client_id))
    cur.execute("""
              SELECT * FROM clients;
                     """)
    print(cur.fetchall())

def delete_client(conn, client_id):
    cur.execute("""
        DELETE FROM clients WHERE id=%s;
             """, (client_id,))
    cur.execute("""
        SELECT * FROM clients;
            """)
    print(cur.fetchall())

def find_client1(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
        SELECT * FROM clients WHERE first_name=%s;
             """, (first_name,))
    print(cur.fetchall())
def find_client2(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
        SELECT * FROM clients WHERE last_name=%s;
             """, (last_name,))
    print(cur.fetchall())
def find_client3(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
        SELECT * FROM clients WHERE email=%s;
             """, (email,))
    print(cur.fetchall())
def find_client4(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
        SELECT * FROM clients WHERE phone=%s;
             """, (phone,))
    print(cur.fetchall())

with psycopg2.connect(database="clients_db", user="postgres", password=" ") as conn:
    with conn.cursor() as cur:
        cur.execute("""
                DROP TABLE clients;
                """)
        create_db(conn)
        first_name = []
        last_name = []
        email = []
        for i in range(int(input("Введите количество клиентов: "))):
            first_name.append(input("Введите имя клиента: "))
            last_name.append(input("Введите фамилию клиента: "))
            email.append(input("Введите email клиента: "))
            add_client(conn, first_name=first_name, last_name=last_name, email=email, phones=None)
        add_phone_question = input("Вы хотите  добавить номера телефонов клиентов? Введите: ДА/НЕТ ").upper()
        if add_phone_question == "ДА":
            for j in range(int(input("Введите количество клиентов, для которых Вы хотите указать номера телефонов: "))):
                phone = []
                client_id = int(input("Введите номер id клиента: "))
                for i in range(int(input("Введите количество телефонных номеров для данного клиента: "))):
                    phone.append(input("Введите номер телефона: "))
                add_phone(conn, client_id=client_id, phone=phone)
                print("Телефонные номера клиента успешно добавлены")
        elif add_phone_question == "НЕТ":
            print("Хорошо, номер телефона не будем указывать")
        change_client_question = input("Вы хотите изменить данные клиента? Ввведите: ДА/НЕТ ").upper()
        if change_client_question == "ДА":
            change_client_question1 = input("Вы хотите изменить имя клиента? Введите: ДА/НЕТ ").upper()
            if change_client_question1 == "ДА":
                for j in range(int(input("Введите количество клиентов, у которых Вы хотите изменить имя: "))):
                    client_id = int(input("Введите номер id клиента: "))
                    first_name = input("Введите новое имя клиента: ")
                    change_client1(conn, client_id, first_name=first_name)
                    print("Изменения в имена клиентов внесены")
            elif change_client_question1 == "НЕТ":
                print("Хорошо, имена клиентов менять не будем")
            change_client_question2 = input("Вы хотите изменить фамилию клиента? Введите: ДА/НЕТ ").upper()
            if change_client_question2 == "ДА":
                for j in range(int(input("Введите количество клиентов, у которых Вы хотите изменить фамилию: "))):
                    client_id = int(input("Введите номер id клиента: "))
                    last_name = input("Введите новую фамилию клиента: ")
                    change_client2(conn, client_id, last_name=last_name)
                    print("Изменения в фамилии клиентов внесены")
            elif change_client_question2 == "НЕТ":
                 print("Хорошо, фамилии клиентов менять не будем")
            change_client_question3 = input("Вы хотите изменить email клиента? Введите: ДА/НЕТ ").upper()
            if change_client_question3 == "ДА":
                for j in range(int(input("Введите количество клиентов, у которых Вы хотите изменить email: "))):
                    client_id = int(input("Введите номер id клиента: "))
                    email = input("Введите новый email клиента: ")
                    change_client3(conn, client_id, email=email)
                    print("Изменения в email клиентов внесены")
            elif change_client_question3 == "НЕТ":
                print("Хорошо, email клиентов менять не будем")
            change_client_question4 = input("Вы хотите изменить телефонные номера клиентов? Введите: ДА/НЕТ ").upper()
            if change_client_question4 == "ДА":
                for j in range(int(input("Введите количество клиентов, которым Вы хотите изменить телефонные номера: "))):
                    phones = []
                    client_id = int(input("Введите номер id клиента: "))
                    for i in range(int(input("Введите количество телефонных номеров для данного клиента: "))):
                        phones.append(input("Введите номер телефона: "))
                    change_client4(conn, client_id, phones=phones)
                print("Телефонные номера клиентов успешно обновлены")
            elif change_client_question4 == "НЕТ":
                print("Хорошо, номера телефонов клиентов менять не будем")
            delete_phone_question = input("Вы хотите удалить номера телефонов клиента? Введите: ДА/НЕТ ").upper()
            if delete_phone_question == "ДА":
                for j in range(int(input("Введите количество клиентов, у которых Вы хотите удалить номера телефонов: "))):
                    client_id = int(input("Введите номер id клиента: "))
                    phones = 'Null'
                    delete_phone(conn, client_id, phones=phones)
                    print("Изменения в номера телефонов клиентов внесены")
            elif delete_phone_question == "НЕТ":
                print("Хорошо, номера телефонов клиентов удалять не будем")
            delete_client_question = input("Вы хотите удалить клиента из базы? Введите: ДА/НЕТ ").upper()
            if delete_client_question == "ДА":
                for j in range(int(input("Введите количество клиентов, которых Вы хотите удалить из базы: "))):
                    client_id = int(input("Введите номер id клиента, которого Вы хотите удалить: "))
                    delete_client(conn, client_id)
                    print("Изменения в базу клиентов внесены")
            elif delete_client_question == "НЕТ":
                print("Хорошо, клиентов удалять не будем")
        elif change_client_question == "НЕТ":
            print("Хорошо, данные клиентов менять не будем")
        find_client_question = input("Вы хотите найти клиента в базе? Введите: ДА/НЕТ ").upper()
        if find_client_question == "ДА":
            for j in range(int(input("Введите количество клиентов, которых Вы хотите найти в базе: "))):
                find_client_question1 = input("Как будем искать клиента? Введите: 'Имя'/'Фамилия'/'email'/'телефонный номер': ")
                if find_client_question1 == "Имя":
                    first_name = input("Введите имя клиента, которого Вы хотите найти: ")
                    find_client1(conn, first_name=first_name)
                    print("Данные по клиенту найдены")
                elif find_client_question1 == "Фамилия":
                    last_name = input("Введите фамилию клиента, которого Вы хотите найти: ")
                    find_client2(conn, last_name=last_name)
                    print("Данные по клиенту найдены")
                elif find_client_question1 == "email":
                    email = input("Введите email клиента, которого Вы хотите найти: ")
                    find_client3(conn, email=email)
                    print("Данные по клиенту найдены")
                elif find_client_question1 == "телефонный номер":
                    phone = input("Введите телефонный номер клиента, которого Вы хотите найти: ")
                    find_client4(conn, phone=phone)
                    print("Данные по клиенту найдены")
        elif find_client_question == "НЕТ":
            print("Хорошо, клиентов искать не будем")
conn.close()


