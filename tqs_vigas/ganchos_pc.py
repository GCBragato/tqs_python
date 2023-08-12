""" Programa para deletar os ganchos em Pontos de Carga """


from os import path, getcwd,chdir
from sys import path as sys_path
sys_path.append(getcwd())
sys_path.append(getcwd() + "\\alv_tqs_revit - por andar")
sys_path.append(getcwd() + "\\tqs_browser")


from glob import glob
import treeview_create as tc


def get_vigas(pavimento):
    pasta_vigas = path.join(pavimento, "VIGAS\\")
    print(pasta_vigas)
    vigas = []
    chdir(pasta_vigas)
    for file in glob("*.GEO"):
        vigas.append(file)
    return vigas


def deleta_ganchos(pavimento, vigas):
    """Apaga os ganchos em Pontos de Carga"""
    pasta_vigas = path.join(pavimento, "VIGAS\\")
    for viga in vigas:

        print("")
        print("Viga: ", viga)
        # Abre o arquivo
        arq = open(path.join(pasta_vigas,viga), "r+")
        # Lê o arquivo
        texto = ''
        texto = arq.read().splitlines()

        # Encotra linha com todos os apoios
        # É linha de apoios depois da linha de apoios
        loc_aux = 0
        i = 0
        for i,linha in enumerate(texto):
            # A segunda linha não vazia é a linha de apoios
            if linha[0] != " ": loc_aux += 1
            if loc_aux == 2: break
        linha_tipos_apoios = texto[i]
        linha_apoios = texto[i+1]

        # Número de apoios é a quantidade de espaços + 1
        # Porém, podemos ter até 3 espaços sequentes, logo, substituiremos
        # antes de contar
        linha_apoios = linha_apoios.rstrip()
        linha_apoios = linha_apoios.replace("   ", " ")
        linha_apoios = linha_apoios.replace("  ", " ")
        # Conta o número de apoios
        n_apoios = linha_apoios.count(" ") + 1

        # Se primeiro e último apoio for dentro das possibilidades
        # definir o binário
        apoios_possiveis = [0,1,3,4,5]
        tipos_apoios = [*linha_tipos_apoios[0:n_apoios]]
        print('tipos_apoios = ',tipos_apoios)
        # Lista com 2 valores, se 0 é PC, se 1 não é
        if int(tipos_apoios[0]) in apoios_possiveis:
            apoio_esquerda = 1
        else:
            apoio_esquerda = 0
        if int(tipos_apoios[-1]) in apoios_possiveis:
            apoio_direita = 1
        else:
            apoio_direita = 0
        tipo_apoio = [apoio_esquerda, apoio_direita]
        print('tipo_apoio = ',tipo_apoio)

        # Encontra a linha (j) dos ganchos
        # É linha de gancho se caracteres nas posições 22, 32 e 42 são '.'
        j = 1
        for j,linha in enumerate(texto):

            # Encontra a posição de pontos na linha
            dot_pos = []
            index = 0
            while index < len(texto[j]):
                index = texto[j].find('.', index)
                if index == -1:
                    break
                index += 1
                dot_pos.append(index)

            # Se as posições forem compatíveis, sai do loop tendo j como linha
            if dot_pos == [22,32,42]:
                break
        j += 1
        print('j = ',j)

        # Encontra a qtde de linhas e a última linha de ganchos
        n_lin_ganchos = ( n_apoios + 1 ) * 2
        print('n_lin_ganchos = ',n_lin_ganchos)
        last_line = j + n_lin_ganchos - 1
        print('last_line = ',last_line)

        # Encontrar a linha específica de gancho e substituir
        linha_s_ganc = '    0    0    0     0.000     0.000     0.000    0    0'
        # Primeiro apoio = 3a linha = j + 2
        # Último apoio = antepenúltima linha = last_line - 2
        if tipo_apoio[0] == 1:
            # Se é PC, substitui a linha de gancho por linha de apoio
            print('linha_a_ser_corrigida = ',j+1)
            print('texto da linha a ser corrigida = ',texto[j+1])
            texto[j+1] = linha_s_ganc
        if tipo_apoio[1] == 1:
            print('linha_a_ser_corrigida = ',last_line-3)
            print('texto da linha a ser corrigida = ',texto[last_line-3])
            texto[last_line-3] = linha_s_ganc

        # Busca o começo do arquivo e limpa
        arq.seek(0)
        arq.truncate(0)
        #Cria o texto novo e o escreve no arquivo
        texto_novo = '\n'.join(texto)
        arq.write(texto_novo)
        # Fecha o arquivo
        arq.close()


def main():
    initialdir = ''
    if path.exists(r'C:\TQS'):
        initialdir = r'C:\TQS'
    pavimento = tc.main(initialdir,True)
    #pavimento = r'C:\TQS\Concreto - Torre A e B - R02\Térreo'
    vigas = get_vigas(pavimento)
    deleta_ganchos(pavimento, vigas)

if __name__ == '__main__':
    main()