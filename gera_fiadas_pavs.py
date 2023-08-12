from os import path, getcwd, chdir, listdir, rename
from sys import path as sys_path
sys_path.append(getcwd())
sys_path.append(getcwd() + "\\tqs_browser")
sys_path.append(getcwd() + "\\alv_tqs_revit - por andar")


import treeview_create as tc
import get_project_floors as gpf
from tkinter.filedialog import askdirectory
from TQS import TQSDwg, TQSExec


def copia_fiada(projeto):
    nomes = gpf.get_project_floors(projeto)
    numeros = gpf.get_project_numbers(projeto)
    pasta = askdirectory(title='Selecione a pasta destino das Fiadas')

    # Para cada pavimento, converter TQS DWG para DXF e copiá-lo
    for nome in nomes:
        # DWG da Fôrma
        dwg_path = path.join(
            projeto,
            nome,'DesFiad1.DWG'
            )

        # Abre o DWG
        dwg = TQSDwg.Dwg()
        dwg.file.Open(dwg_path)
        if dwg.file.Open(dwg_path) != 0:
            print("Não abri o arquivo [%s] para leitura" % dwg_path)
        elif dwg.file.Open(dwg_path) == 0:
            print("Abri o arquivo [%s] para leitura" % dwg_path)
            pass

        # Salva o DWG como DXF nas pasta escolhida
        dwg.file.SaveAs(path.join(
            pasta,str(numeros[nomes.index(nome)])+' - '+nome+'.dxf'
            ))


def main():
    # Usar TreeView Create para pegar o projeto
    projeto = tc.main('',False)
    # Copia as fôrmas para pasta escolhida
    copia_fiada(projeto)


if __name__ == '__main__':
    main()