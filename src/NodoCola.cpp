#include "NodoCola.h"


NodoCola::NodoCola(){
    this->idError = NULL;
    this->tipo = nullptr;
    this->descripcion = nullptr;
    this->estudiante = NULL;
    this->tarea = NULL;
    this->next = NULL;
}
NodoCola::NodoCola(int idError_, string descript_, string tipo_,Estudiante *estudiante_,NodoCola *next_){
    this->idError = idError_;
    this->descripcion = descript_;
    this->tipo = tipo_;
    this->estudiante = estudiante_;
    this->tarea = NULL;
    this->next = next_;

}

NodoCola::NodoCola(int idError_, string descript_, string tipo_, Tarea *tarea_,NodoCola *next_){
    this->idError = idError_;
    this->descripcion = descript_;
    this->tipo = tipo_;
    this->estudiante = NULL;
    this->tarea = tarea_;
    this->next = next_;
}

void NodoCola::setnext(NodoCola *next_){
    this->next = next_;
}

void NodoCola::setidError(int id_){
    this->idError = id_;
}

void NodoCola::setdescript(string descript_)
{
    this->descripcion = descript_;
}

void NodoCola::setTipo(string tipo_){
    this->tipo = tipo_;
}

void NodoCola::setEstudiante(Estudiante *nStudent_){
    this->estudiante = nStudent_;
}

void NodoCola::setTarea(Tarea *nTarea_){
    this->tarea = nTarea_;
}

int NodoCola::getidError(){
    return this->idError;
}

string NodoCola::getdescript(){
    return this->descripcion;
}

string NodoCola::getTipo(){
    return this->tipo;
}

Estudiante *NodoCola::getEstudiante(){
    return this->estudiante;
}

Tarea *NodoCola::getTarea(){
    return this->tarea;
}

NodoCola *NodoCola::getNext(){
    return this -> next;
}
