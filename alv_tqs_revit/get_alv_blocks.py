from TQS import TQSDwg

def corrige_escalas(xScale, insAngle):
    """Corrige insAngle se xScale for negativo"""
    if xScale < 0:
        xScale = -xScale
        insAngle = (insAngle+180)%360
    return xScale, insAngle

def get_alv_blocks(dwgPath):
    myLayers = [245, 241, 252, 161]

    #Abre o arquivo DWG TQS
    dwg = TQSDwg.Dwg()
    dwg.file.Open (dwgPath)
    if dwg.file.Open (dwgPath) != 0:
        print("Não abri o arquivo [%s] para leitura" % dwgPath)
    elif dwg.file.Open (dwgPath) == 0:
        pass

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
                xScale, insertAngle = corrige_escalas(xScale, insertAngle)

                #Adiciona as propriedades como lista na lista myBlocks
                myBlocks.append([blockName,x,y,xScale,yScale,insertAngle])

        #Termina o loop ao encontrar o fim do DWG
        if itipo == TQSDwg.DWGTYPE_EOF:
            break

    #Fecha o arquivo DWG TQS
    dwg.file.Close()
    return myBlocks

if __name__ == '__main__':
    dwgPath = r'C:\TQS\VEGA\MAX CEM\VEGA Max CEM Alvenaria 2\Tipo 8 a 10\Tipo 8 a 10 Teste'
    print(get_alv_blocks(dwgPath))