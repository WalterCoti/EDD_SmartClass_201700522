#include "Estudiante.h"
#include <ctype.h>

Estudiante::Estudiante(string carnet_,string dpi_, string name_, string carrera_, string email_, string pass_, int credit_, int edad_)
{
    carnet = carnet_;
    dpi = dpi_;
    name = name_;
    carrera = carrera_;
    email = email_;
    pass = pass_;
    credit = credit_;
    edad = edad_;

}
//setters
void Estudiante::setcarnet(string carnet_){
    this->carnet =carnet_;
}

void Estudiante::setdpi(string dpi_){
    this->dpi =dpi_;
}

void Estudiante::setname(string name_){
    this->name = name_;
}

void Estudiante::setcarrera(string carrera_){
    this->carrera = carrera_;
}

void Estudiante::setemail(string email_){
    this->email = email_;
}

void Estudiante::setcredit(int credit_){
    this->credit = credit_;
}
void Estudiante::setedad(int edad_){
    this->edad = edad_;
}

//getters
string Estudiante::getcarnet(){
    return this->carnet;
}

string Estudiante::getdpi()
{
    return this->dpi;
}

string Estudiante::getname()
{
    return this->name;
}

string Estudiante::getcarrera(){
    return this->carrera;
}

string Estudiante::getemail(){
    return this->email;
}

string Estudiante::getpass(){
    return this->pass;
}

int Estudiante::getcredit(){
    return this->credit;
}

int Estudiante::getedad(){
    return this->edad;
}
