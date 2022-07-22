import sqlite3

# 1. connect to database
# 2. create a cursor object
# 3. write an sql query
# 4. commit changes to database
# 5. close connection


def create_table():
    # 1 connect to database
    conn = sqlite3.connect("lite.db")
    # 2. create a cursor object
    cur = conn.cursor()
    # 3. write an sql query
    query = "CREATE TABLE IF NOT EXISTS store(item Text, quantity INTEGER, price REAL)"
    cur.execute(query)
    # 4. commit changes, execute
    conn.commit()
    # 5. close connection
    conn.close()


create_table()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    # 4. commit changes, execute
    conn.commit()
    # 5. close connection
    conn.close()


#insert("Coffee Cup", 10, 5)


def view():
    # 1 connect to database
    conn = sqlite3.connect("lite.db")
    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close
    return rows


def delete(item):
    # 1 connect to database
    conn = sqlite3.connect("lite.db")
    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close


def update(quantity, price, item):
    # 1 connect to database
    conn = sqlite3.connect("lite.db")
    # 2. create a cursor object
    cur = conn.cursor()
    cur.execute("UPDATE  store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close


# update
update(5, 7.0, 'Coffee Cup')
# delete
#delete('Wine Glass')

print(view())
