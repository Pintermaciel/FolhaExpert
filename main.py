import eel
import pyautogui


eel.init('web')

eel.start(
    'competencia.html',
    size = pyautogui.size(),
)
