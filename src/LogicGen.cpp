# include <iostream>
#include "LogicGen.h"
#include "Estudiante.h"
#include "ListDC.h"
#include "ListDoble.h"
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
ListDoble *nwListLine = new ListDoble();
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
    const regex pattern("([12]\\d{3}/(0[7-9]|1[01])/(0[1-9]|[12]\\d|3[0]))");
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
    bool vhora = true;
    bool vmes = true;
    bool vdia = true;

    if(!exist){
        cout<<"Error Estudiante No Registrado  "<<endl;
         descripError += "- Estudiante No Registrado";
    }
    if(!valFormat){
        cout<<"Error de Formato fecha: " << fecha_ <<endl;
        descripError += "- Herror en el Formato de fecha";
    }
    if( hora_ < 8 && hora_ > 16){
        vhora = false;
        descripError += "- Herror en el rango de Horas";
    }
    if( dia_ <= 0 && dia_ >= 31){
        descripError += "- Herror en el rango de Dias";
        vdia = false;
    }
    if( mes_ < 7 && mes_ > 11){
        descripError += "- Herror en el rango de Meses";
        vmes = false;
    }
    if(exist && valFormat && vhora && vmes && vdia){
        Tarea *nwTarea = new Tarea(contador,carnetU_, nombre_,descripcion_, materia_,fecha_, hora_,estado_);
        NodoDoble *nwNodoT = new NodoDoble(nwTarea);
        //cout<< "mes "<<to_string(mes_-7)<< "dia "<<to_string(dia_-1)<< "mes "<<to_string(hora_-8)<< endl;

        matrix[mes_-7][dia_-1][hora_ - 8] = nwNodoT;

        contador++;
        delete nwTarea;
    }else{
        Tarea *nwTarea = new Tarea(contador,carnetU_, nombre_,descripcion_, materia_,fecha_, hora_,estado_);
        NodoCola *nwError = new NodoCola(Nerror,descripError,"TAREA",nwTarea);
        nwColaErr->encolar(nwError);
        Nerror++;
        delete nwTarea;
    }
}

void linealizar(){
    for(int m = 0; m<5; m++){           // m mes
        for(int d = 0; d<30; d++){      // d dia
            for(int h = 0; h<9; h++){   // h hora

                NodoDoble *tmpNod = matrix[m][d][h];

                int indice = h+9*(d+30*m);
                if (tmpNod == NULL)
                {
                    cout<< "nodo vacio"<<endl;
                    NodoDoble *vacio = new NodoDoble();
                    vacio->setid(indice);
                    nwListLine->addNodo(vacio);
                    delete vacio;
                }else{
                    cout<< "nodo lleno"<<endl;
                    tmpNod->setid(indice);
                    nwListLine->addNodo(tmpNod);
                }
                delete tmpNod;
            }
        }
    }
}


void prtListLine(){
    nwListLine->getgraphList();
}

//------------------------------COLA DE ERRORES--------------------


void getgraphCola(){
nwColaErr->graficar();
}





/* cout<<to_string(mes_)<<endl;
    cout<<to_string(dia_)<<endl;
cout<<carnetU_<<endl;
cout<<nombre_<<endl;
cout<<descripcion_<<endl;
cout<<fecha_<<endl;
cout<<estado_<<endl;*/



