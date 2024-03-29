from Estructuras.arboles.avlTree import AVLTree
from Estructuras.Listas.List_Cursos import Lista_cursos
from Estructuras.otrasestruct.grafo_curso import grafo
from Estructuras.TablaHash import HashTable

import hashlib
import json
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

currentAVL = AVLTree()
listCursos = Lista_cursos()
tabnotas = HashTable()
keyencript = ""


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
    global keyencript
    key = getkeyencript(passKey_)
    keyencript = passKey_
    print("keyglobal " + keyencript)
    datafile = readJsonFile(phatFile_)
    for student in datafile['estudiantes']:
        carnet = student['carnet']
        dpi = encriptar(key,str(student['dpi']))
        nombre = encriptar(key,student['nombre'])
        carrera = student['carrera']
        correo = encriptar(key,student['correo'])
        #encriptacion simetrica( encriptacion sha256)
        passwr = encriptar(key,encriptsha(student['password']))
        edad= encriptar(key,str(student['edad']))
        
        currentAVL.insert(int(carnet),dpi,nombre,carrera,correo,passwr,0,edad)
     
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
                        addCursoEstudiante(int(carnet),int(anio),int(semestre_),codigo_,nombre_,int(creditos_),prerequisitos_,obligatorio_)
    else:
        for curses in dataread['Cursos']:
            codigo_ = curses['Codigo']
            nombre_ = curses['Nombre']
            creditos_ = curses['Creditos']
            prerequisitos_ = curses['Prerequisitos']
            obligatorio_ = curses['Obligatorio']
            listCursos.addCurso(codigo_,nombre_,creditos_,prerequisitos_,obligatorio_)

def cargarapunte(phatFile_):
    datafile = readJsonFile(phatFile_)
    for usuario in datafile['usuarios']:
        carnet = usuario['carnet']
        for apunte in usuario['apuntes']:
            titulo = apunte['titulo']
            content = apunte['contenido']
            addNota_User(int(carnet),titulo,content)

#--------------------------------REPORTES------------------
def graphtaablehash():
    tabnotas.graficarTabla()

def grafopensum():
    nwGrafo = grafo()
    tmp = listCursos.head
    while tmp:
        nwGrafo.getgrafo(tmp.codigo,listCursos)
        tmp = tmp.sig
    nwGrafo.graficarGrafo()


#======================================================USUARIO======================================================
#--------------------------------NOTAS
def addNota_User(carnet_,titulo_,contenido_):
    tabnotas.addNota(carnet_, titulo_ ,contenido_)

def vernotas(carnet):
    lstnotas = tabnotas.getNotas(carnet)
    lstnotas.getListNotas()



#-------------------------CRUD ESTUDIANTES----------------------------
def Crear_Estudiante(carnet_,DPI_,nombre_,carrera_,correo_,pass_,edad_):
    global keyencript
    print(keyencript)
    nkey = getkeyencript(keyencript)
    dpi = encriptar(nkey,str(DPI_))
    nombre = encriptar(nkey,nombre_)
    correo = encriptar(nkey,correo_)
    pasw = encriptar(nkey,encriptsha(pass_))
    edad = encriptar(nkey,str(edad_))
    currentAVL.insert(int(carnet_),dpi,nombre,carrera_,correo,pasw,0,edad)

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

# ============================== ADD CURSO PENSUM/ ESTUDIANTE ===============================
def addCursoEstudiante(carnet_,anio_,semestre_,codigo_,nombre_,creditos_,prerequisitos_,obligatorio_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        estudiante.yearlist.add_Curso(anio_,semestre_,codigo_, nombre_,creditos_,prerequisitos_,obligatorio_)
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")
        

def addCursoaEstudiante(carnet_,year_,semestre_,codigo_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz, carnet_)
    if estudiante:
        infcurso = listCursos.getCurso(codigo_)
        if infcurso:
            nombre = infcurso.nombre
            creditos = infcurso.creditos
            prerequisitos = infcurso.pre_codigo
            obligatorio = infcurso.obligatorio
            estudiante.yearlist.add_Curso(year_,semestre_,codigo_, nombre,creditos,prerequisitos,obligatorio)
        else:
            print("Curso " + str(codigo_) + "no registrado")
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")
# ------------------------ REPORTES -------------------------------

def graph_cursos_std(carnet_, year_, semestre_):
    estudiante = currentAVL.getStudentNode(currentAVL.raiz,carnet_)
    if estudiante:
        year = estudiante.yearlist.getYear(year_)
        if year:
            semester = year.semestre.getSemestre(semestre_)
            if  semester:
                listaCursos = semester.cursos
                listaCursos.graficar()
            else:
               print("semestre \"" + str(semester.semestre) + "\" no registrado") 
        else:
            print("año \"" + str(year) + "\" no registrado")
    else:
        print("Estudiante \"" + str(carnet_) + "\" no registrado")


def damegrafo(codigo_curso):
    nwGrafo = grafo()
    nwGrafo.getgrafo(codigo_curso,listCursos)
    nwGrafo.graficarGrafo()



