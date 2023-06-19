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
    
    if not empresa or not setor or not funcao or not lider:
        return "failure"

    msg = save_newsetor(empresa, setor, funcao, lider)

    if msg == "success":
        return "success"
    else:
        return "falhou"

eel.start(
    'competencia.html',
    size = pyautogui.size(),
)


