import eel
from web.models.setor import showallrecords, save_newsetor
from web.models.admissao import showallrecordsadm, save_newadm
import pyautogui


eel.init('web')


"""   SETOR    """

@eel.expose
def fetchalldata():
    select_reg = showallrecords()
    eel.action_out(select_reg)
    
@eel.expose
def btn_save(empresa, setor, funcao, lider):
    print("Chamando a função btn_save")
    msg = save_newsetor(empresa, setor, funcao, lider)
    eel.save_returnsetor(str(msg))


"""   ADMISSAO   """

@eel.expose
def fetchalldataadm():
    select_reg = showallrecordsadm()
    eel.action_outadm(select_reg)
    
@eel.expose
def btn_saveadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm):
    print("Chamando a função btn_save")
    msg = save_newadm(nome, cpf, empresa, setor, cargo, salariof, salario, dataadm)
    eel.save_returnadm(str(msg))

eel.start(
    'setor.html',
    size = pyautogui.size(),
)


