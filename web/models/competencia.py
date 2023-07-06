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

def save_newcomp(comp, dias, feriados):
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")

        if comp != "" and dias != "" and feriados != "":
            cursor.execute("INSERT INTO competencia (nome, setor, funcao, competencia, hn, he50, he65, he75, he100, faltadias, faltahora, diasuteis, feriados, cartao_acivale, unimed, desp_unimed, farmacia) SELECT COALESCE(nome, 0), COALESCE(setor, 0), COALESCE(cargo, 0), ?, 0, 0, 0, 0, 0, 0, 0, ?, ?, 0, 0, 0, 0 FROM admissao WHERE nome NOT IN (SELECT nome FROM rescisao);", (comp, dias, feriados))
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

def show_selectedCompetencia(id):
    """
    Retorna um registro de admissão específico com base no ID fornecido.

    Args:
        id (int): ID do registro de admissão.

    Returns:
        list: Lista contendo os detalhes do registro de admissão.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedCompetencia")
        cursor.execute("SELECT * FROM competencia WHERE id =?", (id,))
        editadmissao = []
        for item in cursor.fetchone():
            editadmissao.append(item)
        return editadmissao

    except Exception as error:
        print(error)
        msg = "falha"
        return msg
    
def show_deleteCompetencia(id):
    """
    Função que realiza a exclusão de um competencia no banco de dados.

    Args:
        id: O ID do competencia a ser excluído.

    Returns:
        str: Uma mensagem indicando o resultado da exclusão ("success" em caso de sucesso, "Error" em caso de erro).
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM competencia WHERE id =?", (id,))
        connect.commit()
        connect.close()
        msg = "success"
        return msg
    except Exception as error:
        print(error)
        msg = "Error"
        return msg

def show_selectedeleteCompetencia(id):
    """
    Função que retorna o ID de um competencia com base no ID fornecido.

    Args:
        id: O ID do competencia a ser selecionado.

    Returns:
        int or None: O ID do competencia encontrado ou None se o competencia não existir.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedeleteCompetencia")
        cursor.execute("SELECT * FROM competencia WHERE id =?", (id,))
        selected_setor = cursor.fetchone()
        if selected_setor:
            return selected_setor[0]  # Retornar apenas o ID
        else:
            return None
    except Exception as error:
        print(error)
        return None