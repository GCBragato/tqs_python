from TQS import TQSDwg
import brgt_files_handler as bfh
import get_wall_line as gwl
from os import path, getcwd
from sys import path as sys_path
import math as m

#def get_openings_names():
def get_openings_names(blocos,dwgPath):

    dwg = TQSDwg.Dwg()
    dwg.file.Open (dwgPath)
    if dwg.file.Open (dwgPath) != 0:
        print("Não abri o arquivo [%s] para leitura" % dwgPath)
    elif dwg.file.Open (dwgPath) == 0:
        print("Abri o arquivo [%s] para leitura" % dwgPath)
        pass

    dwg.settings.levelsReadMode = 0

    myLayers = [216]
    NamesList = []
    #Começa o iterador
    dwg.iterator.Begin()
    while True:
        itipo = dwg.iterator.Next()

        #Se é texto
        if itipo == TQSDwg.DWGTYPE_TEXT:

            #Se está nas layers listadas
            if dwg.iterator.level in myLayers:

                # Extrair os dados do texto
                text = dwg.iterator.text
                x = dwg.iterator.x1
                y = dwg.iterator.y1
                NamesList.append(text+","+str(x)+","+str(y))
                #print(text, x, y)

        #Termina o loop ao encontrar o fim do DWG
        if itipo == TQSDwg.DWGTYPE_EOF:
            break
    
    for bloco in blocos:
        if bloco[0] == "$BLVAO":

            dist = -1
            nome = "null"
            for name in NamesList:
                n = str.split(name,",")
                x = float(n[1])
                y = float(n[2])
                if dist==-1 :
                    dist = distancia_entre_pontos(x,y,bloco[1],bloco[2])
                    nome = n[0]
                    #print(nome)
                else:
                    if distancia_entre_pontos(x,y,bloco[1],bloco[2])<dist:
                        dist = distancia_entre_pontos(x,y,bloco[1],bloco[2])
                        nome = n[0]
                        #print(nome)
            if nome != "null":
                bloco[0] = "$"+nome
            else: 
                print("Erro na comparação dos nomes dos vãos.")

    #Fecha o arquivo DWG TQS
    dwg.file.Close()
    #Retorna a lista de nomes
    return blocos


def distancia_entre_pontos(x1,y1,x2,y2):
    dist = m.sqrt((x1-x2)**2+(y1-y2)**2)
    return dist
