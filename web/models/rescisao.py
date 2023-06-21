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
        cursor.execute("SELECT * FROM rescisao")
        rescisao = []
        for item in cursor.fetchall():
            test = item[1]
            print(test)
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
