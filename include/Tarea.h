#ifndef TAREA_H
#define TAREA_H
#include "Fecha.h"
#include <iostream>
#include <string>
using namespace std;

class Tarea
{
    public:
        Tarea(int idtarea_, int carn_tar, string name_t_, string descript_, string materia_, Fecha *fecha_, int hora_);

        //setters
        void setidtarea(int idtarea_);
        void setcarnet(int carn_tar_);
        void setnamet(string name_t);
        void setdescri(string descript_);
        void setmateria(string materia_);
        void setfecha(Fecha *fecha_);
        void sethora(int hora_);

        //getters
        int getidtarea();
        int getcarnet();
        string getname_t();
        string getdescript();
        string getmateria();
        Fecha *getfechatar();
        int gethora();



    private:
        int idtarea;
        int carn_tar;
        string name_t;
        string descript;
        string materia;
        Fecha *fechatar;
        int hora;

};

#endif // TAREA_H
