from TQS import TQSBuild
import sys
build = TQSBuild.Building()
#full_path = sys.argv[1].replace('C:\\TQS\\', '')
full_path = r'C:\TQS\VEGA\MAX CEM\VEGA Max CEM Alvenaria'.replace('C:\\TQS\\', '')
build.file.Open(full_path)
num_pavimentos = build.floorsplan.floorsPlanNumber
nom_pavimentos = ""
for pav in range(num_pavimentos):
    if pav == 0:
        virgula = ''
    else:
        virgula = ','
    nom_pavimentos += virgula+build.floorsplan.GetName(pav)
sys.stdout.buffer.write(nom_pavimentos.encode('utf8'))
#'C:/TQS/CEA/Mississipi/CEA-MISSISSIPI'