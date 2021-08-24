#include "LogicGen.h"
#include "Estudiante.h"
#include "ListDC.h"
#include "windows.h"
#include "NodoCola.h"
#include "ColaErr.h"
#include <regex>

ListDC *nwListDC = new ListDC();
ColaErr *nwColaErr = new ColaErr();

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
    int Nerror = 1;
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

       // nwListDC->printlist();
    }else{
        //Estudiante *nEstudiante = new Estudiante(carnet_,dpi_,nombre_,carrera_,email_,pass_,creditos_, edad_);
         //cout<<"crea el estudiante "<< endl;
        //NodoCola *newNodo = new NodoCola(Nerror,report,"Estudiante", nEstudiante ,NULL);
       // cout<<"crea el nodo "<< endl;
       // nwColaErr->encolar(newNodo);
       // cout<<"encola el nodo "<< endl;
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
