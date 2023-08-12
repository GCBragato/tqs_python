from TQS import TQSDwg


def get_wall_line(dwgPath):

    #Abre o arquivo DWG TQS
    dwg = TQSDwg.Dwg()
    dwg.file.Open (dwgPath)
    if dwg.file.Open (dwgPath) != 0:
        print("Não abri o arquivo [%s] para leitura" % dwgPath)
    elif dwg.file.Open (dwgPath) == 0:
        #print('Arquivo aberto com sucesso')
        pass

    # Ler elementos em níveis desligados
    dwg.settings.levelsReadMode = 0

    #Inicia a lista de linhas
    myLines = []

    #Começa o iterador
    dwg.iterator.Begin()
    while True:
        itipo = dwg.iterator.Next()

        #Se é linha
        if itipo == TQSDwg.DWGTYPE_POLYLINE:

            #Se está nas layers listadas
            if dwg.iterator.level == 233:

                #Salva as propriedades do bloco em variáveis temporárias
                x1 = dwg.iterator.x1
                y1 = dwg.iterator.y1
                x2 = dwg.iterator.x2
                y2 = dwg.iterator.y2

                #Adiciona as propriedades como lista na lista myBlocks
                myLines.append([x1,y1,x2,y2])

        #Termina o loop ao encontrar o fim do DWG
        if itipo == TQSDwg.DWGTYPE_EOF:
            break

    #Fecha o arquivo DWG TQS
    dwg.file.Close()
    return myLines

if __name__ == '__main__':
    dwgPath = r'C:\TQS\VEGA\MAX Ipes\VEGA Max Ipes Alvest T2 Old\Tipo 1 ao 6\Tipo 1 ao 6'
    print(get_wall_line(dwgPath))