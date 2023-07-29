import time
import pyautogui
import pandas as pd

# pyautogui.write
# pyautogui.press
# pyautogui.click
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.1


# Passo 3: Editar o txt

time.sleep(3)
pyautogui.click(x=108, y=148)  # linha 1
pyautogui.hotkey('shift', 'down')  # seleciona linha 1
pyautogui.hotkey('ctrl', 'c')
pyautogui.press("home")
pyautogui.hotkey('ctrl', 'v')  # duplica linha
pyautogui.hotkey('shift', 'down')  # seleciona linha 3
pyautogui.press("backspace")  # deleta linha 3 de cd
pyautogui.press("left")
pyautogui.press("up")
pyautogui.press("backspace")
pyautogui.press("backspace")
pyautogui.write("atus")  # altera 1º linha de stop para status
pyautogui.hotkey('ctrl', 's')  # salvar
