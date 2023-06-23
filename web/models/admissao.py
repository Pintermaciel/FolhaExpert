import sqlite3
import traceback

def show_all_records_adm():
    """
    Retorna uma lista com todos os registros de admissão do banco de dados.

    Returns:
        list: Lista contendo os registros de admissão.
    """
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM admissao")
        admissao = []
        for item in cursor.fetchall():
            admissao.append(item)
        return admissao
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_new_adm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm):
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

def show_selected_admissao(id):
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
