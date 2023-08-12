from os import path, getcwd,chdir
from sys import path as sys_path
sys_path.append(getcwd())
sys_path.append(getcwd() + "\\alv_tqs_revit")
sys_path.append(getcwd() + "\\tqs_browser")

import treeview_create as tc
from TQS import TQSDwg


def cb_ca(projeto):
    # Caminhos
    porlid = path.join(projeto,'ESPACIAL','PORLID.DWG')
    b_dat = path.join(projeto,'FUNDAC','B0001.DAT')

    # Cria objeto TQS Dwg e Abre para Edição
    dwg = TQSDwg.Dwg()
    dwg.file.Open(porlid)
    if dwg.file.Open(porlid) != 0:
        print("Não abri o arquivo [%s] para edição" % porlid)
    elif dwg.file.Open(porlid) == 0:
        print("Abri o arquivo [%s] para edição" % porlid)
        pass

    # Iterador para detectar textos
    t_ca = []
    dwg.iterator.Begin()
    while True:
        itipo = dwg.iterator.Next()
        # Se é Texto && Está na Layer correta && Começa com CA
        if itipo == TQSDwg.DWGTYPE_TEXT and dwg.iterator.level == 12 and dwg.iterator.text[:2] == 'CA':
            #print(dwg.iterator.text)
            address = dwg.iterator.GetElementReadPosition()
            x = dwg.iterator.x1
            y = dwg.iterator.y1
            height = dwg.iterator.textHeight
            angle = dwg.iterator.textAngle
            text = dwg.iterator.text
            t_ca.append([address,x,y,height,angle,text])
        # Se é fim do arquivo, sair do loop
        if itipo == TQSDwg.DWGTYPE_EOF:
            break

    # Encontrar Altura e Nome do Bloco
    t_bloco = []
    h_bloco = []
    for t in t_ca:
        # Deletar texto de CA
        dwg.edit.Erase(t[0])
        # Iterador para detectar blocos
        dwg.iterator.Begin()
        while True:
            itipo = dwg.iterator.Next()
            # Se é Texto && Está na Layer correta && Tem a Mesma Coordenada X && Distância Y menor que 50
            if (itipo == TQSDwg.DWGTYPE_TEXT and
                dwg.iterator.level == 72 and
                dwg.iterator.x1 == t[1] and
                abs(dwg.iterator.y1 - t[2]) < 50):

                t_bloco.append([dwg.iterator.text])

            elif (itipo == TQSDwg.DWGTYPE_TEXT and
                dwg.iterator.level == 12 and
                dwg.iterator.x1 == t[1] and
                abs(dwg.iterator.y1 - t[2]) < 50 and
                dwg.iterator.text[:2] == 'HF'):

                h_bloco.append([dwg.iterator.text[3:]])

            if itipo == TQSDwg.DWGTYPE_EOF:
                break

    # Encontrar o Comprimento de Embutimento
    t_emb = {}
    b_dat_file = open(b_dat,'r')
    b_dat_lines = b_dat_file.readlines()
    b_dat_file.close()
    b_dat_lines = [line.rstrip() for line in b_dat_lines]
    # Cada Linha de Blocos
    b_lines = [n for n in range(len(b_dat_lines)) if b_dat_lines[n][5:6] == 'B']
    for line in b_lines:
        bloco = b_dat_lines[line][5:10].strip()
        emb = float(b_dat_lines[line+2][15:26].strip())
        t_emb.update({bloco:emb})

    combined = [[a,b,c] for a,b,c in zip(t_ca,t_bloco,h_bloco)]

    # Extrai CA e Calcula CB
    for item in combined:
        address = item[0][0]
        x = float(item[0][1])
        y = float(item[0][2])
        height = float(item[0][3])
        angle = float(item[0][4])
        text = item[0][5]
        ca = float(text[3:text.find('m')])
        bloco = item[1][0]
        h_bloco = float(item[2][0])
        emb = t_emb[bloco]
        cb = ca + h_bloco/100 - emb/100
        cb_ca_final = 'CB=' + str(round(cb,2)) + 'm/CA=' + str(round(ca,2)) + 'm'
        dwg.draw.Text(x,y,height,angle,cb_ca_final)

    # Salva e Fecha o DWG
    dwg.file.Save()
    dwg.file.Close()
    return


def main ():
    #projeto = r'C:\TQS\Realiza\Terraco Sky\Terraco Sky R06'
    projeto = tc.main('',False)
    cb_ca(projeto)
    #print('Pronto.')


if __name__ == '__main__':
    main()