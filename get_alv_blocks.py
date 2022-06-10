# ----------------------------------------------------------------------------
#
#   Programa para salvar as propriedades de um bloco em um dado DWG, se
#   ele estiver nas layers indicadas
#   Engenheiro Civil Gustavo Campos Bragato - CREA 101.635.1704 D-GO
#   Criado em 10/05/2022
#   Última Versão (do Gustavo) criada em 10/05/2022
#   Última Versão (da Comunidade) criada em -
#
# ----------------------------------------------------------------------------
#
#   A venda deste algoritmo por pessoas que não sejam o Gustavo Campos Bragato
#   é ***EXPRESSAMENTE*** proibida.
#   Entretanto a divulgação e alteração do código é livre!
#
#   Se quiser discutir soluções de implementações diferentes, melhorar esse
#   código, criar uma interface de usuário, etc, peço que
#   você entre no grupo de telegram. O link é https://t.me/tqspython
#
# ----------------------------------------------------------------------------
#
#   INSTRUÇÕES DE USO:
#   1) Definir o caminho do seu DWG na variável 'dwgPath'
#   2) Os blocos só são extraídos se estiverem nas layers inseridas na
#   lista de layers myLayers. Insira ali as layers que deseja filtrar.
#   3) Os blocos são extraidos como lista para a lista myBlocks. myBlocks é
#   uma lista de listas. A lista do bloco tem os índices 0 a 5, sendo eles:
#   0 = Nome do bloco
#   1 = Coordenada X
#   2 = Coordenada Y
#   3 = Escala X
#   4 = Escala Y
#   5 = Ângulo de Rotação em Graus
#   4) Para extrair a coordenada X do 2º bloco da lista, por exemplo:
#   coordenadaX = myBlock[1][1]
#
# ----------------------------------------------------------------------------
# Início do Programa
# ----------------------------------------------------------------------------
# coding: utf-8

# Importa a biblioteca do TQS
from TQS import TQSDwg
import sys

# Variáveis do usuário
# dwgPath = r'C:\Users\gusta\OneDrive\repos\brgtrepos\Python\tqs_python\DesFiad1'
# Run this on CMD: python get_alv_fiad.py C:\Users\gusta\OneDrive\repos\brgtrepos\Python\tqs_python\DesFiad1
dwgPath = sys.argv[1]
myLayers = [245, 241, 252, 161]

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

#Exibe um pouco dos dados extraídos
qtdeBlocos = len(myBlocks)
print(f'{qtdeBlocos} blocos extraídos')
print('O primeiro bloco é este:', myBlocks[0])
print('O último bloco é este:', myBlocks[-1])
print('A coordenada x do último bloco é esta:',myBlocks[-1][1])

#Fecha o arquivo DWG TQS
dwg.file.Close()