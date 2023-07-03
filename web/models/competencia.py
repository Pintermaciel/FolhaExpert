import sqlite3

def showallrecordscompetencia():
    """
    Retorna uma lista com todos os registros de admissão do banco de dados.

    Returns:
        list: Lista contendo os registros de admissão.
    """
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT id, nome, setor, funcao, competencia FROM competencia ORDER BY id DESC")
        competencia = []
        for item in cursor.fetchall():
            competencia.append(item)
        return competencia
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg
