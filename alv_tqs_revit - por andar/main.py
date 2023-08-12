from tkinter import filedialog as fd
from os import path, getcwd
from sys import path as sys_path
sys_path.append(getcwd())
import get_project_floors as gpf
import get_alv_blocks as gab
import brgt_files_handler as bfh
import get_openings as go
import get_wall_line as gwl
import get_openings_names as gon


def get_pav_folder():
    """Selecione uma pasta de pavimento de projeto TQS"""
    title = "Selecione a pasta de pavimento de projeto TQS"
    init_path = r"C:\TQS"
    if path.exists(init_path):
        initialdir = init_path
    pavimento = fd.askdirectory(mustexist=True,title=title,initialdir=initialdir)
    return path.normpath(path.normpath(pavimento))


def get_project_folder():
    """Selecione uma pasta de projeto TQS"""
    title = "Selecione a pasta do projeto TQS"
    if path.exists(r'C:\TQS'):
        initialdir = r'C:\TQS'
    projeto = fd.askdirectory(mustexist=True,title=title,initialdir=initialdir)
    return path.normpath(projeto)


def get_project_floors(projeto):
    return gpf.get_project_floors(projeto)


def main():
    # Parte que lê os blocos do DesFiad1.DWG:
    # Primeiro passo: Selecionar pasta de projeto
    pavimento = get_pav_folder()
    projeto = path.dirname(pavimento)
    projeto_nome = path.basename(projeto) #testar
    # Terceiro passo: Ler blocos de cada pavimento e escrever .atr
    print('Lendo pavimento %s' % pavimento)
    dwgPath1aF = path.join(pavimento, 'DesFiad1.DWG')
    dwgPath2aF = path.join(pavimento, 'DesFiad2.DWG')
    blocos1aF = gab.get_alv_blocks(dwgPath1aF)
    blocos2aF = gab.get_alv_blocks(dwgPath2aF)
    dwgPathMod = path.join(pavimento, path.basename(pavimento))
    myLines = gwl.get_wall_line(dwgPathMod)

    # Dar nomes pra cada abertura
    blocos1aF = gon.get_openings_names(blocos1aF,dwgPath1aF)

    bfh.write_blocks(projeto_nome,pavimento,blocos1aF,myLines,'1aF')
    bfh.write_blocks(projeto_nome,pavimento,blocos2aF,myLines,'2aF')

    # Quarto passo: Ler Portas e Janelas do projeto e escrever .atr
    portas, janelas = go.read_openings(projeto)
    bfh.write_openings(projeto_nome,portas,janelas)


if __name__ == "__main__":
    main()