#include "readfile.h"
#include <string>

#include <fstream>
#include <sstream>
#include <iostream>
#include "windows.h"
#include "LogicGen.h"
#include <regex>


using namespace std;

void readfileStudent(string path_){
    string text = "";
    string head = "";
    string carnet,dpi,name,carrera,email,pass,credit, edad;
    ifstream fileOp(path_);

    if(!fileOp.is_open()){
        cout << "ERROR: Archivo no pudo ser abierto" << endl;
    }
    getline(fileOp, head,'\n');
    while(fileOp.good()){
        getline(fileOp,carnet,',');
        getline(fileOp,dpi,',');
        getline(fileOp,name,',');
        getline(fileOp,carrera,',');
        getline(fileOp,pass,',');
        getline(fileOp,credit,',');
        getline(fileOp,edad,',');
        getline(fileOp,email,'\n');
        valStudent(carnet,dpi,name,carrera,email,pass,stoi(credit),stoi(edad));
    }
}

void readfileTarea(string path_){
    string text = "";
    string head = "";
    string mes,dia,hora,carnet,Nombre,descripcion,materia, fechatar,estado;
    ifstream fileOp(path_);

    if(!fileOp.is_open()){
        cout << "ERROR: Archivo no pudo ser abierto" << endl;
    }
    getline(fileOp, head,'\n');
    while(fileOp.good()){
        getline(fileOp,mes,',');
        getline(fileOp,dia,',');
        getline(fileOp,hora,',');
        getline(fileOp,carnet,',');
        getline(fileOp,Nombre,',');
        getline(fileOp,descripcion,',');
        getline(fileOp,fechatar,',');
        getline(fileOp,estado,'\n');
       // valStudent(carnet,dpi,name,carrera,email,pass,stoi(credit),stoi(edad));
    }
}
