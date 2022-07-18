
from TQS import TQSUtil, TQSDwg, TQSJan, TQSEag
import tkinter as tk
from tkinter import ttk

class App(object):
    def __init__(self, master):

        # Configuração da Janela
        master.iconbitmap('C:/TQSW/EXEC/PYTHON/resources/BRGT Icon.ico')
        master.title('Ferro Vertical')
        win_width = 240
        win_height = 65
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        center_x = int((screen_width / 2) - (win_width / 2))
        center_y = int((screen_height / 2) - (win_height / 2))
        master.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
        master.resizable(False, False)
        master.attributes('-topmost', True)

        # Configuração do DropDown de armaduras


        # Configuração da Frame que contém o DropDown de armaduras
        frame_arm = ttk.Frame(master)
        frame_arm.columnconfigure(0)
        frame_arm.columnconfigure(1)
        # Label 'Selecione a bitola da armadura'
        ttk.Label(frame_arm,text='Bitola a inserir:').grid(
            row=0,column=0,sticky='w',padx=5,pady=5)
        # DropDown de armaduras
        self.bitola = tk.StringVar()
        self.bitola.set(8)
        self.armaduras_dropdown = ttk.Combobox(frame_arm,
            textvariable=self.bitola, state='readonly', width=10)
        self.armaduras_dropdown['values'] = (8, 10, 12.5, 16, 20, 25)
        self.armaduras_dropdown.grid(row=0,column=1,sticky='w',padx=5,pady=5)
        self.armaduras_dropdown.focus()
        frame_arm.pack()

        # Button 'Finalizar'
        end_button = ttk.Button(master,text='Finalizar',command=master.destroy,
            width=10)
        end_button.pack()

root = tk.Tk()
armadura = App(root)
root.mainloop()
armadura = float(armadura.bitola.get())
print(armadura)
print(type(armadura))