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

def save_newcomp(comp):
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")

        if comp != "":
            cursor.execute("INSERT INTO competencia (nome, setor, funcao, competencia, hn, he50, he65, he75, he100, faltadias, faltahora) SELECT COALESCE(nome, 0), COALESCE(setor, 0), COALESCE(cargo, 0), ?, 0, 0, 0, 0, 0, 0, 0 FROM admissao WHERE nome NOT IN (SELECT nome FROM rescisao);", (comp,))
            connect.commit()
            connect.close()
            msg = "sucesso"
            return msg
        else:
            msg = "falha"
            return msg
    except Exception as error:
        print(error)
        msg = "falha"
        return msg
