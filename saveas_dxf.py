from TQS import TQSDwg

dwgPath = r'C:\Users\gusta\OneDrive\repos\brgtrepos\Python\tqs_python\DesFiad1'

dwg = TQSDwg.Dwg()
if dwg.file.Open (dwgPath) != 0:
    print("Não abri o arquivo [%s] para leitura" % dwgPath)
elif dwg.file.Open (dwgPath) == 0:
    print("Abri o arquivo [%s] para leitura" % dwgPath)

dwg.file.SaveAs(r'C:\Users\gusta\OneDrive\repos\brgtrepos\Python\tqs_python\DesFiad1.DXF')
dwg.file.Close()