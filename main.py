import main
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
def Crear_Estudiante(carnet_,DPI_,nombre_,carrera_,correo_,pass_,creditos_,edad_):
    currentAVL.insert(carnet_,DPI_,nombre_,carrera_,correo_,pass_,creditos_,edad_)


def editar_Estudiante(carnet_,DPI_,nombre_,carrera_,correo_,pass_,creditos_,edad_):
    tmPNodo = currentAVL.getStudentNode(currentAVL.raiz,carnet_)
    if tmPNodo:
        tmPNodo.carnet = carnet_
        tmPNodo.dpi = DPI_
        tmPNodo.nombre = nombre_
        tmPNodo.carrera = carrera_
        tmPNodo.correo = correo_
        tmPNodo.passw = pass_
        tmPNodo.credito =creditos_
        tmPNodo.edad = edad_
    else:
        currentAVL.insert(carnet_,DPI_,nombre_,carrera_,correo_,pass_,creditos_,edad_)


def verStudent(carnet_):
    STDtmp = currentAVL.getStudentNode(currentAVL.raiz,carnet_)
    return STDtmp
# ------------------------CRUD TAREAS --------------------------------
def create_Task(carnet_,nombre_,descripcion_,materia_ , fecha_, hora_, estado_):
    nwNodo = NodoTask(carnet_,nombre_,descripcion_,materia_ , fecha_, hora_, estado_)
    currentAVL.add_task_listyear(carnet_,nwNodo,getDatoFecha(fecha_,"y"),getDatoFecha(fecha_,"m"),getDatoFecha(fecha_,"d"),hora_)

def info_Task(carnet_,fecha_, hora_,posicion_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(getDatoFecha(fecha_,"y"))
        if year:
            mes = year.mes.getMes(getDatoFecha(fecha_,"m"))
            if mes:
                nodoMatrix = mes.tareas.existeNod(getDatoFecha(fecha_,"d"), hora_)
                if nodoMatrix:
                    lstTask = nodoMatrix.lstTareas
                    return lstTask.getinfo(posicion_)
    return None

def update_Task(carnet_,nombre_,descripcion_,materia_ , fecha_, hora_, estado_,posicion_):
    nwNodo = NodoTask(carnet_, nombre_, descripcion_, materia_, fecha_, hora_, estado_)
    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(getDatoFecha(fecha_,"y"))
        if year:
            mes = year.mes.getMes(getDatoFecha(fecha_,"m"))
            if mes:
                nodoMatrix = mes.tareas.existeNod(getDatoFecha(fecha_,"d"), hora_)
                if nodoMatrix:
                    lstTask = nodoMatrix.lstTareas
                    lstTask.updateTask(nwNodo,posicion_)
                else:
                    print("Nodo no existe")
        else:
            print("año \"" + str(year) + "\" no registrado")
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")

def delete_Task(carnet_,fecha_, hora_,posicion_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(getDatoFecha(fecha_, "y"))
        if year:
            mes = year.mes.getMes(getDatoFecha(fecha_, "m"))
            if mes:
                nodoMatrix = mes.tareas.existeNod(getDatoFecha(fecha_, "d"), hora_)
                if nodoMatrix:
                    lstTask = nodoMatrix.lstTareas
                    lstTask.deleteTask(posicion_)
                else:
                    print("Nodo no existe")
        else:
            print("año \"" + str(year) + "\" no registrado")
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")


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
                    print("Nodo no existe")
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
