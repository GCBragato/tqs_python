from os import path, getcwd, chdir, listdir
from sys import path as sys_path
sys_path.append(getcwd())
sys_path.append(getcwd() + "\\alv_tqs_revit")
sys_path.append(getcwd() + "\\tqs_browser")

import treeview_create as tc
from TQS import TQSDwg


def verifica(pavimento,tipo):
    if tipo == 'vigas':
        pasta = pavimento + r'\VIGAS'
    elif tipo == 'pilar':
        pasta = pavimento + r'\PILAR'
    arquivos = [f for f in listdir(pasta) if f.endswith('.DWG')]
    for arquivo in arquivos:
        caminho = path.join(pasta,arquivo)
        dwg = TQSDwg.Dwg()
        dwg.file.Open(caminho)
        if dwg.file.Open(caminho) != 0:
            print("Não abri o arquivo [%s] para leitura" % caminho)
        elif dwg.file.Open(caminho) == 0:
            print("Abri o arquivo [%s] para leitura" % caminho)
            pass
        dwg.globalrebar.firstMark = 1
        dwg.globalrebar.RenumerateMarks()
        dwg.file.Save()
        dwg.file.Close()
    return


def main ():
    pavimento = tc.main('',True)
    #pavimento = r'C:\TQS\VEGA\MAX CEM\VEGA Max CEM Concreto R01\Garagem'
    # Para vigas, selecionar o pavimento
    # Para pilar, selecionar o projeto
    verifica(pavimento,'vigas')


if __name__ == '__main__':
    main()