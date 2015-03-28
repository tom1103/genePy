import sqlite3

db_name = "./.db/pass.sq3"


class Db(object):
    """Classe Db pour interraction avec BDD"""

    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self._createTable()

    def _createTable(self):
        """Creation de la table si non existante"""
        self.cur.execute("CREATE TABLE IF NOT EXISTS password(login TEXT, passw TEXT, note TEXT)")


    def dataInsert(self, login, passw, note):
        """Insertion data : login, passw, note"""
        self.cur.execute("INSERT INTO password(login, passw, note) VALUES(:login, :passw, :note)", {"login":login, "passw":passw, "note":note})
        self.conn.commit()

    def readData(self):
        """Lecture de la table"""
        self.cur.execute("SELECT * FROM 'password'")
        return(self.cur.fetchall())

    def close(self):
        """Fermeture du curseur et de la connection"""
        self.cur.close()
        self.conn.close()