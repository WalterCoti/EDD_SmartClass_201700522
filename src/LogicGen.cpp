#include "LogicGen.h"
#include "Estudiante.h"
#include "ListDC.h"
#include "windows.h"
#include <regex>

ListDC *nwList = new ListDC();

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
        nwList->addEstudent(nEstudiante);
    }else{

        cout<<"Datos agregados  a la cola de errores" << endl;
    }


}

void delStudent(string dpi_){
    nwList->deletStudent(dpi_);
    nwList->printlist();
}

void updateStudent(string dato,int valor){
}

