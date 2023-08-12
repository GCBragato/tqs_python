#Regra para gerar a saída
def gera_saida(delta_x1, delta_x2, cargas_entrada, cargas_saida):
    for line in cargas_entrada:
        if line.split()[0] != "CON" \
            and line.split()[0] != "CARGAS" \
            and line.split()[0] != "CHORIZ" \
            and line.split()[0] != "FIM":
                continue
        elif line.split()[0] == "CON":
            for i in [0, delta_x1, delta_x2]:
                cargas_format = "{:>7}{:>14},{:>14}{:>6}{:>14} ".format(
                line.split()[0],
                "{0:.3f}".format(float(line.split()[1].replace(",",""))+i),
                "{0:.3f}".format(float(line.split()[2])),
                line.split()[3],
                "{0:.3f}".format(float(line.split()[4]))
                )
                cargas_saida.write(cargas_format.rstrip(" ")+"\n")
        elif line.split()[0] == "CARGAS":
            if line.split()[2] != "1":
                cargas_saida.write(f'  CARGAS CASO   {line.split()[2]}\n')
            else:
                cargas_saida.write(f'  CARGAS CASO   {line.split()[2]}\n')
        elif line.split()[0] == "CHORIZ":
            cargas_saida.write(f'    CHORIZ       {"{0:.3f}".format(3*float(line.split()[1]))}\n')
        elif line.split()[0] == "FIM":
            if line.split()[2] == "Final":
                cargas_saida.write(" FIM")
            else:
                cargas_saida.write("  FIM\n")
########################################################################################################
    
# Variáveis de entrada
delta_x1 = 5239.8142 #Delta X1
delta_x2 = 10460.6077 #Delta X2
cargas_entrada = open(".\CARGASEX.DAT") #Arquivo de entrada
cargas_saida = open(".\CARGASEX - SAÍDA.DAT","w") #Arquivo de saída
########################################################################################################

#Chama a saida
gera_saida(delta_x1, delta_x2, cargas_entrada, cargas_saida)
########################################################################################################

