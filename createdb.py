import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Cria a conexão com o database para SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            
if __name__ == '__main__':
    create_connection(r"C:\Users\Matheus\OneDrive\Área de Trabalho\FolhaExpert\startbootstrap-sb-admin-2-gh-pages\web\FolhaExpert\web\databases\storage.db")