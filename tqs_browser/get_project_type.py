from TQS import TQSBuild

def get_project_type(projeto):
    """Lista os pavimentos do projeto"""
    build = TQSBuild.Building()
    full_path = projeto.replace('C:\\TQS\\', '')
    build.file.Open(full_path)
    structure_type = build.project.structureType
    return structure_type

if __name__ == '__main__':
    type = get_project_type("C:\\TQS\\CEA\\Mississipi\\CEA-MISSISSIPI")
    print(type)