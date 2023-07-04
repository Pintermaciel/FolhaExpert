import sqlite3

def showallrecordshrs():
    """
    Retorna uma lista com todos os registros de horas do banco de dados.

    Returns:
        list: Lista contendo os registros de horas.
    """
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT id, nome, hn, he50, he65, he100, faltadias, faltahora, competencia FROM competencia ORDER BY id DESC")
        competencia = []
        for item in cursor.fetchall():
            competencia.append(item)
        return competencia
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def show_selectedhrs(id):
    """
    Retorna um registro de horas específico com base no ID fornecido.

    Args:
        id (int): ID do registro de horas.

    Returns:
        list: Lista contendo os detalhes do registro de horas.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedhoras")
        cursor.execute("SELECT * FROM competencia WHERE id =?", (id,))
        editadmissao = []
        for item in cursor.fetchone():
            editadmissao.append(item)
        return editadmissao

    except Exception as error:
        print(error)
        msg = "falha"
        return msg
    