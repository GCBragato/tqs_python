# Importa a biblioteca do TQS
from TQS import TQSDwg
import sys

# Variáveis do usuário
#dwgPath = sys.argv[1]
dwgPath = r'C:\Users\gusta\OneDrive\repos\brgtrepos\Python\tqs_python\DesFiad1'
myLayers = [161, 241, 245, 251, 252]

"""
Layers:
161 - Pontos de Ferro
241 - Blocos de 1a Fiada
245 - Blocos sob aberturas
251 - Aberturas de Portas
252 - Aberturas de Janelas
"""

#Abre o arquivo DWG TQS
dwg = TQSDwg.Dwg()
if dwg.file.Open (dwgPath) != 0:
    print("Não abri o arquivo [%s] para leitura" % dwgPath)
elif dwg.file.Open (dwgPath) == 0:
    print("Abri o arquivo [%s] para leitura" % dwgPath)

#Inicia a lista de blocos
myBlocks = []

#Começa o iterador
dwg.iterator.Begin()
while True:
    itipo = dwg.iterator.Next()

    #Se é bloco
    if itipo == TQSDwg.DWGTYPE_BLOCK:

        #Se está nas layers listadas
        if dwg.iterator.level in myLayers:

            #Salva as propriedades do bloco em variáveis temporárias
            blockName = dwg.iterator.blockName
            x = dwg.iterator.x1
            y = dwg.iterator.y1
            xScale = dwg.iterator.xScale
            yScale = dwg.iterator.yScale
            insertAngle = dwg.iterator.insertAngle

            #Adiciona as propriedades como lista na lista myBlocks
            myBlocks.append([blockName,x,y,xScale,yScale,insertAngle])

    #Termina o loop ao encontrar o fim do DWG
    if itipo == TQSDwg.DWGTYPE_EOF:
        break

#Fecha o arquivo DWG TQS
dwg.file.Close()

#Printa todos os dados extraídos
for block in myBlocks:
    blockName,x,y,xScale,yScale,insertAngle = block
    myString = f'{blockName},{x},{y},{xScale},{yScale},{insertAngle}\n'
    sys.stdout.buffer.write(myString.encode('utf8'))