#include "Tarea.h"
#include "Fecha.h"
using namespace std;
Tarea::Tarea(int idtarea_, int carn_tar_, string name_t_, string descript_, string materia_, Fecha *fechatar_, int hora_){
    this->idtarea = idtarea_;
    this->carn_tar = carn_tar_;
    this->name_t = name_t_;
    this->descript = descript_;
    this->materia = materia_;
    this->fechatar = fechatar_;
    this->hora = hora_;
}


void Tarea::setidtarea(int id_)
{
    this->idtarea = id_;
}

void Tarea::setcarnet(int carnet_)
{
    this-> carn_tar = carnet_;
}

void Tarea::setnamet(string name_t_)
{
    this -> name_t = name_t_;
}
void Tarea::setdescri(string descript_)
{
    this-> descript = descript_;
}

void Tarea::setmateria(string materia_){
    this->materia = materia_;
}

void Tarea::setfecha(Fecha *fechatar_){
    this->fechatar = fechatar_;
}

void Tarea::sethora(int hora_){
    this->hora = hora_;
}

int Tarea::getidtarea(){
    return this -> idtarea;
}

int Tarea::getcarnet(){
    return this->carn_tar;
}

string Tarea::getname_t(){
    return this->name_t;
}

string Tarea::getdescript(){
    return this->descript;
}

string Tarea::getmateria(){
    this -> materia;
}

Fecha *Tarea::getfechatar(){
    this->fechatar;
}

int Tarea::gethora(){
    this -> hora;
}


