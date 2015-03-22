import sqlite3

db_name = "./db/pass.sq3"
db_path = "./db/"


conn = sqlite3.connect("pass.sq3")
cur = conn.cursor()


# Création de la table

def createtable():
    cur.execute("CREATE TABLE pass (id INTEGER, login TEXT, pass TEXT)")

def testdata():
    i = 0
    while i<100:
        cur.execute("INSERT INTO pass(id,login,pass) VALUES(:i,'test3','test332')", {"i":i})
        i = i+1
    conn.commit()


def readdata():
    cur.execute("SELECT * FROM 'pass'")
    print(cur.fetchall())

# createtable()
testdata()
readdata()

cur.close()
conn.close()