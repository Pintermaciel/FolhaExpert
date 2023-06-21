import eel
from web.models.setor import showallrecords, save_newsetor
from web.models.admissao import showallrecordsadm, save_newadm
from web.models.rescisao import showallrecordsres, save_newres, show_selectedRescisao, update_res
import pyautogui


eel.init('web')


"""   SETOR    """

#mostra a tabela
@eel.expose
def fetchalldata():
    select_reg = showallrecords()
    eel.action_out(select_reg)

#salva no banco de dados   
@eel.expose
def btn_save(empresa, setor, funcao, lider):
    print("Chamando a função btn_save")
    msg = save_newsetor(empresa, setor, funcao, lider)
    eel.save_returnsetor(str(msg))


"""   ADMISSAO   """

#mostra a tabela
@eel.expose
def fetchalldataadm():
    select_reg = showallrecordsadm()
    eel.action_outadm(select_reg)

#salva no banco de dados   
@eel.expose
def btn_saveadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm):
    print("Chamando a função btn_save")
    msg = save_newadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm)
    eel.save_returnadm(str(msg))


"""   RESCISAO   """

#mostra a tabela
@eel.expose
def fetchalldatares():
    select_reg = showallrecordsres()
    eel.action_outres(select_reg)
    
#salva no banco de dados
@eel.expose
def btn_saveres(nome, datares, liquidores, carteirares, motivo):
    print("Chamando a função btn_save")
    msg = save_newres(nome, datares, liquidores, carteirares, motivo)
    eel.save_returnres(str(msg))

#edita no banco de dados
@eel.expose
def get_rescisao(id):
    selected_rescisao = show_selectedRescisao(id)
    eel.action_editres(selected_rescisao)

@eel.expose
def btn_saveeditres(nomeedit, dataresedit, liquidoresedit, carteiraresedit, motivoedit, editid):
    print("Chamando a função btn_saveeditres")
    msg = update_res(nomeedit, dataresedit, liquidoresedit, carteiraresedit, motivoedit, editid)
    


"""   START   """

eel.start(
    'rescisao.html',
    size = pyautogui.size(),
)


