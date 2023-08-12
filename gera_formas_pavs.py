from os import path, getcwd, chdir, listdir, rename
from sys import path as sys_path
sys_path.append(getcwd())
sys_path.append(getcwd() + "\\tqs_browser")


import treeview_create as tc
import get_project_floors as gpf
from tkinter.filedialog import askdirectory
from TQS import TQSDwg, TQSExec


def desenha_formas(projeto):

    # Dados do projeto
    nomeedi = projeto.split('\\')[-1]

    # Inicia o Job do TQSExec
    job = TQSExec.Job()
    
    # Processamento Global, mas só para Gerar Fôrmas
    job.EnterTask(TQSExec.TaskFolder(nomeedi, TQSExec.TaskFolder.FOLDER_FRAMES))
    job.EnterTask(TQSExec.TaskGlobalProc(
        floorPlan = 2,
        floorDraw = 1,
        slabs = 0,
        beams = 0,
        columnsData = 0,
        columns = 0,
        columnsReport = 0,
        gridModel = 0,
        gridDraw = 0,
        gridExtr = 0,
        gridAnalysis = 0,
        gridBeamsTrnsf = 0,
        gridSlabsTrnsf = 0,
        gridNonLinear = 0,
        frameModel = 0,
        frameAnalysis = 0,
        frameBeamsTrnsf = 0,
        frameColumnsTrnsf = 0,
        foundations = 0,
        stairs = 0,
        fire = 0,
        precastPhases = 0
    ))
    
    # Executa o Job
    job.Execute()


def copia_formas(projeto):
    nomes = gpf.get_project_floors(projeto)
    numeros = gpf.get_project_numbers(projeto)
    pasta = askdirectory(title='Selecione a pasta destino das Fôrmas')

    # Para cada pavimento, converter TQS DWG para DXF e copiá-lo
    for nome in nomes:
        # DWG da Fôrma
        dwg_path = path.join(
            projeto,
            nome,'FOR'+str.zfill(str(numeros[nomes.index(nome)]),4)+'.DWG'
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
    # Desenha as fôrmas do projeto
    desenha_formas(projeto)
    # Copia as fôrmas para pasta escolhida
    copia_formas(projeto)


if __name__ == '__main__':
    main()