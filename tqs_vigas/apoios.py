""" Programa para substituir o tipo de apoio das vigas
Tipos possíveis:
1 - Pilar que morre
2 - Viga
3 - Pilar que nasce com arranque
4 - Pilar que nasce sem arranque
5 - Pilar que passa
"""

from tkinter import filedialog as fd
import tkinter as tk
from tkinter import ttk, Button
from os import path, getcwd,chdir
from glob import glob
from sys import path as sys_path
sys_path.append(getcwd())
sys_path.append(getcwd() + "\\alv_tqs_revit")

def get_pav_folder():
    """Selecione a pasta do pavimento do TQS"""
    title = "Selecione a pasta do pavimento do projeto TQS"
    if path.exists(r'C:\TQS'):
        initialdir = r'C:\TQS'
    projeto = fd.askdirectory(mustexist=True,title=title,initialdir=initialdir)
    return path.normpath(projeto)

def combobox(pavimentos):
    root = tk.Tk()

    # config the root window
    root.geometry('200x120')
    root.resizable(False, False)
    root.title('Pavimento')

    # label
    label = ttk.Label(text="Selecione o pavimento a alterar:")
    label.pack(fill=tk.X, padx=5, pady=5)

    # create a combobox
    selected_pav = tk.StringVar()
    pav_cb = ttk.Combobox(root, textvariable=selected_pav)

    # get first 3 letters of every month name
    pav_cb['values'] = pavimentos

    # prevent typing a value
    pav_cb['state'] = 'readonly'

    # place the widget
    pav_cb.pack(fill=tk.X, padx=5, pady=5)

    # Button for closing
    exit_button = Button(root, text="Fechar", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

    return selected_pav.get()

def get_vigas(pavimento):
    pasta_vigas = path.join(pavimento, "VIGAS\\")
    print(pasta_vigas)
    vigas = []
    chdir(pasta_vigas)
    for file in glob("*.GEO"):
        vigas.append(file)
    return vigas

def muda_apoio(pavimento, vigas, tipo_from, tipo_to):
    """Muda o tipo de apoio da viga"""
    pasta_vigas = path.join(pavimento, "VIGAS\\")
    for viga in vigas:
        # Abre o arquivo
        arq = open(path.join(pasta_vigas,viga), "r+")
        # Le o arquivo
        texto = ''
        texto = arq.read().splitlines()
        # Encontra a linha (i) dos apoios
        loc_aux = 0
        i = 0
        for i,linha in enumerate(texto):
            # A segunda linha não vazia é a linha de apoios
            if linha[0] != " ": loc_aux += 1
            if loc_aux == 2: break
        # Extrai linha de apoios e substitui os textos na região delimitada
        linha_apoios = texto[i]
        linha_apoios_nova = linha_apoios[0:10].replace(tipo_from, tipo_to)+linha_apoios[10:]
        # Sobrescreve a linha de apoios no arquivo
        texto[i] = linha_apoios_nova
        # Busca o começo do arquivo e limpa
        arq.seek(0)
        arq.truncate(0)
        #Cria o texto novo e o escreve no arquivo
        texto_novo = '\n'.join(texto)
        arq.write(texto_novo)
        # Fecha o arquivo
        arq.close()

def main():
    pavimento = get_pav_folder()
    #pavimento = r'C:\TQS\CEA\Mississipi\CEA-Mississipi Concreto - Torre A e B - R02\Térreo'
    vigas = get_vigas(pavimento)
    tipo_from = '4'
    tipo_to = '1'
    muda_apoio(pavimento, vigas, tipo_from, tipo_to)

if __name__ == '__main__':
    main()