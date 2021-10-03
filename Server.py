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


#----------------------------------------------CRUD ESTUDIANTE----------------------------------------------

@app.route('/estudiante', methods=['POST'])
def set_student():
    student = request.get_json(force=True)
    print(student['carnet'])
    print(student['DPI'])
    return jsonify({"finalizado":"fin del mensaje cargado"})

#----------------------------------------------CRUD RECORDATORIO----------------------------------------------


#----------------------------------------------CARGA MASIVA----------------------------------------------

#----------------------------------------------CARGA MASIVA----------------------------------------------


if __name__ == "__main__":
    app.run("localhost", port=3000)
