from TQS import TQSBuild

def get_project_floors(projeto):
    """Lista os pavimentos do projeto"""
    build = TQSBuild.Building()
    full_path = projeto.replace('C:\\TQS\\', '')
    build.file.Open(full_path)
    tot_pavimentos = build.floorsplan.floorsPlanNumber
    nom_pavimentos = []
    for pav in range(tot_pavimentos):
        nom_pavimentos.append(build.floorsplan.GetName(pav))
    return nom_pavimentos

def get_project_numbers(projeto):
    """Lista os números dos pavimentos do projeto"""
    build = TQSBuild.Building()
    full_path = projeto.replace('C:\\TQS\\', '')
    build.file.Open(full_path)
    tot_pavimentos = build.floorsplan.floorsPlanNumber
    num_pavimentos = []
    for pav in range(tot_pavimentos):
        num_pavimentos.append(build.floorsplan.GetProjectNumber(pav))
    return num_pavimentos

if __name__ == '__main__':
    projeto = r"C:\TQS\VEGA\MAX Ipes\VEGA Max Ipes Alvest T1"
    pavimentos = get_project_floors(projeto)
    #print(pavimentos)
    numeros = get_project_numbers(projeto)
    #print(numeros)
    pav = [[a,b] for a,b in zip(pavimentos,numeros)]
    for p in pav:
        print(p)