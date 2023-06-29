import sqlite3
import traceback

def showallrecordsadm():
    """
    Retorna uma lista com todos os registros de admissão do banco de dados.

    Returns:
        list: Lista contendo os registros de admissão.
    """
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM admissao ORDER BY id DESC")
        admissao = []
        for item in cursor.fetchall():
            admissao.append(item)
        return admissao
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_newadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm):
    """
    Insere um novo registro de admissão no banco de dados.

    Args:
        nome (str): Nome do funcionário.
        cpf (str): CPF do funcionário.
        empresa (str): Nome da empresa.
        setor (str): Setor do funcionário.
        cargo (str): Cargo do funcionário.
        salariof (str): Salário na folha de pagamento.
        salario (str): Salário do funcionário.
        dataadm (str): Data de admissão.

    Returns:
        str: Mensagem de sucesso ou falha.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso!")

        if nome != "" and cpf != "" and empresa != "" and setor != "" and cargo != "" and salariof != "" and salario != "" and dataadm != "":
            cursor.execute("INSERT INTO admissao(nome, cpf, empresa, setor, cargo, salario_folha, salario, data_admissao) VALUES(?,?,?,?,?,?,?,?)", (nome,cpf,empresa,setor,cargo,salariof,salario,dataadm))
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

def show_selectedAdmissao(id):
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
        cursor.execute("SELECT * FROM admissao WHERE id =?", (id,))
        editadmissao = []
        for item in cursor.fetchone():
            editadmissao.append(item)
        return editadmissao

    except Exception as error:
        print(error)
        msg = "falha"
        return msg


def show_selectedEmpAdmissao():
    """
    Retorna uma lista das empresas distintas presentes na tabela "setor".
    
    Returns:
        Uma lista contendo as empresas distintas.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedEmpAdmissao")
        cursor.execute("SELECT DISTINCT empresa FROM setor")
        editadmissao = [item[0] for item in cursor.fetchall()]  # Obter todas as empresas retornadas pela consulta
        return editadmissao
    except Exception as error:
        print(error)
        msg = "falha"
        return msg

def show_selectedSetorAdmissao(empresa):
    """
    Retorna uma lista dos setores distintos relacionados a uma determinada empresa.
    
    Args:
        empresa: A empresa para a qual se deseja obter os setores relacionados.
        
    Returns:
        Uma lista contendo os setores distintos relacionados à empresa.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedSetorAdmissao")
        cursor.execute("SELECT DISTINCT setor FROM setor where empresa = ?", (empresa,))
        editadmissao = [item[0] for item in cursor.fetchall()]  # Obter todas as empresas retornadas pela consulta
        return editadmissao
    except Exception as error:
        print(error)
        msg = "falha"
        return msg

def show_selectedCargoAdmissao(setor):
    """
    Retorna uma lista das funções/cargos distintos relacionados a um determinado setor.
    
    Args:
        setor: O setor para o qual se deseja obter as funções/cargos relacionados.
        
    Returns:
        Uma lista contendo as funções/cargos distintos relacionados ao setor.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedCargoAdmissao")
        cursor.execute("SELECT DISTINCT funcao FROM setor where setor = ?", (setor,))
        editadmissao = [item[0] for item in cursor.fetchall()]  # Obter todas as setor retornadas pela consulta
        return editadmissao
    except Exception as error:
        print(error)
        msg = "falha"
        return msg


def update_adm(nomeedit, cpfedit, empresaedit, setoredit, cargoedit, salariofedit, salarioedit, dataadmedit, editid):
    """
    Atualiza um registro de admissão existente no banco de dados.

    Args:
        nomeedit (str): Novo nome do funcionário.
        cpfedit (str): Novo CPF do funcionário.
        empresaedit (str): Novo nome da empresa.
        setoredit (str): Novo setor do funcionário.
        cargoedit (str): Novo cargo do funcionário.
        salariofedit (str): Novo salário na folha de pagamento.
        salarioedit (str): Novo salário do funcionário.
        dataadmedit (str): Nova data de admissão.
        editid (int): ID do registro de admissão a ser atualizado.

    Returns:
        str: Mensagem de sucesso ou falha.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! update_adm")
        print(nomeedit, cpfedit, empresaedit, setoredit, cargoedit, salariofedit, salarioedit, dataadmedit, editid)

        if nomeedit != "" and cpfedit != "" and empresaedit != "" and setoredit != "" and cargoedit != "" and salarioedit != "" and cargoedit != "" and salariofedit != "" and dataadmedit != "":
            query = "UPDATE admissao SET nome=?, cpf=?, empresa=?, setor=?, cargo=?, salario_folha=?, salario=?, data_admissao=? WHERE id=?"
            params = (nomeedit, cpfedit, empresaedit, setoredit, cargoedit, salariofedit, salarioedit, dataadmedit, editid)
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
    
def show_deleteAdmissao(id):
    """
    Função que realiza a exclusão de um admissao no banco de dados.

    Args:
        id: O ID do admissao a ser excluído.

    Returns:
        str: Uma mensagem indicando o resultado da exclusão ("success" em caso de sucesso, "Error" em caso de erro).
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM admissao WHERE id =?", (id,))
        connect.commit()
        connect.close()
        msg = "success"
        return msg
    except Exception as error:
        print(error)
        msg = "Error"
        return msg

def show_selectedeleteAdmissao(id):
    """
    Função que retorna o ID de um admissao com base no ID fornecido.

    Args:
        id: O ID do admissao a ser selecionado.

    Returns:
        int or None: O ID do admissao encontrado ou None se o admissao não existir.
    """
    try:
        connect = sqlite3.connect("web/databases/storage.db")
        cursor = connect.cursor()
        print("Conexão com o banco de dados estabelecida com sucesso! show_selectedeleteAdmissao")
        cursor.execute("SELECT * FROM admissao WHERE id =?", (id,))
        selected_setor = cursor.fetchone()
        if selected_setor:
            return selected_setor[0]  # Retornar apenas o ID
        else:
            return None
    except Exception as error:
        print(error)
        return None
