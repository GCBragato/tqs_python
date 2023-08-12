from os import path, getcwd, chdir, listdir, rename
from sys import path as sys_path
sys_path.append(getcwd())
sys_path.append(getcwd() + "\\tqs_browser")

import treeview_create as tc
import get_project_floors as gpf
from tkinter.filedialog import askdirectory
from TQS import TQSDwg


def renomear_formas(projeto,nomes,numeros,pasta):
    # Dados do projeto
    arquivos = [path.join(pasta,'FOR'+str.zfill(str(num),4)) for num in numeros]

    #rename arquivos to nomes
    i = 1
    for arquivo, nome in zip(arquivos,nomes):
        try:
            nome_from = arquivo+'.DXF'
            nome_to = path.join(pasta,str(i)+' - '+nome)+'.DXF'
            print('Renomeando arquivo',nome_from,'para',nome_to)
            rename(nome_from,nome_to)
        except:
            print('ERRO')
            print('Falha ao renomear arquivo',nome_from)
        i += 1


def main():
    projeto = tc.main('',False)
    nomes = gpf.get_project_floors(projeto)
    numeros = gpf.get_project_numbers(projeto)
    pasta = askdirectory(title='Selecione a pasta com os arquivos .DXF')
    renomear_formas(projeto,nomes,numeros,pasta)


if __name__ == '__main__':
    main()
