import sqlite3

def showallrecordsres():
    """
    Função que busca todos os registros na tabela de Rescisão no banco de dados e retorna uma lista com os resultados.

    Returns:
        list: Lista de registros de Rescisão.
    """
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM rescisao ORDER BY id DESC")
        rescisao = []
        for item in cursor.fetchall():
            rescisao.append(item)
        return rescisao
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_newres(nome, datares, liquidores, carteirares, motivo):
    """
    Função que salva um novo registro de Rescisão no banco de dados.

    Args:
        nome (str): Nome do funcionário.
        datares (str): Data de rescisão.
        liquidores (float): Valor líquido da rescisão.
        carteirares (str): Número da carteira de rescisão.
        motivo (str): Motivo da rescisão.

    Returns:
        str: Mensagem indicando o resultado da operação.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! save_newres")
        
        if nome != "" and datares != "" and liquidores != "" and carteirares != "" and motivo != "":
            cursor.execute("INSERT INTO rescisao(nome, datares, liquidores, carteirares, motivo) VALUES(?,?,?,?,?)", (nome,datares,liquidores,carteirares,motivo))
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
    
def show_selectedRescisao(id):
    """
    Função que busca um registro de Rescisão pelo ID no banco de dados e retorna os dados.

    Args:
        id (int): ID do registro de Rescisão.

    Returns:
        list: Lista contendo os dados do registro de Rescisão.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedRescisao")
        cursor.execute("SELECT * FROM rescisao WHERE id =?", (id,))
        editrescisao = []
        for item in cursor.fetchone():
            editrescisao.append(item)
        return editrescisao

    except Exception as Error:
        print(Error)
        msg = "falhou"
        return msg
    
def show_selectedNomeRescisao():
    """
    Retorna uma lista dos nomes distintos presentes na tabela "admissao".
    
    Returns:
        Uma lista contendo os nomes distintos encontrados na tabela.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedNomeRescisao")
        cursor.execute("SELECT DISTINCT nome FROM admissao")
        editadmissao = [item[0] for item in cursor.fetchall()]  # Obter todos os nomes retornados pela consulta
        return editadmissao
    except Exception as error:
        print(error)
        msg = "falha"
        return msg
    
def update_res(nomeedit, dataresedit, liquidoresedit, carteiraresedit, motivoedit, editid):
    """
    Função que atualiza um registro de Rescisão no banco de dados.

    Args:
        nomeedit (str): Novo nome do funcionário.
        dataresedit (str): Nova data de rescisão.
        liquidoresedit (float): Novo valor líquido da rescisão.
        carteiraresedit (str): Novo número da carteira de rescisão.
        motivoedit (str): Novo motivo da rescisão.
        editid (int): ID do registro de Rescisão a ser atualizado.

    Returns:
        str: Mensagem indicando o resultado da operação.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! update_res")

        if nomeedit != "" and dataresedit != "" and liquidoresedit != "" and carteiraresedit != "" and motivoedit != "":
            cursor.execute("UPDATE rescisao SET nome =?, datares =?, liquidores =?, carteirares =?, motivo =? WHERE id =?", (nomeedit, dataresedit, liquidoresedit, carteiraresedit, motivoedit, editid))
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

def show_deleteRescisao(id):
    """
    Função que realiza a exclusão de um rescisao no banco de dados.

    Args:
        id: O ID do rescisao a ser excluído.

    Returns:
        str: Uma mensagem indicando o resultado da exclusão ("success" em caso de sucesso, "Error" em caso de erro).
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM rescisao WHERE id =?", (id,))
        connect.commit()
        connect.close()
        msg = "success"
        return msg
    except Exception as error:
        print(error)
        msg = "Error"
        return msg

def show_selectedeleteRescisao(id):
    """
    Função que retorna o ID de um rescisao com base no ID fornecido.

    Args:
        id: O ID do rescisao a ser selecionado.

    Returns:
        int or None: O ID do rescisao encontrado ou None se o rescisao não existir.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedeleteRescisao")
        cursor.execute("SELECT * FROM rescisao WHERE id =?", (id,))
        selected_setor = cursor.fetchone()
        if selected_setor:
            return selected_setor[0]  # Retornar apenas o ID
        else:
            return None
    except Exception as error:
        print(error)
        return None