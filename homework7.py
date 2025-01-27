import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(db_name, product):
    sql = '''INSERT INTO products 
    (product_title , price , quantity)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_15_products():
    insert_product(db_name, ('молоко "Весёлый молочник"', 100, 5))
    insert_product(db_name, ('молоко "Простоквашино"', 120, 10))
    insert_product(db_name, ('молоко "Домик в деревне"', 110, 8))
    insert_product(db_name, ('молоко "Белый город"', 105, 6))
    insert_product(db_name, ('молоко "Тёмное утро"', 115, 7))
    insert_product(db_name, ('молоко "Киргизское"', 90, 15))

    insert_product(db_name, ('сыр "Российский"', 400, 3))
    insert_product(db_name, ('сыр "Голландский"', 450, 4))
    insert_product(db_name, ('сыр "Моцарелла"', 500, 2))
    insert_product(db_name, ('сыр "Пармезан"', 800, 1))

    insert_product(db_name, ('сметана "Простоквашино"', 150, 12))
    insert_product(db_name, ('сметана "Домик в деревне"', 160, 10))
    insert_product(db_name, ('сметана "Белый город"', 140, 8))
    insert_product(db_name, ('сметана "Деревенская"', 130, 5))
    insert_product(db_name, ('сметана "Киргизская"', 100, 20))

def update_quantity(db_name, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(db_name, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(db_name, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def print_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_with_filter(db_name, filter):
    sql = '''SELECT id, product_title, price, quantity FROM products WHERE price < ? AND quantity > ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, filter)
            rows = cursor.fetchall()
            if rows:
                print("Товары, удовлетворяющие условиям:")
                for row in rows:
                    print(row)
            else:
                print("Нет товаров, удовлетворяющих условиям.")
    except sqlite3.Error as e:
        print(e)

def select_by_name(db_name):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%молоко%' '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

db_name = '''hw.db'''
sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection(db_name)
if my_connection is not None:
    print('Connection established')
    create_table(my_connection, sql_to_create_products_table)
# insert_15_products()
# update_price(db_name, (200, 1))
# update_quantity(db_name, (7, 2))
# delete_product(db_name, 3)
# print_all_products(db_name)
# select_products_with_filter(db_name, (300, 5))
# select_by_name(db_name)