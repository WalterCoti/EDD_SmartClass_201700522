#include "Fecha.h"
#include <string>
using namespace std;
Fecha::Fecha(string dia_,string mes_, string anio_){
        this->dia = dia_;
        this->mes = mes_;
        this->anio = anio_;
}
Fecha::Fecha(){
    this->dia = nullptr;
    this->mes = nullptr;
    this->anio = nullptr;
}

        //getters
string Fecha::getdia(){
    return this->dia;
}
string Fecha::getmes(){
    return  this->mes;
}
string Fecha::getanio(){
    return this->anio;
}

string Fecha::getnewFormat(){
    string newdate = this->dia + "/" + this->mes + "/" + this->anio;
    return  newdate;
}

        //setters
void Fecha::setdia(string dia_){
    this->dia = dia_;
}
void Fecha::setmes(string mes_){
    this->mes = mes_;
}
void Fecha::setanio(string anio_){
    this->anio = anio_;
}

