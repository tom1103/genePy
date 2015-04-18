import sqlite3
import os
import random

class Db(object):

    """Classe Db pour interraction avec BDD"""
    def __init__(self):
        self.db_path = './.db/'
        self.db_name = 'pass.sq3'
        self._createPath()
        self.conn = sqlite3.connect(self.db_path+self.db_name)
        self.cur = self.conn.cursor()
        self._createTable()

    def _createTable(self):
        """Creation de la table si non existante"""
        self.cur.execute("CREATE TABLE IF NOT EXISTS password(login TEXT, passw TEXT, note TEXT)")

    def _createPath(self):
        if os.path.isdir(self.db_path):
            pass
        else:
            os.makedirs(self.db_path, mode=0o777)

    def dataInsert(self, login, passw, note):
        """Insertion data : login, passw, note"""

        self.cur.execute("INSERT INTO password(login, passw, note) VALUES (:login, :passw, :note)", {"login": login, "passw": passw, "note": note})
        self.conn.commit()

    def readData(self):
        """Lecture de la table"""
        self.cur.execute("SELECT * FROM 'password'")
        return(self.cur.fetchall())

    def close(self):
        """Fermeture du curseur et de la connection"""
        self.cur.close()
        self.conn.close()

db = Db()
print(db.readData())
db.close()
