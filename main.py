from Estructuras.avlTree import AVLTree
from analizador.Syntactic import parser
from analizador.Syntactic import user_list,task_list
from Estructuras.NodoTask import NodoTask
import Estructuras

currentAVL = AVLTree()
# ------------------------ CARGA MASIVA -----------------------------
def openfile(pathFile_):
    #try:
        f = open(pathFile_, 'r',encoding="utf-8")
        data_File = f.read()
        f.close()
        parser.parse(data_File)
        realizarCarga()
   # except:
       # print("Error al leer el archivo")

def realizarCarga():
    nlst = user_list.getList()
    while nlst is not None:
        currentAVL.insert(nlst.Carnet,nlst.DPI,nlst.Nombre,nlst.Carrera,nlst.Correo,nlst.Password,nlst.Creditos,nlst.Edad)
        nlst = nlst.Next
    tasklst = task_list.getList()
    while tasklst is not None:
        nwtask = NodoTask(tasklst.Carnet,tasklst.Nombre,tasklst.Descripcion,tasklst.Materia,tasklst.Fecha,tasklst.Hora,tasklst.Estado)
        currentAVL.add_task_listyear(tasklst.Carnet,nwtask,getDatoFecha(tasklst.Fecha,"y"),getDatoFecha(tasklst.Fecha,"m"),getDatoFecha(tasklst.Fecha,"d"),getHora(tasklst.Hora))
        tasklst = tasklst.Next

def getDatoFecha(Fecha, dato_):
    DateSpl = Fecha.split("/")
    if dato_ == "d":
        return  int(DateSpl[0])
    elif dato_ == "m":
        return int(DateSpl[1])
    elif dato_ =="y":
        return int(DateSpl[2])

def getHora(Hora):
    horacl = Hora.split(":")
    return int(horacl[0])

#-------------------------CRUD ESTUDIANTES----------------------------

# ------------------------CRUD TAREAS --------------------------------

# ------------------------ REPORTES -------------------------------
def graph_List_Task(carnet_, year_, mes_,dia_, hora_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz,carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(year_)
        if year:
            mes = year.mes.getMes(mes_)
            if  mes:
                nodoMatrix = mes.tareas.existeNod(dia_, hora_)
                if nodoMatrix:
                    lstTask = nodoMatrix.lstTareas
                    lstTask.graficar()
                else:
                    print("Nodo no existe existe ")
        else:
            print("año \"" + str(year) + "\" no registrado")
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")

def graph_Matrix(carnet_, year_, mes_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(year_)
        if year:
            mes = year.mes.getMes(mes_)
            if mes:
                mes.tareas.graficarMatriz()
            else:
                print("Mes \"" + str(mes_) + "\" no registrado")
        else:
            print("Año \"" + str(year) + "\" no registrado")
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")

def graph_BTree():
    pass

#
# strin = "09"
# numerito = int(strin)
# print(numerito)