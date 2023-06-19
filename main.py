import eel
from web.models.setor import showallrecords, save_newsetor
import pyautogui


eel.init('web')

@eel.expose
def fetchalldata():
    select_reg = showallrecords()
    eel.action_out(select_reg)
    
@eel.expose
def btn_save(empresa, setor, funcao, lider):
    print("Chamando a função btn_save")
    msg = save_newsetor(empresa, setor, funcao, lider)
    eel.save_returnsetor(str(msg))

eel.start(
    'setor.html',
    size = pyautogui.size(),
)


