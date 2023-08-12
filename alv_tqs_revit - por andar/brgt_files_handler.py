import os

def write_project_folder(projeto):
    """Cria o diretório de projeto no caminho
    OneDrive\\\\_ftf\\BRGT\\alv_tqs_revit\\\\%nome do projeto%"""
    onedrive = os.environ['OneDrive']
    #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    proj_folder = onedrive+'\\_ftf\\BRGT\\alv_tqs_revit\\'+projeto
    if not os.path.exists(proj_folder):
        os.makedirs(proj_folder)
    return proj_folder

def write_blocks(projeto,pavimento,blocos,myLines,fiada):
    """Escreve um arquivo ".atr" com os blocos e linhas para cada pavimento"""

    # Caminho da pasta do projeto dentro do OneDrive
    proj_folder = write_project_folder(projeto)

    complemento = ''
    # Define caminho do arquivo ".atr" para a fiada atual
    if fiada == '2aF':
        complemento = '_'+fiada

    pavimento = pavimento + complemento

    # Cria o arquivo ".atr"
    # Se existe, apaga e cria de novo (substitui)
    atr_file_path = os.path.join(proj_folder, '%s.atr' % os.path.basename(pavimento))
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
        for line in myLines:
            f.write(
                "$LINE,"+
                str(line[0])+","+
                str(line[1])+","+
                str(line[2])+","+
                str(line[3])+"\n"
            )

def write_opening(projeto, openings, opening_type):
    """Escreve um ".atr" com os dados das aberturas"""

    # Caminho da pasta do projeto dentro do OneDrive
    proj_folder = write_project_folder(projeto)

    # Cria o arquivo ".atr"
    # Se existe, apaga e cria de novo (substitui)
    atr_file_path = os.path.join(proj_folder, '%s.atr' % opening_type)
    if os.path.exists(atr_file_path):
        os.remove(atr_file_path)
    with open(atr_file_path, "x") as f:
        for opening in openings:
            f.write(
                str(opening[0])+","+
                str(opening[1])+","+
                str(opening[2])+","+
                str(opening[3])+","+
                str(opening[4])+","+
                str(opening[5])+","+
                str(opening[6])+","+
                str(opening[7])+","+
                str(opening[8])+","+
                str(opening[9])+"\n"
                )


def write_openings(projeto,portas,janelas):
    write_opening(projeto,portas,'PORTAS')
    write_opening(projeto,janelas,'JANELAS')


if __name__ == "__main__":
    blocos = [['P4015', 204.5, -467.0, 1.0, 1.0, 180.0], ['P1015', 229.5, -467.0, 1.0, 1.0, 180.0]]
    #write_pavs('ProjTeste','PavTeste',blocos)
    portas = [['P61', 59.0, 14.0, 221.0, 0.0, 119.0, 19.0, 0.0, 0.0, 'porta 59x220 cm'], ['P71', 69.0, 14.0, 221.0, 0.0, 129.0, 19.0, 0.0, 0.0, 'porta 69x220 cm']]
    write_openings('ProjTeste',portas,[])