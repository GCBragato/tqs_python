from sys import path as sys_path
from os import getcwd
sys_path.append(getcwd() + "\\alv_tqs_revit - por andar")
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
from tkinter import filedialog as fd
import project_folders as pf
import get_project_floors as gpf
import get_project_type as gpt


class App(object):
    def __init__(self, master, tqs_path, list_pavs):
        self.tqs_path = tqs_path
        self.list_pavs = list_pavs

        # Ícones
        self.img_folder = tk.PhotoImage(
            file='./tqs_browser/resources/TQS icons/folder.png',
            width=20,height=16)
        self.img_conc = tk.PhotoImage(
            file='./tqs_browser/resources/TQS icons/conc.png',
            width=20,height=16)
        self.img_alvest = tk.PhotoImage(
            file='./tqs_browser/resources/TQS icons/alv.png',
            width=20,height=16)
        self.img_preo = tk.PhotoImage(
            file='./tqs_browser/resources/TQS icons/preo.png',
            width=20,height=16)
        self.img_parcon = tk.PhotoImage(
            file='./tqs_browser/resources/TQS icons/parcon.png',
            width=20,height=16)
        self.img_pav = tk.PhotoImage(
            file='./tqs_browser/resources/TQS icons/pav.png',
            width=20,height=16)

        # Configuração da janela e posicionamento ao centro da tela
        #master.iconbitmap(r'C:\Backup\Icons\BRGT Icon.ico')
        master.title('Árvore de Edifícios TQS')
        win_width = 500
        win_height = 800
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        center_x = int((screen_width / 2) - (win_width / 2))
        center_y = int((screen_height / 2) - (win_height / 2))
        master.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
        master.resizable(False, False)
        master.attributes('-topmost', True)

        # frame_top
        frame_top = ttk.Frame(master)
        frame_top.columnconfigure(0, weight=1)
        frame_top.columnconfigure(0, weight=3)
        frame_top.columnconfigure(0, weight=1)
        frame_top.columnconfigure(0, weight=1)
        # Label 'Pasta Raiz'
        ttk.Label(frame_top,text='Pasta Raiz:').grid(row=0,column=0,sticky='w',
            pady=5)
        # Entry 'Caminho'
        self.tqs_path_entry = ttk.Entry(frame_top, width=35)
        self.tqs_path_entry.insert(0, self.tqs_path)
        self.tqs_path_entry.grid(row=0, column=1, sticky='w',padx=5,pady=5)
        self.tqs_path_entry.focus()
        # Button 'Atualizar'
        att_button = ttk.Button(frame_top,
            text='Atualizar',
            command=self.update_tree,
            width=10)
        att_button.grid(row=0, column=2, sticky='w',padx=3,pady=5)
        # Button 'Encontra Pasta'
        ff_button = ttk.Button(frame_top,
            text='Encontra Pasta',
            command=self.find_folder,
            width=14)
        ff_button.grid(row=0, column=3, sticky='w',pady=5)
        frame_top.pack()

        # Árvore de Edifícios
        tree_frame = ttk.Frame(master)
        self.tree = ttk.Treeview(tree_frame,show='tree',)
        #self.tree.grid(row=0, column=0, sticky='nsew',padx=5,pady=5)
        self.update_tree()
        ybar=tk.Scrollbar(tree_frame,orient=tk.VERTICAL,
            command=self.tree.yview)
        self.tree.configure(yscroll=ybar.set)
        self.tree.pack(side='left',fill='both',expand=True)
        ybar.pack(side=tk.RIGHT,fill=tk.Y)
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        tree_frame.pack(fill='both',expand=True,padx=5,pady=5)

        # frame_bottom
        frame_bottom = ttk.Frame(master)
        ttk.Label(frame_bottom,text='Projeto Selecionado:').pack(side='left',
            fill='x',expand=False)
        # Entry não editável de projeto selecionado
        self.selected_project_entry = ttk.Entry(frame_bottom, width=60)
        self.selected_project_entry.pack(side='right',fill='x',expand=True)
        self.selected_project_entry.config(state='disabled')
        frame_bottom.pack()

        # Botão Ok
        close_button = ttk.Button(master,text='Fechar',command=master.destroy,
            width=10)
        close_button.pack(side=tk.BOTTOM,padx=5,pady=5)
        
        # Variável de saída
        self.output = None


    def project_type(self,project):
        type = gpt.get_project_type(project)
        if type == 0:
            return self.img_conc
        elif type == 1:
            return self.img_preo
        elif type == 2:
            return self.img_alvest
        elif type == 3:
            return self.img_parcon
        return self.img_conc


    def list_tqs_pavs(self,projects):
        """Adiciona os pavimentos de cada projeto TQS na árvore"""
        # Lista todos os projetos TQS
        projects = pf.main(self.tqs_path)
        for project in projects:
            pavs = gpf.get_project_floors(project)
            # Adiciona os pavimentos ao projeto
            for pav in pavs:
                self.tree.insert(project,0,os.path.join(project,pav),
                text=pav,image=self.img_pav)


    def on_select(self,event):
        """Seleciona um projeto TQS"""
        try:
            self.selected_project_entry.config(state='normal')
            self.selected_project_entry.delete(0,tk.END)
            for selected_item in self.tree.selection():
                _selected_item = self.tree.item(selected_item)['text']
                _selected_item_name = os.path.basename(_selected_item)
                self.selected_project_entry.insert(0,_selected_item_name)
            self.selected_project_entry.config(state='disabled')
            self.output = self.tree.selection()[0]
        except IndexError:
            pass
        return


    def update_tree(self):
        """Atualiza a árvore de edifícios"""
        self.tqs_path = self.tqs_path_entry.get()
        self.tqs_path = os.path.normpath(self.tqs_path)
        list_pavs = self.list_pavs

        # Lista todos os projetos TQS
        projects = pf.main(self.tqs_path)
        
        # Limpa a árvore
        self.tree.delete(*self.tree.get_children())

        # Adiciona os projetos TQS na árvore
        # Insere a pasta raiz
        self.tree.insert('', 'end', iid=self.tqs_path, text=self.tqs_path,
            open=True)
        # Insere os projetos TQS
        path_depth = len(self.tqs_path.split(os.path.sep))
        for project in projects:
            project_split = project.split(os.path.sep)
            project_depth = len(project_split)
            for i in range(project_depth):
                if i < path_depth:
                    continue
                current_folder = '\\'
                current_folder = current_folder.join(project_split[:i])
                if self.tree.exists(current_folder):
                    continue
                else:
                    self.tree.insert(os.path.dirname(current_folder),
                    'end',
                    current_folder,
                    text=os.path.basename(current_folder),
                    image=self.img_folder)
            proj_image = self.project_type(project)
            self.tree.insert(os.path.dirname(project),'end',project,
                text=os.path.basename(project),image=proj_image)
        if list_pavs:
            self.list_tqs_pavs(projects)
        return


    def is_tqs_project(self,project):
        """Verifica se o projeto é um projeto TQS"""
        if os.path.exists(os.path.join(project,'EDIFICIO.BDE')):
            return True
        return False


    def find_folder(self):
        """Selecione uma pasta de projeto TQS"""
        title = "Selecione a pasta de projetos TQS"
        projeto = fd.askdirectory(mustexist=True,title=title,
            initialdir=self.tqs_path)
        projeto = os.path.normpath(projeto)
        self.tqs_path_entry.delete(0,tk.END)
        self.tqs_path_entry.insert(0, projeto)
        self.update_tree()
        return


def main(initialdir,list_pavs):
    if os.path.exists(r'C:\TQS'):
        initialdir = r'C:\TQS'
    else:
        initialdir = ''
    root = tk.Tk()
    app = App(root, tqs_path=initialdir,list_pavs=list_pavs)
    root.mainloop()
    return app.output


if __name__ == '__main__':
    main('',False)