import numpy as np
class cargas:
    def __init__(self,linha,case):
        self.linha = linha
        self.case = case
        pass
class CHORIZ:
    def __init__(self,linha,case):
        self.linha = linha
        self.case = case
        pass
class fim:
    def __init__(self,linha):
        self.linha = linha
        pass
# Rotaciona Coordenadas
def rotate(vector, angulo):

    angulo = np.radians(angulo)
    rotacao = np.array([[np.cos(angulo), np.sin(angulo)],
                        [-np.sin(angulo), np.cos(angulo)]])
    return np.dot(vector, rotacao)

#Regra para gerar a saída
def gera_saida(delta_coords, cargas_entrada, cargas_saida,apagar_origem):
    caso = 0
    list_conlinha = []
    list_cargas = []
    list_choriz = []
    list_fim = []

    for line in cargas_entrada:
        if line.split()[0] != "CON" \
            and line.split()[0] != "CARGAS" \
            and line.split()[0] != "CHORIZ" \
            and line.split()[0] != "FIM":
                continue
        elif line.split()[0] == "CON":
            list = [[0.0,0.0,0.0]]
            list.extend(delta_coords)            
            count = 0
            while count <len(list):
                if apagar_origem and count == 0:
                    count += 1
                    continue
                vector = np.zeros(2)
                vector[0] = float(line.split()[1].replace(",",""))
                vector[1] = float(line.split()[2].replace(",",""))                
                vector = rotate(vector, list[count][2])
                cargas_format = "{:>7}{:>14},{:>14}{:>6}{:>14} ".format(
                line.split()[0],
                "{0:.3f}".format(vector[0]+float(list[count][0])), #X
                "{0:.3f}".format(vector[1]+float(list[count][1])), #Y
                line.split()[3],
                "{0:.3f}".format(float(line.split()[4]))
                )
                if caso == 5:
                    if list[count][2] == 90:
                        list_conlinha.append(cargas(cargas_format,7))
                    elif list[count][2] == 180:
                        list_conlinha.append(cargas(cargas_format,6))
                    elif list[count][2] == 270 or list[count][2] == -90:
                        list_conlinha.append(cargas(cargas_format,8))
                    elif list[count][2] == 0:
                        list_conlinha.append(cargas(cargas_format,5))
                elif caso == 6:
                    if list[count][2] == 90:
                        list_conlinha.append(cargas(cargas_format,8))
                    elif list[count][2] == 180:
                        list_conlinha.append(cargas(cargas_format,5))
                    elif list[count][2] == 270 or list[count][2] == -90:
                        list_conlinha.append(cargas(cargas_format,7))
                    elif list[count][2] == 0:
                        list_conlinha.append(cargas(cargas_format,6))
                elif caso == 7:
                    if list[count][2] == 90:
                        list_conlinha.append(cargas(cargas_format,6))
                    elif list[count][2] == 180:
                        list_conlinha.append(cargas(cargas_format,8))
                    elif list[count][2] == 270 or list[count][2] == -90:
                        list_conlinha.append(cargas(cargas_format,5))
                    elif list[count][2] == 0:
                        list_conlinha.append(cargas(cargas_format,7))
                elif caso == 8:
                    if list[count][2] == 90:
                        list_conlinha.append(cargas(cargas_format,5))
                    elif list[count][2] == 180:
                        list_conlinha.append(cargas(cargas_format,7))
                    elif list[count][2] == 270 or list[count][2] == -90:
                        list_conlinha.append(cargas(cargas_format,6))
                    elif list[count][2] == 0:
                        list_conlinha.append(cargas(cargas_format,8))
                else:
                    list_conlinha.append(cargas(cargas_format,caso))
                count += 1
        elif line.split()[0] == "CARGAS":
            if line.split()[2] != "1":
                caso = int(line.split()[2])
                list_cargas.append(cargas(f'  CARGAS CASO   {line.split()[2]}',caso))
                
            else:
                caso = int(line.split()[2])
                list_cargas.append(cargas(f'  CARGAS CASO   {line.split()[2]}',caso))                
        elif line.split()[0] == "CHORIZ":
            copies=0
            if apagar_origem:
                copies = len(delta_coords)
            else:  
                copies = len(delta_coords)+1
            list_choriz.append(CHORIZ(f'    CHORIZ       {"{0:.3f}".format((copies)*float(line.split()[1]))}\n',caso))
            
        
    for caso in list_cargas:
        cargas_saida.write(caso.linha+"\n")
        for conlinha in list_conlinha:
            if conlinha.case == caso.case:
                cargas_saida.write(conlinha.linha+"\n")
        for choriz in list_choriz:
            if choriz.case == caso.case:
                cargas_saida.write(choriz.linha+"\n")
        cargas_saida.write("  FIM\n")
    cargas_saida.write(" FIM")
    

########################################################################################################
# Variáveis de entrada
_delta_coords = [[10,10.0,90],[20,20.0,180]] # Coordenadas de deslocamento
apagar_origem = False
########################################################################################################
delta_coords = np.zeros((len(_delta_coords),3))
for i in range(len(_delta_coords)):
    delta_coords[i][0] = _delta_coords[i][0]
    delta_coords[i][1] = _delta_coords[i][1]
    delta_coords[i][2] = _delta_coords[i][2]

#delta_coords = np.array(_delta_coords)
#delta_x1 = 5239.8142 #Delta X1
#delta_x2 = 10460.6077 #Delta X2
cargas_entrada = open("C:/Users/Carlos/OneDrive/repos/brgt/Python/tqs_python/cargasex_pro/CARGASEX.DAT") #Arquivo de entrada
cargas_saida = open("C:/Users/Carlos/OneDrive/repos/brgt/Python/tqs_python/cargasex_pro/CARGASEX - SAÍDA.DAT","w") #Arquivo de saída
########################################################################################################

#Chama a saida
gera_saida(delta_coords, cargas_entrada, cargas_saida,apagar_origem)
########################################################################################################

