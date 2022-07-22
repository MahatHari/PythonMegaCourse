import psycopg2

# create table


def create_table():
    conn = psycopg2.connect(
        "dbname='pythons-postgres' user='postgres' password='test' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL) ")
    conn.commit()
    conn.close()

# insert into table


def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='pythons-postgres' user='postgres' password='test' host='localhost' port='5432' ")
    cur = conn.cursor()
    # sql injection prone
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

# create view


def view():
    conn = psycopg2.connect(
        "dbname='pythons-postgres' user='postgres' password='test' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

# update table


def update(quantity, price, item):
    conn = psycopg2.connect(
        "dbname='pythons-postgres' user='postgres' password='test' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",
                (quantity, price, item))
    conn.commit()
    conn.close()

# delete row from table


def delete(item):
    conn = psycopg2.connect(
        "dbname='pythons-postgres' user='postgres' password='test' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE  FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


create_table()
print(view())
update(12, 6.0, 'Coffee Cup')

delete("Beer Cup")
delete("Tea Cup")
print(view())
