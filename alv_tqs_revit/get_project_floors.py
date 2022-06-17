from TQS import TQSBuild

def get_project_floors(projeto):
    """Lista os pavimentos do projeto"""
    build = TQSBuild.Building()
    full_path = projeto.replace('C:\\TQS\\', '')
    build.file.Open(full_path)
    num_pavimentos = build.floorsplan.floorsPlanNumber
    nom_pavimentos = []
    for pav in range(num_pavimentos):
        nom_pavimentos.append(build.floorsplan.GetName(pav))
    return nom_pavimentos

if __name__ == '__main__':
    pavimentos = get_project_floors(r"C:\TQS\CEA\Mississipi\CEA-MISSISSIPI")
    print(pavimentos)