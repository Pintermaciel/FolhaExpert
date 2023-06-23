import sqlite3
import traceback

def showallrecords():
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM setor ORDER BY id DESC")
        setor = []
        for item in cursor.fetchall():
            setor.append(item)
        return setor
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_newsetor(empresa, setor, funcao, lider):
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")
        
        if empresa != "" and setor != "" and funcao != "" and lider != "":
            cursor.execute("INSERT INTO setor(empresa, setor, funcao, lider) VALUES(?,?,?,?)", (empresa,setor,funcao,lider))
            connect.commit()
            connect.close()
            msg = "sucess"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "falhou"
        return msg
    
def show_selectedSetor(id):
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
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedAdmissao")
        cursor.execute("SELECT * FROM setor WHERE id =?", (id,))
        editadmissao = []
        for item in cursor.fetchone():
            editadmissao.append(item)
        return editadmissao

    except Exception as error:
        print(error)
        msg = "falha"
        return msg
    
def update_setor(empresa, setor, funcao, lider, id):
    """
    Atualiza um registro de admissão existente no banco de dados.

    Args:
        empresa (str): Novo nome da empresa.
        setor (str): Novo setor do funcionário.
        funcao (str): Nova função do funcionário.
        lider (str): Novo líder do setor.
        id (int): ID do registro de admissão a ser atualizado.

    Returns:
        str: Mensagem de sucesso ou falha.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! update_setor")

        if empresa != "" and setor != "" and funcao != "" and lider != "":
            query = "UPDATE setor SET empresa=?, setor=?, funcao=?, lider=? WHERE id=?"
            params = (empresa, setor, funcao, lider, id)
            print("Comando SQL:", query)
            print("Parâmetros:", params)
            cursor.execute(query, params)
            connect.commit()
            connect.close()
            msg = "sucesso"
            print(msg)
            return msg
        else:
            msg = "falha"
            print(msg)
            return msg
    except Exception as error:
        print("Erro ao executar o SQL:")
        traceback.print_exc()
        msg = "falha"
        print(msg)
        return msg