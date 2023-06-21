import sqlite3

def showallrecordsres():
    try:
        connect = sqlite3.connect(r"web/databases/storage.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM rescisao")
        recisao = []
        for item in cursor.fetchall():
            test = item[1]
            print(test)
            recisao.append(item)
        return recisao
    except Exception as error:
        print(error)
        msg = "Erro"
        return msg

def save_newres(nome, datares, liquidores, carteirares, motivo):
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