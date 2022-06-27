import os
import tkinter as tk
from tkinter import ttk

folder = os.path.normpath(r'C:\TQS\Clinica Multimed\CM A - Estrutura Original')
print(f'folder = {folder}')
print(f'folder dirname = {os.path.dirname(folder)}')
print(f'folder basename = {os.path.basename(folder)}')
print(f'split = {os.path.split(folder)}')

dude = ['C:\\','ARROZ','FEIJAO']
print(os.path.join(*dude))


        # for project in projects:
        #     parent_path = path.dirname(project)
        #     print(f'projeto = {project}')
        #     print(f'parent_path = {parent_path}')
        #     if parent_path == self.path:
        #         self.tree.insert(parent_path, 'end', iid=project, text=path.basename(project),open=True)
        #     else:
        #         while parent_path != self.path:
        #             if self.tree.exists(parent_path) and parent_path!=self.path:
        #                 self.tree.insert(parent_path,'end',text=path.basename(project))
        #                 parent_path=path.dirname(parent_path)
        #             else:
        #                 self.tree.insert(path.dirname(parent_path), 'end', iid=parent_path, text=path.basename(parent_path),open=True)
        #                 parent_path=path.dirname(parent_path)
