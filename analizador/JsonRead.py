import json
def openJson(pathFile_):
    try:
        f = open(pathFile_, 'r', encoding="utf-8")
        data_File = f.read()
        f.close()
    except:
        print("Error al leer el archivo")