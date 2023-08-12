import pyautogui as pyag
import activate_window as aw
import time
import sys
import os

# Checa se está sendo chamado por linha de comando
try:
    #print(sys.argv[1])
    tecla = sys.argv[1].lower()
except:
    tecla = 'g18'

# Define Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

def click_from_tudo(btn: str):
    """Opções de mover a partir de tudo:
    tudo = 0, 0
    subestrutura = 274, -14
    vertical = 299, -14
    dir_x = 371, -14
    dir_y = 426, -14
    cerca = 586, -14
    """

    #Localiza Tudo
    btn_tudo_loc = pyag.locateCenterOnScreen("images/tudo.png", confidence=0.9)

    #Clica em
    if btn == 'tudo':
        pyag.click(btn_tudo_loc[0]+0, btn_tudo_loc[1]+0)
    elif btn == 'subestrutura':
        pyag.click(btn_tudo_loc[0]+274, btn_tudo_loc[1]-14)
    elif btn == 'vertical':
        pyag.click(btn_tudo_loc[0]+299, btn_tudo_loc[1]-14)
    elif btn == 'dir_x':
        pyag.click(btn_tudo_loc[0]+371, btn_tudo_loc[1]-14)
    elif btn == 'dir_y':
        pyag.click(btn_tudo_loc[0]+426, btn_tudo_loc[1]-14)
    elif btn == 'cerca':
        pyag.click(btn_tudo_loc[0]+586, btn_tudo_loc[1]-14)


def click_from_combinacoes(btn: str):
    """Opções de mover a partir de combinações:
    combinacoes = 0,0
    dir_flex_alma = -182, 5
    curva_int = -182, 107
    verificar = 24, 109
    """

    #Localiza Combinações
    btn_comb_loc = pyag.locateCenterOnScreen("images/combinacoes.png", confidence=0.9)

    #Clica em
    if btn == 'combinacoes':
        pyag.click(btn_comb_loc[0]+0, btn_comb_loc[1]+0)
    elif btn == 'dir_flex_alma':
        pyag.click(btn_comb_loc[0]-182, btn_comb_loc[1]+5)
    elif btn == 'curva_int':
        pyag.click(btn_comb_loc[0]-182, btn_comb_loc[1]+107)
    elif btn == 'verificar':
        pyag.click(btn_comb_loc[0]+24, btn_comb_loc[1]+109)


def click_calcular():
    """Clica em calcular
    """

    #Localiza Calcular
    btn_calc_loc = pyag.locateCenterOnScreen("images/calcular.png", confidence=0.9)

    #Clica em
    pyag.click(btn_calc_loc[0]+0, btn_calc_loc[1]+0)


def click(btn: str):
    """Direciona o click para a função correta.

    tudo, subestrutura, vertical, dir_x, dir_y, cerca, combinacoes, dir_flex_alma, curva_int, verificar, calcular
    """

    if btn == 'tudo' or btn == 'subestrutura' or btn == 'vertical' or btn == 'dir_x' or btn == 'dir_y' or btn == 'cerca':
        click_from_tudo(btn)
    elif btn == 'combinacoes' or btn == 'dir_flex_alma' or btn == 'curva_int' or btn == 'verificar':
        click_from_combinacoes(btn)
    if btn == 'calcular':
        click_calcular()


def rotinas_click(rotina: str):
    if rotina == 'g4': # Vertical
        click('vertical')
    elif rotina == 'g5': # Dir X
        click('dir_x')
    elif rotina == 'g6': # Dir Y
        click('dir_y')
    elif rotina == 'g7': # Subestrutura Cima
        click('subestrutura')
        pyag.press('up')
        pyag.press('enter')
    elif rotina == 'g10': # Subestrutura Baixo
        click('subestrutura')
        pyag.press('down')
        pyag.press('enter')
    elif rotina == 'g8': # Cerca Cima
        click('cerca')
        pyag.press('up')
        pyag.press('enter')
    elif rotina == 'g11': # Cerca Baixo
        click('cerca')
        pyag.press('down')
        pyag.press('enter')
    elif rotina == 'g9': # Verificar tudo
        click('combinacoes')
        time.sleep(5)
        click('calcular')
        time.sleep(2)
        pyag.keyDown('alt')
        pyag.keyDown('f4')
        time.sleep(.1)
        pyag.keyUp('f4')
        pyag.keyUp('alt')
    elif rotina == 'g12': # Flexão na direção da alma
        click('dir_flex_alma')
    elif rotina == 'g18': # Subestrutura mais, Dir Y, Verifica All
        click('subestrutura')
        pyag.press('down')
        pyag.press('enter')
        click('dir_y')
        click('combinacoes')
        time.sleep(0.5)
        click('calcular')
        time.sleep(2)
        pyag.keyDown('alt')
        pyag.keyDown('f4')
        time.sleep(.1)
        pyag.keyUp('f4')
        pyag.keyUp('alt')


def main(tecla: str):
    try:
        w = aw.WindowMgr()
        w.find_window_wildcard("Verificação Gráfica")
        w.set_foreground()
    except:
        return

    time.sleep(0.5)
    rotinas_click(tecla)


if __name__ == '__main__':
    main(tecla)
