import sqlite3

db_name = "./db/pass.sq3"
db_path = "./db/"

conn = sqlite3.connect("pass.sq3")
cur = conn.cursor()


# Création de la table

def createtable():
    cur.execute("CREATE TABLE pass (id TEXT, login TEXT, pass TEXT)")

def testdata():
    i = 0
    while i<10:
        cur.execute("INSERT INTO pass(id, login, pass) VALUES(1, test, test2)")
        i += i
    conn.commit()

def readdata():
    cur.execute()

# createtable()
testdata()

