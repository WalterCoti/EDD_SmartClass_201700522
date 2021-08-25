# include <iostream>
#include "LogicGen.h"
#include "Estudiante.h"
#include "ListDC.h"
#include "windows.h"
#include "NodoCola.h"
#include "NodoDoble.h"
#include "ColaErr.h"
#include "Tarea.h"
#include <regex>
#include <istream>

using namespace std;
//-------------------------------INICIALIZACION DE VARIABLES---------------
ListDC *nwListDC = new ListDC();
ColaErr *nwColaErr = new ColaErr();
int contador=0;
int Nerror = 1;

NodoDoble *matrix[5][30][9];
//--------------------------------THE MATRIX------------------------------
void initMatrix(){
    for(int i = 0; i<5; i++){
        for(int j = 0; j<30; j++){
            for(int k = 0; k<9; k++){
                matrix[i][j][k] = NULL;
            }
        }
    }
}



//--------------------------------- ESTUDIANTES-----------------------------------

bool isemail(string email_){
    //cout <<"email que llega -> " << email_ << endl;
    const regex pattern("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+");
    return regex_match(email_,pattern);
}

bool isdpi(string numdpi_){
    //cout<<"tamaño de dpi -> " << numdpi_.length()<< endl;
    if(numdpi_.length() == 13){
        return true;
    }return false;
}


bool iscarnet(string numcarnet_)
{
    //cout<<"tamaño de carnet -> " << numcarnet_.length()<< endl;
    if(numcarnet_.length() == 9){
        return true;
    }return false;
}

void valStudent(string carnet_,string dpi_,string nombre_, string carrera_,string email_,string pass_, int creditos_,int edad_)
{

    string report = "";

    if(!iscarnet(carnet_))
    {
        report += " -Error de carnet";
        cout<<"- Error carnet: " << carnet_ << endl;
    };
    if(!isdpi(dpi_))
    {
        report += " -Error de dpi";
         cout<<"- Error dpi: " << dpi_ << endl;
    };
    if(!isemail(email_))
    {
        report += " -Error de correo";
         cout<<"- Error correo: " << email_  << endl;
    };
    if(iscarnet(carnet_) && isdpi(dpi_) && isemail(email_)){
        Estudiante *nEstudiante = new Estudiante(carnet_,dpi_,nombre_,carrera_,email_,pass_,creditos_, edad_);
        nwListDC->addEstudent(nEstudiante);

    }else{
        Estudiante *nEstudiante = new Estudiante(carnet_,dpi_,nombre_,carrera_,email_,pass_,creditos_, edad_);
        NodoCola *newNodo = new NodoCola(Nerror,report,"Estudiante", nEstudiante);
        nwColaErr->encolar(newNodo);
        Nerror++;
    }


}

void delStudent(string dpi_){
    nwListDC->deletStudent(dpi_);

}

void updateStudent(string dato,int valor){
}

void printStu(){
   nwListDC->graphListDC();
}


//--------------------------------------------TAREAS-----------------------------------------------------------
bool isValDate(string fecha_){
    const regex pattern("([12]\\d{3}/(0?[7-9]|1[0-1])/(0[1-9]|[12]\\d|3[0]))");
    return regex_match(fecha_,pattern);
}


string dameDate(string fecha_, int type_){
    string anio, mes, dia;
    istringstream inputdate;
    inputdate.str(fecha_);
    getline(inputdate, anio, '/');
    getline(inputdate, mes, '/');
    getline(inputdate, dia, '/');
    if(type_ == 1){
        //cout<< anio << endl;
        return anio;
    }else if(type_ == 2){
        //cout<< mes << endl;
        return mes;
    }else{
        //cout<< dia << endl;
        return dia;
    }
}


void valTarea(int mes_, int dia_,int hora_, string carnetU_,string nombre_,string descripcion_, string materia_, string fecha_,  string estado_){
    string descripError = "";
    bool exist = nwListDC->existEst(carnetU_);
    bool valFormat = isValDate(fecha_);


    if(valFormat){
        descripError += "- Herror en el Formato de fecha";
    }
    if( hora_ < 8 && hora_ > 16){
        descripError += "- Herror en el rando de Horas";
    }
    if( dia_ <= 0 && dia_ >= 31){
        descripError += "- Herror en el rando de Dias";
    }
    if( mes_ < 7 && mes_ > 11){
        descripError += "- Herror en el rando de Meses";
    }
    if(exist && valFormat ){

        Tarea *nwTarea = new Tarea(contador,carnetU_, nombre_,descripcion_, materia_,fecha_, hora_,estado_);
        NodoDoble *nwNodoT = new NodoDoble(nwTarea);
        matrix[mes_][dia_][hora_] = nwNodoT;
        contador++;
    }

}


void linealizar(){

}

//------------------------------COLA DE ERRORES--------------------


void getgraphCola(){
nwColaErr->graficar();
}









