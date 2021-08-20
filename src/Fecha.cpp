#include "Fecha.h"
#include <string>
using namespace std;
Fecha::Fecha(int dia_,int mes_, int anio_){
        this->dia = dia_;
        this->mes = mes_;
        this->anio = anio_;
}

        //getters
int Fecha::getdia(){
    return this->dia;
}
int Fecha::getmes(){
    return  this->mes;
}
int Fecha::getanio(){
    return this->anio;
}

string Fecha::getnewFormat(){
    string newdate = to_string(this->dia) + "/" + to_string(this->mes) + "/" + to_string(this->anio);
    return  newdate;
}


        //setters
void Fecha::setdia(int dia_){
    this->dia = dia_;
}
void Fecha::setmes(int mes_){
    this->mes = mes_;
}
void Fecha::setanio(int anio_){
    this->anio = anio_;
}

