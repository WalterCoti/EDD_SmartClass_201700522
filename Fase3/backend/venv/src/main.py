from Estructuras.arboles.avlTree import AVLTree
from Estructuras.Listas.List_Cursos import Lista_cursos
from Estructuras.otrasestruct.grafo_curso import grafo

import hashlib
import json
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

currentAVL = AVLTree()
listCursos = Lista_cursos()


#======================================================ENCRIPTACION======================================================

def getkeyencript(password_):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=b'123',iterations=100000,)
    keyh = base64.urlsafe_b64encode(kdf.derive(password_.encode()))
    return keyh.decode()

#string a string
def encriptar(key_,token_str):
    fkey = Fernet(key_.encode())
    token = fkey.encrypt(token_str.encode())
    return token.decode()

def desencriptar(key_,token_):
    fkey = Fernet(key_.encode())
    desen = fkey.decrypt(token_.encode())
    return desen.decode()

#encriptar sha256
def encriptsha(cadena_):
    tmpencrip = str(hashlib.sha256(bytes(cadena_,'utf-8')).hexdigest())
    return tmpencrip



#======================================================ADMIN======================================================
# ------------------------ CARGA MASIVA -----------------------------
def readJsonFile(filename):
    f = open(filename, 'r',encoding="utf-8")
    dataread = json.loads(f.read())
    return dataread

# ESTUDIANTES

def carga_estudiantes(phatFile_,passKey_):
    key = getkeyencript(passKey_)
    datafile = readJsonFile(phatFile_)
    for student in datafile['estudiantes']:
        carnet = student['carnet']
        dpi = encriptar(key,str(student['DPI']))
        nombre = encriptar(key,student['nombre'])
        carrera = key,student['carrera']
        correo = encriptar(key,student['correo'])
        passwr = encriptsha(student['password'])
        edad= encriptar(key,str(student['edad']))
        #encriptacion sha256
        currentAVL.insert(carnet,dpi,nombre,carrera,correo,passwr,0,edad)
        

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

def carga_cursos(phatFile_):
    estudiante = False
    f = open(phatFile_, 'r',encoding="utf-8")
    dataread = json.loads(f.read())

    for line in dataread:
        if 'Estudiantes' in line:
            estudiante = True
            break
    if estudiante:
        for current in dataread['Estudiantes']:
            carnet = current['Carnet']
            for years in current['Años']:
                anio = years['Año']
                for semester in years['Semestres']:
                    semestre_ = semester['Semestre']
                    for curses in semester['Cursos']:
                        codigo_ = curses['Codigo']
                        nombre_ = curses['Nombre']
                        creditos_ = curses['Creditos']
                        prerequisitos_ = curses['Prerequisitos']
                        obligatorio_ = curses['Obligatorio']
                        addCursoEstudiante(carnet,int(anio),int(semestre_),int(codigo_),nombre_,int(creditos_),prerequisitos_,obligatorio_)
    else:
         
        for curses in dataread['Cursos']:
            codigo_ = curses['Codigo']
            nombre_ = curses['Nombre']
            creditos_ = curses['Creditos']
            prerequisitos_ = curses['Prerequisitos']
            obligatorio_ = curses['Obligatorio']
            listCursos.addCurso(codigo_,nombre_,creditos_,prerequisitos_,obligatorio_)
# ============================== ADD CURSO PENSUM/ ESTUDIANTE ===============================
def addCursoEstudiante(carnet_,anio_,semestre_,codigo_,nombre_,creditos_,prerequisitos_,obligatorio_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        estudiante.yearlist.add_Curso(anio_,semestre_,codigo_, nombre_,creditos_,prerequisitos_,obligatorio_)
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")
        

def addCursoPensum():
    listCursos
#======================================================USUARIO======================================================

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

    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(getDatoFecha(fecha_, "y"))
        if year:
            mes = year.mes.getMes(getDatoFecha(fecha_, "m"))
            if mes:
                nodoMatrix = mes.tareas.existeNod(getDatoFecha(fecha_, "d"), getHora(hora_))
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

def graph_BTreeStudent(carnet_, year_, semestre_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz,carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(year_)
        if year:
            semester = year.semestre.getSemestre(semestre_)
            if  semester:
                treeBCurses = semester.cursos
                treeBCurses.graficar()
            else:
               print("semestre \"" + str(semester.semestre) + "\" no registrado") 
        else:
            print("año \"" + str(year) + "\" no registrado")
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")


def graph_BTreePensum():
    pass

def damegrafo(codigo_curso):
    nwGrafo = grafo()
    nwGrafo.getgrafo(codigo_curso,listCursos)
    nwGrafo.graficarGrafo()




