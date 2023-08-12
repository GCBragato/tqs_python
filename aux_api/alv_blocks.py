class Bloco():
    #          Bloco( 39,      14,      19,     'I',     [2],      2,      [],      2.5)
    def __init__(self,comp:int,larg:int,alt:int,tipo:str,graute=[],nsept=2,lsept=[],esp=2.5):
        self.comp = comp
        self.larg = larg
        self.alt = alt
        if nsept == 0:
            nsept = 1
            lsept = [comp]
        self.nsept = nsept
        self.lsept = lsept
        self.esp = esp
        # 'graute' é uma lista indicando se o septo, enumerado da
        # esquerda para a direita, está grauteado
        # Se lista de pontos de graute != vazia, reduzir os valores
        # dentro dela em 1
        graute = [i-1 for i in graute if graute]
        self.graute = graute
        # Se lista de comprimentos de septos vazia, executar função
        # que calcula o comprimento de cada septo automaticamente
        if not lsept:
            self.lsept = self.auto_sept(tipo)

        # Dados de área e coordenadas de cada septo
        self.csept = self.sept_comp(self.lsept,self.esp)
        self.asept = self.sept_area(self.csept,self.larg)
        self.xysept = self.sept_coords(self.comp,self.larg,self.csept)
        self.xyseptCG = self.sept_coordsCG(self.xysept)
        self.xyseptGCG = self.sept_coordsGCG(self.xyseptCG,self.graute)

    def auto_sept(self,tipo:str):
        """Retorna lista de septos para os tipos I (septos Iguais),
        T (Tê) e C (Canto)
        """

        lsept = []
        if tipo.upper() == 'I':
            #Se tipo Iguais, calcular todos os septos iguais
            for i in range(self.nsept):
                lsept.append((self.comp-(self.nsept+1)*self.esp)/
                self.nsept)
        elif tipo.upper() == 'T':
            #Aceita 3 septos
            #Se tipo T, teremos 3 septos, sendo o 1 e 3 iguais
            #Cálculo para septo do Meio
            sM = self.larg-2*self.esp
            #Cálculo para septos do Lado
            sL = (self.comp-sM-self.esp*4)/2
            lsept = [sL,sM,sL]
            self.nsept = 3
        elif tipo.upper() =='C':
            #Aceita 2 septos
            #Se tipo C, teremos 2 septos, sendo o à esquerda o menor
            #Cálculo para septo Menor
            sM = self.larg-2*self.esp
            #Cálculo para septo mAior
            sA = self.comp-sM-self.esp*3
            lsept = [sM,sA]
        return lsept

    def sept_comp(self,lsept,esp):
        """Comprimento de cada septo bruto"""
        #Se septo for último ou primeiro, comprimento dele é lsept + esp + 1/2 esp
        #Se não, lsept + 1/2 esp + 1/2 esp
        csept = []
        if len(lsept) == 0:
            return [self.comp]
        for i in range(len(lsept)):
            if i == 0 or i == len(lsept)-1:
                csept.append(lsept[i]+1.0*esp+0.5*esp)
            else:
                csept.append(lsept[i]+0.5*esp+0.5*esp)
        return csept

    def sept_area(self,csept,larg):
        """Área de cada septo bruto"""
        asept = []
        if len(csept) == 0:
            return self.areaL
        for i in range(len(csept)):
            asept.append(csept[i]*larg)
        return asept

    def sept_coords_liquid(self,comp,larg,esp,lsept):
        """Coordenadas dos vértices de cada septo líquido"""
        dAc = -comp/2
        coords = []
        for i in range(len(lsept)):
            dAc += esp+lsept[i]/2
            c1 = [dAc+(lsept[i]/2),-(larg/2)+esp]
            c2 = [dAc+(lsept[i]/2),(larg/2)-esp]
            c3 = [dAc-(lsept[i]/2),(larg/2)-esp]
            c4 = [dAc-(lsept[i]/2),-(larg/2)+esp]
            coords.append([c1,c2,c3,c4])
            dAc += lsept[i]/2
        return coords

    def sept_coords(self,comp,larg,csept):
        """Coordenadas dos vértices de cada septo bruto"""
        dAc = -comp/2
        coords = []
        for i in range(len(csept)):
            c1 = [dAc,+larg/2]
            c2 = [dAc,-larg/2]
            c3 = [dAc+csept[i],-larg/2]
            c4 = [dAc+csept[i],+larg/2]
            coords.append([c1,c2,c3,c4])
            dAc += csept[i]
        return coords

    def sept_coordsCG(self,xysept):
        """Coordenas do CG de cada septo"""
        # xysept é uma lista de listas
        # A lista [0] tem o comprimento igual ao número de septos do bloco
        # A lista [1] tem o comprimento de 4, sendo cada um uma lista
        # A lista [2] tem o comprimento de 2, são coordenadas cartesianas

        # Precisamos retornar 1 lista d2
        # Lista [0] é uma lista de septos
        # Lista [1] é uma lista com CG de cada septo
        septo = []
        for m in range(len(xysept)): # Loop externo, percorre septos
            cgX = 0.0
            cgY = 0.0
            coorsX = []
            coorsY = []
            # PODE SER OTIMIZAADO PARA 1 SÓ LOOP
            for i in range(4): # Loop interno a, extrai as coordenadas
                coorsX.append(xysept[m][i][0])
                coorsY.append(xysept[m][i][1])
            for i in range(4): #Loop interno b, calcula o CG
                cgX += (coorsX[i-1]+coorsX[i])*(coorsX[i-1]*coorsY[i]-coorsX[i]*coorsY[i-1])
                cgY += (coorsY[i-1]+coorsY[i])*(coorsX[i-1]*coorsY[i]-coorsX[i]*coorsY[i-1])
            septo.append([cgX/(6*self.asept[m]),cgY/(6*self.asept[m])])
        return septo

    def sept_coordsGCG(self,xyseptCG,graute):
        """Coordenadas do CG de cada septo grauteado"""
        xyseptGCG = []
        for septo in graute:
            xyseptGCG.append(xyseptCG[septo])
        return xyseptGCG


#Família 39x14
def dict_fam():
    P0515 = Bloco(4,14,19,'I',[],0,[0],0)
    P1015 = Bloco(9,14,19,'I',[],0,[0],0)
    P2015 = Bloco(19,14,19,'I',[],1,[],2.5)
    P2015G = Bloco(19,14,19,'I',[1],1,[],2.5)
    P3515 = Bloco(34,14,19,'C',[],2,[],2.5)
    P3515G1 = Bloco(34,14,19,'C',[2],2,[],2.5)
    P3515G2 = Bloco(34,14,19,'C',[1],2,[],2.5)
    P3515F = Bloco(34,14,19,'C',[1,2],2,[],2.5)
    P4015 = Bloco(39,14,19,'I',[],2,[],2.5)
    P4015G = Bloco(39,14,19,'I',[2],2,[],2.5)
    P4015F = Bloco(39,14,19,'I',[1,2],2,[],2.5)
    P5515 = Bloco(54,14,19,'T',[],3,[],2.5)
    P5515G1 = Bloco(54,14,19,'T',[2],3,[],2.5)
    P5515G2 = Bloco(54,14,19,'T',[2,3],3,[],2.5)
    P5515G3 = Bloco(54,14,19,'T',[3],3,[],2.5)
    P5515F = Bloco(54,14,19,'T',[1,2,3],3,[],2.5)

    familia_39x14_dict = {
    'P0515':P0515,
    'P1015':P1015,
    'P2015':P2015,
    'P2015G':P2015G,
    'P3515':P3515,
    'P3515G1':P3515G1,
    'P3515G2':P3515G2,
    'P3515F':P3515F,
    'P4015':P4015,
    'P4015G':P4015G,
    'P4015F':P4015F,
    'P5515':P5515,
    'P5515G1':P5515G1,
    'P5515G2':P5515G2,
    'P5515G3':P5515G3,
    'P5515F':P5515F,
    }
    return familia_39x14_dict
