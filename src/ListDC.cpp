#include "ListDC.h"
#include "Estudiante.h"
#include <fstream>
#include <windows.h>
#include <iostream>
#include <string>
#include <sstream>

ListDC::ListDC()
{
    this->head = NULL;
    this->end = NULL;
    this->size = 0;
    this->nfile = 0;
}

bool ListDC::isEmptyLCD()
{
    if(this->head == NULL){
        return true;
    }
    return false;
}

bool ListDC::existEst(string carnet_){
    NodoD *tmp = this->head;
    if(this->head == NULL){
        return false;
    }else{
        do{
            if(tmp->getEstudiante()->getcarnet() == carnet_){
                return true;
            }
            tmp = tmp->getnext();
        }while(tmp != this->head);
    }
}


void ListDC::addEstudent(Estudiante *estudiante_){
    NodoD *newNodo = new NodoD(estudiante_);
    if(isEmptyLCD()){
        this->head = newNodo;
        this->end = newNodo;
        newNodo->setnext(head);
        newNodo->setprevious(end);
    } else {
        this->end->setnext(newNodo);
        newNodo->setprevious(end);
        this->head->setprevious(newNodo);
        newNodo->setnext(head);
        this->end = newNodo;
    }
    this->size++;

}

void ListDC::updateStudent(string dpistudent_,int opc_)
{


}

void ListDC::deletStudent(string dpistudent_){
    NodoD *actual  = this->head;
    NodoD *anterior = NULL;
    bool nodoDel = false;
    if(isEmptyLCD()){
        cout << "Lista vacia" << endl;
    }else{
        do{
            if(actual->getEstudiante()->getcarnet() == dpistudent_){
                //obtener datos del que elimino xD
                if(actual == this->head){
                    this->head = this->head->getnext();
                    this->head->setprevious(this->end);
                    this->end->setnext(this->head);
                }else if(actual == this->end){
                    this->end = anterior;
                    this->end->setnext(this->head);
                    this->head->setprevious(this->end);
                }else{
                    anterior->setnext(actual->getnext());
                    actual->getnext()->setprevious(anterior);
                }
                nodoDel = true;
            }
            anterior = actual;
            actual = actual->getnext();

        }while(actual != this->head && nodoDel != true);

        if(!nodoDel){
            cout << " Usuario no registrado";
        }
    }
    delete actual;
    delete anterior;
}


void ListDC::printlist()
{
 NodoD *tmp = this->head;
 if(this->head != NULL){
 do{
    cout << "- " << tmp->getEstudiante()->getname() << endl;
    tmp = tmp->getnext();
 }while(tmp != this->head);
 } else{
    cout << "\n La lista  Vacia" << endl;
 }
}

void ListDC::graphListDC(){
    NodoD *aux = this->head;
    string n_data = "";
    string e_data = "";
    string graph = "digraph List {\nrankdir=LR;\nnode [shape = record, color=blue , style=filled, fillcolor=skyblue];\n";
    string n_actual;
    string n_sig;
    string n_anterior;
    do{
    //cout << aux->getEstudiante()->getname() << endl;
     n_actual = aux->getEstudiante()->getcarnet();
     n_sig =    aux->getnext()->getEstudiante()->getcarnet();
     n_anterior = aux->getprevious()->getEstudiante()->getcarnet();
     n_data +=  n_actual + "[label=\"Carnet : " + aux->getEstudiante()->getcarnet() + "\\n\" \n"
                         + "+ \" DPI:   "+ aux->getEstudiante()->getdpi() + "\\n\" \n"
                         + "+ \" Nombre:  "+ aux->getEstudiante()->getname() + "\\n\" \n"
                         + "+ \" Correo:  "+ aux->getEstudiante()->getemail() + "\\n\" \n"
                         + "+ \" Password:  "+ aux->getEstudiante()->getpass() + "\\n\" \n"
                         + "+ \" Creditos:  "+ to_string(aux->getEstudiante()->getcredit()) + "\\n\" \n"
                         + "+ \" Edad:  "+ to_string(aux->getEstudiante()->getedad()) + "\"]; \n";
     e_data += n_actual+ "->" + n_sig + ";\n";
     e_data += n_actual+ "->" + n_anterior + ";\n";

    aux = aux->getnext();
    }while(aux != this->head);

    graph += n_data;
    graph += e_data;
    graph += "\n}";
    //-------------------------------------
    try{
        //Esta variable debe ser modificada para agregar su path de creacion de la Grafica
        string path = "D:\\Resultados\\";
        ofstream file;
        file.open(path + "Estudiantes" + to_string(this->nfile) + ".dot",std::ios::out);
        if(file.fail()){
            exit(1);
        }
        file<<graph;
        file.close();
        string command = "dot -Tpng " + path + "Estudiantes"+to_string(this->nfile) +".dot -o  " + path + "Estudiantes" + to_string(this->nfile)+".png";
        system(command.c_str());
        cout<<"Grafica generada con exito"<<endl;
        this->nfile++;
    }catch(exception e){
        cout<<"Fallo detectado"<<endl;
    }
    //-------------------------------------
    delete aux;
}

