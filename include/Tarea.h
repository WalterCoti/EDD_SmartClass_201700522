#ifndef TAREA_H
#define TAREA_H
#include "Fecha.h"
#include <iostream>
#include <string>
using namespace std;

class Tarea
{
    public:
        Tarea(int idtarea_, string carn_tar, string name_t_, string descript_, string materia_, string fecha_, int hora_, string estado_);
        //setters
        void setidtarea(int idtarea_);
        void setcarnet(string carn_tar_);
        void setnamet(string name_t);
        void setdescri(string descript_);
        void setmateria(string materia_);
        void setfecha(string fecha_);
        void sethora(int hora_);
        void setestado(string estado_);

        //getters
        int getidtarea();
        string getcarnet();
        string getname_t();
        string getdescript();
        string getmateria();
        string getfechatar();
        int gethora();
        string getestado();



    private:
        int idtarea;
        string carn_tar,name_t,descript,materia,estado,fechatar;
        int hora;

};

#endif // TAREA_H
