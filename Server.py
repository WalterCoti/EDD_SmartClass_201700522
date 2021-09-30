from flask import Flask, request, jsonify
import main
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def get_hello():
    return jsonify("hola dios soy yo de nuevo ")

@app.route('/estudiante', methods=['POST'])
def set_student():
    student = request.get_json(force=True)
    print(student['carnet'])
    print(student['DPI'])
    return jsonify({"finalizado":"fin del mensaje cargado"})


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




if __name__ == "__main__":
    app.run("localhost", port=3000)
