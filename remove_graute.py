from sys import path as sys_path
from os import getcwd, path
sys_path.append(getcwd() + "\\tqs_browser")

from TQS import TQSDwg
import treeview_create as tc


def remove_graute(pavPath):
    # Nome do desenho é o nome do pavimento
    #dwgPath = path.join(pavPath,path.basename(pavPath))
    dwgPath = r'C:\Users\gusta\Desktop\DesFiad1'

    # Layers a serem filtradas
    myLayers = [241, 245]

    # Cria um objeto TQSDwg
    dwg = TQSDwg.Dwg()
    dwg.file.Open(dwgPath)
    if dwg.file.Open(dwgPath) != 0:
        print("Não abri o arquivo [%s] para leitura" % dwgPath)
    elif dwg.file.Open(dwgPath) == 0:
        #print("Abri o arquivo [%s] para leitura" % dwgPath)
        pass

    # Iterador para detectar e salvar os blocos grauteados
    myBlocks = []
    dwg.iterator.Begin()
    while True:
        itipo = dwg.iterator.Next()
        #Se é bloco
        if itipo == TQSDwg.DWGTYPE_BLOCK:
            #Se está nas layers listadas
            if dwg.iterator.level in myLayers:
                # Extrai o nome do bloco
                blockName = dwg.iterator.blockName
                # Se nome do bloco maior que 5 (grauteado), salva
                if len(blockName) > 5:
                    addr = dwg.iterator.GetElementReadPosition()
                    blockName = blockName[0:5]
                    x = dwg.iterator.x1
                    y = dwg.iterator.y1
                    xScale = dwg.iterator.xScale
                    yScale = dwg.iterator.yScale
                    insertAngle = dwg.iterator.insertAngle
                    level = dwg.iterator.level
                    myBlocks.append(
                        [addr,blockName,x,y,xScale,yScale,insertAngle,level]
                        )
        # Se é fim do arquivo, sair do loop
        if itipo == TQSDwg.DWGTYPE_EOF:
            break
    # Deletar blocos grauteados e insere sem graute
    for block in myBlocks:
        dwg.draw.level = block[7]
        dwg.draw.BlockInsert(block[1],block[2],block[3],block[4],block[5],block[6])
        dwg.edit.Erase(block[0])

    # Salva e fecha o arquivo
    dwg.file.Save()
    dwg.file.Close()


def main():
    #pavPath = tc.main('',True)
    pavPath = ''
    remove_graute(pavPath)


if __name__ == '__main__':
    main()