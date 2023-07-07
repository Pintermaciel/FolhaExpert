import traceback
import sqlite3

def showallrecordsdesc():
    """
    Retorna uma lista com todos os registros de horas do banco de dados.

    Returns:
        list: Lista contendo os registros de horas.
    """
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("""
                        SELECT  id,
                                nome,
                                valor_inss,
                                valor_irrf,
                                cafe,
                                marmita,
                                os,
                                multas,
                                pensao,
                                plantao,
                                deslocamento,
                                reb_desp_viagens,
                                outros_descontos,
                                outros_recebimentos,
                                valor_pag_deposito,
                                competencia 
                        FROM competencia 
                        ORDER BY id DESC;
                        """)
        competencia = []
        for item in cursor.fetchall():
            competencia.append(item)
        return competencia
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def show_selecteddesc(id):
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
    
def update_desc(editnome, editcompetencia, editcartaoacivale, editunimed, editdesp_unimed, editfarmacia, editid):
    try:
        if editnome != "" and editcompetencia != "" and editcartaoacivale != "" and editunimed != "" and editdesp_unimed != "" and editfarmacia != "":
            connect = sqlite3.connect("web/databases/storage.db")
            cursor = connect.cursor()
            print("Conexão com o banco de dados estabelecida com sucesso! update_horas")
            print(editnome, editcompetencia, editcartaoacivale, editunimed, editdesp_unimed, editfarmacia, editid)

            query = "UPDATE competencia SET nome=?, competencia=?, cartaoacivale=?, unimed=?, desp_unimed=?, farmacia=? WHERE id=?"
            params = (editnome, editcompetencia, editcartaoacivale, editunimed, editdesp_unimed, editfarmacia, editid)
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
