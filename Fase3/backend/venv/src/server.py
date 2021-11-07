from flask import Flask, request, jsonify
import main
app = Flask(__name__)

#======================================================ADMIN======================================================
#----------------------------------------------CARGA MASIVA, estudiantes, notas----------------------------------------------
@app.errorhandler(500)
def handle_500(e):
    return jsonify(error=str(e)), 500

@app.route('/carga', methods = ['POST'])
def masiveStudent():
    infofile = request.get_json(force=True)
    tipo_Carga = infofile['tipo']
    pathFile = infofile['path']
    nwpath = pathFile.replace('\\', '\\\\')
    if tipo_Carga == "estudiante":
        passwEncri = infofile['passenc']
        main.carga_estudiantes(nwpath,passwEncri)
        return jsonify(notificacion="Datos Cargados a memoria")
    elif tipo_Carga == "nota":
        main.cargarapunte(nwpath)
        return jsonify({"notification":"Tipo de carga recordatorio"})
    elif tipo_Carga == "curso":
        main.carga_cursos(nwpath)
        return jsonify({"notification": "Tipo de carga Cursos"})
    else:
        return jsonify({"notification":"Tipo de carga no definido"})

#---------------------------------------------- REPORTES ----------------------------------------------
@app.route('/reporte', methods=['GET'])
def reportes():
    reportN = request.get_json(force=True)
    typereport = reportN['tipo']
    if typereport == 0:
        encript = reportN['desencriptar']
        passkey = reportN['passwkey']
        main.currentAVL.generarGraph(encript,passkey)      #genera grafica AVL
        return jsonify(Estudiante="Avl Estudiantes")
    elif typereport == 1:
        main.grafopensum()
        return jsonify(Estudiante="Grafo de pensum creado exitosamente")
    elif typereport == 2:
        main.tabnotas.graficarTabla()
        return jsonify({"Reporte Tabla Hash":"Reporte Creado exitosamente"})
    else:
        return jsonify({"notification":"Tipo de reporte no definido"})
   


#----------------------------------------------CRUD ESTUDIANTE----------------------------------------------

@app.route('/registro', methods=['POST'])
def set_student():
    nw_std = request.get_json(force=True)
    main.Crear_Estudiante(nw_std['carnet'], nw_std['DPI'], nw_std['nombre'], nw_std['carrera'], nw_std['correo'], nw_std['password'], int(nw_std['edad']))
    return jsonify(Estudiante="Creado exitosamente")

@app.route('/estudiante', methods=['PUT'])
def edit_Estudent():
    editSTD = request.get_json(force=True)
    main.editar_Estudiante(editSTD['carnet'], editSTD['DPI'], editSTD['nombre'], editSTD['carrera'], editSTD['correo'], editSTD['password'], int(editSTD['creditos']), int(editSTD['edad']))
    return jsonify(Estudiante="Editado exitosamente")

@app.route('/estudiante', methods=['GET'])
def verStudent():
    editSTD = request.get_json(force=True)
    std = main.verStudent(editSTD['carnet'])
    return jsonify(carnet=std.carnet,dpi = std.dpi, nombre=std.nombre, carrera = std.carrera, correo = std.correo, password = std.passw, creditos = std.credito, edad= std.edad )

@app.route('/estudiante', methods=['DELETE'])
def Delete_Student():
    delStudent = request.get_json(force=True)
    main.currentAVL.delete(delStudent['carnet'])
    return jsonify(Estudiante="Eliminado exitosamente")


#======================================================USUARIO======================================================
@app.route('/Anotacion', methods=['POST'])
def crearnota():
    data = request.get_json(force=True)
    carnet = data['carnet']
    titulo = data['titulo']
    content = data['contenido']
    main.addNota_User(carnet,titulo, content)
    return jsonify("Nota agregada con exito")
    

@app.route('/vernotas', methods=['GET'])
def verAnotaciones():
    data = request.get_json(force=True)
    carnet = data['carnet']
    main.vernotas(carnet)
    return jsonify("Anotaciones")


@app.route('/asignaciones', methods=['POST'])
def addcurso():
    dataread = request.get_json(force=True)
    carnet = dataread['carnet']
    year = dataread['anio']
    semestre = dataread['semestre']
    codigo = dataread['codigo']
    main.addCursoaEstudiante(carnet,year,semestre,codigo)
    return jsonify(Estudiante="Curso " + str(codigo) + " asignado correctamente")

@app.route('/prev_cursos', methods=['GET'])
def grafopensum():
    graficar = request.get_json(force=True)
    codigocurso = graficar['codigo']
    main.damegrafo(codigocurso)
    return jsonify(Estudiante="Grafo para el curso " + str(codigocurso) + " creado exitosamente")
    
@app.route('/cursosasignados', methods=['GET'])
def cur_asign():
    dataread = request.get_json(force=True)
    carnet = dataread['carnet']
    year = dataread['anio']
    semestre = dataread['semestre']
    main.graph_cursos_std(int(carnet),int(year), int(semestre))
    return jsonify(Estudiante="Grafica cursos asignados " + str(carnet) + " creado exitosamente")


if __name__ == "__main__":
    app.run("localhost", port=3000)