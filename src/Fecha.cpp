#include "Fecha.h"

Fecha::Fecha(int dia_,int mes_, int anio_){
        this->dia = dia_;
        this->mes = mes_;
        this->anio = anio_;
}

        //setters
int Fecha::getdia(){
    return this->dia;
}
int Fecha::getmes(){
    return  this->mes;
}
int Fecha::getanio(){
    return this->anio;
}

        //getters
void Fecha::setdia(int dia_){
    this->dia = dia_;
}
void Fecha::setmes(int mes_){
    this->mes = mes_;
}
void Fecha::setanio(int anio_){
    this->anio = anio_;
}

