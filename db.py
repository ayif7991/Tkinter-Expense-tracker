import  sqlite3
import datetime
now = datetime.datetime.utcnow()

CREATE_GROCERIES = "CREATE TABLE IF NOT EXISTS groceries(id INTEGER PRIMARY KEY, item text, price float, date DATE);"
CREATE_HOUSEHOLD = "CREATE TABLE IF NOT EXISTS household(id INTEGER PRIMARY KEY, item text, price float, date DATE);"
CREATE_ENTERTAINMENT = ("CREATE TABLE IF NOT EXISTS entertainment(id INTEGER PRIMARY KEY, item text, price float, "
                        "date DATE);")
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other(id INTEGER PRIMARY KEY, Item text, price float, date DATE);"

INSERT_GROCERIES = "INSERT INTO groceries(item,price,date) VALUES(?,?,?);"
INSERT_HOUSEHOLD = "INSERT INTO household(item,price,date) VALUES(?,?,?);"
INSERT_ENTERTAINMENT = "INSERT INTO entertainment(item,price,date) VALUES(?,?,?);"
INSERT_OTHER = "INSERT INTO other(item,price,date) VALUES(?,?,?);"

SELECT_ALL1 = "SELECT * FROM groceries;"
SELECT_ALL2 = "SELECT * FROM household;"
SELECT_ALL3 = "SELECT * FROM entertainment;"
SELECT_ALL4 = "SELECT * FROM other;"

SELECT_GROCERIES = "SELECT * FROM groceries WHERE item = ? AND price = ?;"
SELECT_HOUSEHOLD = "SELECT * FROM household WHERE item = ? AND price = ?;"
SELECT_ENTERTAINMENT = "SELECT * FROM entertainment WHERE item = ? AND price = ?;"
SELECT_OTHER = "SELECT * FROM other WHERE item = ? AND price = ?;"

DELETE_GROCERIES = "DELETE FROM groceries WHERE item = ? AND price = ?;"
DELETE_HOUSEHOLD = "DELETE FROM household WHERE item = ? AND price = ?;"
DELETE_ENTERTAINMENT = "DELETE FROM entertainment WHERE item = ? AND price = ?;"
DELETE_OTHER = "DELETE FROM other WHERE item = ? AND price = ?;"


list_db = [CREATE_GROCERIES,CREATE_HOUSEHOLD,CREATE_ENTERTAINMENT,CREATE_OTHER]

def create_tables():
    conn = sqlite3.connect("data.db")
    with conn:
        for db in list_db:
            conn.execute(db)

def insert_groceries(item,price,date):
    conn = sqlite3.connect("data.db")
    with conn:
        c = conn.cursor()
        conn.execute(INSERT_GROCERIES,(item,price,date))
        conn.commit()

def insert_household(item, price, date):
    conn = sqlite3.connect("data.db")
    with conn:
        c = conn.cursor()
        conn.execute(INSERT_HOUSEHOLD, (item, price, date))
        conn.commit()
def insert_entertainment(item,price,date):
    conn = sqlite3.connect("data.db")
    with conn:
        c = conn.cursor()
        conn.execute(INSERT_ENTERTAINMENT,(item,price,date))
        conn.commit()

def insert_other(item, price, date):
    conn = sqlite3.connect("data.db")
    with conn:
        c = conn.cursor()
        conn.execute(INSERT_OTHER, (item, price, date))
        conn.commit()

def select_all_groceries():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)

        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output

def select_all_household():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL2)

        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output
def select_all_entertainment():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL3)

        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output

def select_all_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)

        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output

def select_groceries():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_GROCERIES)

        list = c.fetchone()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output
def select_household():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_HOUSEHOLD)

        list = c.fetchone()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output
def select_entertainment():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ENTERTAINMENT)

        list = c.fetchone()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output

def select_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_OTHER)

        list = c.fetchone()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + '' + str(x[2]) + str(x[3]) + '\n'
        return output
def delete_grocery(item, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_GROCERIES, (item, price))
        conn.commit()
        c.close()

def delete_household(item, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_HOUSEHOLD, (item, price))
        conn.commit()
        c.close()

def delete_entertainment(item, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ENTERTAINMENT, (item, price))
        conn.commit()
        c.close()

def delete_other(item, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_OTHER, (item, price))
        conn.commit()
        c.close()

# create_tables()
