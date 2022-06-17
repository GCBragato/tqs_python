import os

def write_atr(projeto,pavimento,blocos):
    """Escreve um arquivo ".atr" para cada pavimento"""

    # Cria o diretório de projeto no caminho
    # %apptada%\BRGT\alv_tqs_revit\%nome do projeto%
    appdata = os.environ['APPDATA'] 
    proj_folder = appdata+'\\BRGT\\alv_tqs_revit\\'+projeto
    if not os.path.exists(proj_folder):
        os.makedirs(proj_folder)

    # Cria o arquivo ".atr"
    # Se existe, apaga e cria de novo (substitui)
    atr_file_path = os.path.join(proj_folder, '%s.atr' % pavimento)
    if os.path.exists(atr_file_path):
        os.remove(atr_file_path)
    with open(atr_file_path, "x") as f:
        for bloco in blocos:
            f.write(
                str(bloco[0])+","+
                str(bloco[1])+","+
                str(bloco[2])+","+
                str(bloco[3])+","+
                str(bloco[4])+","+
                str(bloco[5])+"\n"
                )
    
if __name__ == "__main__":
    blocos = [['P4015', 204.5, -467.0, 1.0, 1.0, 180.0], ['P1015', 229.5, -467.0, 1.0, 1.0, 180.0]]
    write_atr('ProjTeste','PavTeste',blocos)