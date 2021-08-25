#include "Tarea.h"
#include "Fecha.h"

using namespace std;

Tarea::Tarea(int idtarea_, string carn_tar_, string name_t_, string descript_, string materia_, string fecha_, int hora_,string estado_){
    this->idtarea = idtarea_;
    this->carn_tar = carn_tar_;
    this->name_t = name_t_;
    this->descript = descript_;
    this->materia = materia_;
    this->fechatar = fecha_;
    this->hora = hora_;
    this->estado = estado_;
}


void Tarea::setidtarea(int id_)
{
    this->idtarea = id_;
}

void Tarea::setcarnet(string carnet_)
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

void Tarea::setfecha(string fechatar_){
    this->fechatar = fechatar_;
}

void Tarea::sethora(int hora_){
    this->hora = hora_;
}

void Tarea::setestado(string estado_){
    this->estado = estado_;
}

int Tarea::getidtarea(){
    return this -> idtarea;
}

string Tarea::getcarnet(){
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

string Tarea::getfechatar(){
    this->fechatar;
}

int Tarea::gethora(){
    this -> hora;
}

string Tarea::getestado(){
    return estado;
}
