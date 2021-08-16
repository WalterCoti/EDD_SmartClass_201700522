#include "NodoD.h"

NodoD::NodoD(Estudiante *estudiante_,NodoD *next_,NodoD *previous_)
{
    this->estudiante = estudiante_;
    this->next = next_;
    this->previous = previous_;
}
NodoD::NodoD(Estudiante *estudiante_)
{
    this->estudiante = estudiante_;
    this->next = NULL;
    this->previous = NULL;
}

NodoD::NodoD()
{
    this->estudiante = NULL;
    this->next = NULL;
    this->previous = NULL;
}

void NodoD::setnext(NodoD *next_)
{
    this->next = next_;
}

void NodoD::setprevius(NodoD *previous_)
{
    this->previous = previous_;
}

void NodoD::setestudiante(Estudiante *estudiante_)
{
    this->estudiante = estudiante_;
}

NodoD *NodoD::getnext()
{
    return this->previus;
}
NodoD *NodoD::getprevious()
{
    return previous;
}

Estudiante *NodoD::getEstudiante()
{
    return estudiante;
}
