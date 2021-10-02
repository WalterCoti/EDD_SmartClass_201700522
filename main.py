from Estructuras.avlTree import AVLTree
from analizador.Syntactic import parser
from analizador.Syntactic import user_list,task_list

currentAVL = AVLTree()

def openfile(pathFile_):
    try:
        f = open(pathFile_, 'r',encoding="utf-8")
        data_File = f.read()
        f.close()
        parser.parse(data_File)
        realizarCarga()
    except:
        print("Error al leer el archivo")

def realizarCarga():
    nlst = user_list.getList()
    while nlst is not None:
        currentAVL.insert(nlst.Carnet,nlst.DPI,nlst.Nombre,nlst.Carrera,nlst.Correo,nlst.Password,nlst.Creditos,nlst.Edad)
        nlst = nlst.Next
    tasklst = task_list.getList()
    while tasklst is not None:

        tasklst = tasklst.Next
    currentAVL.generarGraph()
