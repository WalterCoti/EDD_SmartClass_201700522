from flask import Flask, request, jsonify
import main
app = Flask(__name__)


#----------------------------------------------CARGA MASIVA----------------------------------------------
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
        main.openfile(nwpath)
        return jsonify(notificacion="si pasa aqui")
    elif tipo_Carga == "recordatorio":
        return jsonify({"notification":"Tipo de carga recordatorio"})
    elif tipo_Carga == "curso":
        return jsonify({"notification": "Tipo de carga Cursos"})
    else:
        return jsonify({"notification":"Tipo de carga no definido"})

#---------------------------------------------- REPORTES ----------------------------------------------
@app.route('/reporte', methods=['GET'])
def reportes():
    reportN = request.get_json(force=True)
    typereport = reportN['tipo']
    if typereport == 0:
        main.currentAVL.generarGraph()      #genera grafica AVL
    elif typereport == 1:
        main.graph_Matrix(reportN['carnet'],reportN['año'],reportN['mes'])
    elif typereport == 2:
        main.graph_List_Task(reportN['carnet'],reportN['año'],reportN['mes'],reportN['dia'],reportN['hora'])
    # nNodo = NodoTask(1345,"Prueba1","prueba descripcion 1","Materia 1","12/5/2021","8:00","Finalizado")
    elif typereport == 3:
        pass
    elif typereport == 4:
        pass
    else:
        return jsonify({"notification":"Tipo de reporte no definido"})
    return jsonify(Grafica="Grafica generada exitosamente")


#----------------------------------------------CRUD ESTUDIANTE----------------------------------------------

@app.route('/estudiante', methods=['POST'])
def set_student():
    nw_std = request.get_json(force=True)
    main.Crear_Estudiante(nw_std['carnet'], nw_std['DPI'], nw_std['nombre'], nw_std['carrera'], nw_std['correo'], nw_std['password'], int(nw_std['creditos']), int(nw_std['edad']))
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

#----------------------------------------------CRUD RECORDATORIO----------------------------------------------
@app.route('/recordatorios', methods=['POST'])
def crear_Recordatorio():
    rec = request.get_json(force=True)
    main.create_Task(rec['Carnet'], rec['Nombre'], rec['Descripcion'], rec['Materia'], rec['Fecha'], rec['Hora'], rec['Estado'])
    return jsonify(Recordatorio="Creado exitosamente")

@app.route('/recordatorios', methods=['PUT'])
def editar_Recordatorio():
    editRec = request.get_json(force=True)
    main.update_Task(editRec['Carnet'], editRec['Nombre'], editRec['Descripcion'], editRec['Materia'], editRec['Fecha'], editRec['Hora'], editRec['Estado'],editRec['Posicion'])
    return jsonify(Recordatorio="Editado exitosamente")

@app.route('/recordatorios', methods=['GET'])
def info_Recordatorio():
    infoTask = request.get_json(force=True)
    Task_N = main.info_Task(infoTask['Carnet'],infoTask['Fecha'],infoTask['Hora'],infoTask['Posicion'])
    return jsonify(carnet=Task_N.carnet, Nombre=Task_N.name_task, Descripcion=Task_N.desc_task, Materia=Task_N.materia, Fecha=Task_N.fecha, Hora=Task_N.hora, Estado=Task_N.estado)

@app.route('/recordatorios', methods=['DELETE'])
def delete_Recordatorio():
    delTask = request.get_json(force=True)
    main.info_Task(delTask['Carnet'], delTask['Fecha'], delTask['Hora'], delTask['Posicion'])
    return jsonify(Eliminado="Recordatorio Eliminado")

#----------------------------------------------CARGA MASIVA CURSOS----------------------------------------------


if __name__ == "__main__":
    app.run("localhost", port=3000)
