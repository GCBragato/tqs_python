from tkinter import filedialog as fd
from os import path
import get_project_floors as gpf
import get_alv_blocks as gab
import atr_handler as ah

def get_project_folder():
    """Selecione uma pasta de projeto TQS"""
    title = "Selecione a pasta do projeto TQS"
    if path.exists(r'C:\TQS'):
        initialdir = r'C:\TQS'
    projeto = fd.askdirectory(mustexist=True,title=title,initialdir=initialdir)
    print(projeto)
    return path.normpath(projeto)

def get_project_floors(projeto):
    return gpf.get_project_floors(projeto)

def main():
    # Primeiro passo: Selecionar pasta de projeto
    projeto = get_project_folder()
    # Segundo passo: Ler pavimentos do projeto
    pavimentos = get_project_floors(projeto)
    # Terceiro passo: Ler blocos de cada pavimento e escrever .atr
    for pavimento in pavimentos:
        dwgPath = path.join(projeto, pavimento, 'DesFiad1.DWG')
        blocos = gab.get_alv_blocks(dwgPath)
        projeto_nome = path.basename(projeto)
        ah.write_atr(projeto_nome,pavimento,blocos)

if __name__ == "__main__":
    main()