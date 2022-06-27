from tkinter import filedialog as fd
from os import path, getcwd
from sys import path as sys_path
sys_path.append(getcwd())
import get_project_floors as gpf
import get_alv_blocks as gab
import brgt_files_handler as bfh
import get_openings as go

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
    projeto = get_project_folder()
    projeto_nome = path.basename(projeto)
    # Segundo passo: Ler pavimentos do projeto
    pavimentos = get_project_floors(projeto)
    # Terceiro passo: Ler blocos de cada pavimento e escrever .atr
    for pavimento in pavimentos:
        dwgPath = path.join(projeto, pavimento, 'DesFiad1.DWG')
        blocos = gab.get_alv_blocks(dwgPath)
        bfh.write_blocks(projeto_nome,pavimento,blocos)

    # Quarto passo: Ler Portas e Janelas do projeto e escrever .atr
    portas, janelas = go.read_openings(projeto)
    bfh.write_openings(projeto_nome,portas,janelas)

if __name__ == "__main__":
    main()