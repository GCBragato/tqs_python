import os
import dataclasses

def read_opening(projeto, opening_type):
    """Lê arquivos de aberturas do projeto"""

    # Diretório, abre, lê e transforma em lista
    openingPath = os.path.join(projeto+'\\'+opening_type+'.DAT')
    openingFile = open(openingPath, 'r')
    openingLines = openingFile.read().splitlines()
    openingFile.close()

    # Calcula a quantidade de aberturas do arquivo
    openingQnt = int(len(openingLines)/7)
    
    # Cria lista de open
    # Loop externo, pula de abertura em abertura
    openingList = []
    for opening in range(openingQnt):
        dataLine = opening*7
        name = openingLines[dataLine]
        dimX = float(openingLines[dataLine+1][0:15])
        dimY = float(openingLines[dataLine+1][16:30])
        dimZ = float(openingLines[dataLine+1][31:45])
        cotaInicial = float(openingLines[dataLine+1][46:60])
        c_verga = float(openingLines[dataLine+2][0:10])
        h_verga = float(openingLines[dataLine+2][11:20])
        c_cverga = float(openingLines[dataLine+3][0:10])
        h_cverga = float(openingLines[dataLine+3][11:20])
        descricao = openingLines[dataLine+5]
        openingList.append([
            name.strip(),
            dimX,
            dimY,
            dimZ,
            cotaInicial,
            c_verga,
            h_verga,
            c_cverga,
            h_cverga,
            descricao.strip()
        ])
    return openingList

def read_openings(projeto):
    portas = read_opening(projeto, 'PORTAS')
    janelas = read_opening(projeto, 'JANELAS')
    return portas,janelas
    
if __name__ == "__main__":
    projeto = r'C:\TQS\CEA\Mississipi\CEA-MISSISSIPI'
    portas,janelas = read_openings(projeto)
    print()
    print('Portas:')
    print(portas)
    print()
    print('Janelas:')
    print(janelas)