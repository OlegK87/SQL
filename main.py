import psycopg2


def get_id_data():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id FROM clients;
        """)
        list_id = cur.fetchall()
        id_result = []
        for id_number in list_id:
            id_result.append(id_number[0])
    return id_result


def get_phones_data():
    with conn.cursor() as cur:
        cur.execute("""
            SELECT phone_number FROM phone_numbers;
        """)
        phones_list = cur.fetchall()
        phones_result = []
        for phone in phones_list:
            phones_result.append(phone[0])
    return phones_result


def create_db():
    with conn.cursor() as cur:
        cur.execute("""
                        CREATE TABLE IF NOT EXISTS clients(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(20) NOT NULL,
                        last_name VARCHAR(20) NOT NULL,
                        email VARCHAR(60) NOT NULL
                        );
                    """)

        cur.execute("""
                        CREATE TABLE IF NOT EXISTS phone_numbers(
                        id SERIAL PRIMARY KEY,
                        phone_number VARCHAR(11),
                        client_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE
                        );
                    """)
        conn.commit()


def add_client(first_name, last_rname, email):
    with conn.cursor() as cur:
        cur.execute("""SELECT email FROM clients;""")
        client_list = cur.fetchall()
        client_result = []
        for client in client_list:
            client_result.append(client[0])

        if email in client_result:
            print(f'Данный {email} уже есть в базе данных')
        else:
            cur.execute("""INSERT INTO clients (first_name, last_name, email)
                           VALUES (%s, %s, %s);
                        """, (first_name, last_rname, email))
        conn.commit()


def add_phone(phone_number, client_id):
    id_result = get_id_data()
    phones_result = get_phones_data()
    with conn.cursor() as cur:
        if client_id in id_result:

            if str(phone_number) in phones_result:
                print(f'Данный номер телефона {phone_number} уже есть в базе данных')
            else:
                cur.execute("""
                    INSERT INTO phone_numbers (phone_number, client_id)
                    VALUES (%s, %s);
                            """, (phone_number, client_id))
            conn.commit()

        else:
            print(f'Клиент с номером id {client_id} отсутствует в базе данных')


def change_phone(phone_number, client_id):
    phones_res = get_phones_data()
    with conn.cursor() as cur:
        if str(phone_number) in phones_res:
            print(f'Данный номер телефона - {phone_number} уже есть в базе данных')
        else:
            cur.execute("""
                UPDATE phone_numbers SET phone_number = %s 
                WHERE id = (
                SELECT id from phone_numbers
                WHERE client_id = %s 
                LIMIT 1);
                        """, (phone_number, client_id))
        conn.commit()


def change_client(client_id, first_name=None, last_name=None, email=None,
                phone_number=None):
    id_result = get_id_data()
    with conn.cursor() as cur:
        if client_id in id_result:
            if first_name is not None:
                cur.execute("""
                    UPDATE clients SET first_name = %s 
                    WHERE id = %s;
                            """, (first_name, client_id))
            if last_name is not None:
                cur.execute("""
                    UPDATE clients SET last_name = %s 
                    WHERE id = %s;
                            """, (last_name, client_id))
            if email is not None:
                cur.execute("""
                    UPDTAE clients SET email = %s 
                    WHERE id = %s;
                            """, (email, client_id))
            if phone_number is not None:
                change_phone(phone_number, client_id)
        else:
            print(f'Клиент с номером id {client_id} отсутствует в базе данных')

    conn.commit()


def delete_phone(phone_number):
    phones_result = get_phones_data()
    with conn.cursor() as cur:
        if str(phone_number) not in phones_result:
            print(f'Данный номер телефона - {phone_number} не зарегистирован в базе данных')
        else:
            phone_number = str(phone_number)
            cur.execute("""
                DELETE FROM phone_numbers WHERE phone_number = %s;
                        """, (phone_number,))
        conn.commit()


def delete_client(client_id):
    id_result = get_id_data()
    with conn.cursor() as cur:
        if client_id in id_result:
            cur.execute("""
                DELETE FROM clients WHERE id = %s;
                        """, (client_id,))
        else:
            print(f'Клиент с номером id {client_id} отсутствует в базе данных')


def find_client(first_name, last_name, email, phone_number=None):
    with conn.cursor() as cur:

        if phone_number is not None:
            phone_number = str(phone_number)
            cur.execute("""
                SELECT client_id FROM phone_numbers
                WHERE phone_number = %s;
                        """, (phone_number,))
            id_number = cur.fetchall()[0][0]
            print(f'Номер id клиента, с указанным Вами номером телефона: {id_number}')

        else:
            cur.execute("""
                SELECT id FROM clients 
                WHERE first_name = %s AND last_name = %s AND email = %s; 
                        """, (first_name, last_name, email))
            id_number = cur.fetchall()[0][0]
            print(f'Номер id клиента с данными, которые Вы указали: {id_number}')


if __name__ == "__main__":

    with psycopg2.connect(database="clients_db", user="postgres", password="Motocikl") as conn:
        with conn.cursor() as cur:
            cur.execute("""
                    DROP TABLE clients CASCADE;
                     """)
        create_db()
        add_client('Денис', 'Сидоров', 'dude@mail.ru')
        add_client('Евгений', 'Кочетов', 'evgen@mail.ru')
        add_phone(79150010305, 1)
        add_phone(79160020406, 2)
        change_phone(79110030507, 1)
        change_client(1, 'Александр', 'Дерюгин', phone_number=79160030608)
        delete_client(2)
        find_client('Александр', 'Дерюгин', 'dude@mail.ru')
        find_client('Александр', 'Дерюгин', 'dude@mail.ru', 79160030608)

    conn.close()