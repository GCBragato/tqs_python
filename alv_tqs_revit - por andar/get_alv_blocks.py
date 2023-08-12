from TQS import TQSDwg
import brgt_files_handler as bfh
import get_wall_line as gwl
from os import path, getcwd
from sys import path as sys_path

def corrige_escalas(xScale, insAngle):
    """Corrige insAngle se xScale for negativo"""
    if xScale < 0:
        xScale = -xScale
        insAngle = (insAngle+180)%360
    return xScale, insAngle

def get_alv_blocks(dwgPath):
    myLayers = [245, 241, 251, 252, 161, 246, 242]

    #Abre o arquivo DWG TQS
    dwg = TQSDwg.Dwg()
    dwg.file.Open (dwgPath)
    if dwg.file.Open (dwgPath) != 0:
        print("Não abri o arquivo [%s] para leitura" % dwgPath)
    elif dwg.file.Open (dwgPath) == 0:
        #print("Abri o arquivo [%s] para leitura" % dwgPath)
        pass

    # Ler elementos em níveis desligados
    dwg.settings.levelsReadMode = 0

    #Inicia a lista de blocos
    myBlocks = []

    #Começa o iterador
    dwg.iterator.Begin()
    while True:
        itipo = dwg.iterator.Next()
        #print(itipo)

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

    #if dwgPath == r"C:\TQS\VEGA\MAX Ipes\VEGA Max Ipes Alvest T1\Cobertura\DesFiad1.DWG":
        #print(myBlocks)

    return myBlocks

if __name__ == '__main__':
    projeto = 'C:\TQS\VEGA\MAX Ipes\VEGA Max Ipes Alvest T1'
    projeto_nome = path.basename(projeto)
    pavimento = 'Cobertura'
    dwgPath = path.join(projeto, pavimento, 'DesFiad1.DWG')
    blocos = get_alv_blocks(dwgPath)
    #dwgPathMod = path.join(projeto, pavimento, pavimento)
    #myLines = gwl.get_wall_line(dwgPathMod)
    #bfh.write_blocks(projeto_nome,pavimento,blocos,myLines)