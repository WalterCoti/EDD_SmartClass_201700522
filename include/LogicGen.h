#ifndef LOGICGEN_H
#define LOGICGEN_H
#include "Estudiante.h"
#include "ListDC.h"
//--------------the matrix recargado
void initMatrix();
//----------------------estudiantes-------------------------
void valStudent(string carnet_,string dpi_,string nombre_, string carrera_,string email_,string pass_, int creditos_,int edad_);
bool isemail(string email_);
bool isdpi(string numdpi_);
bool iscarnet(string carnet_);
void delStudent(string dpi_);
void printStu();
//----------------Tareas---------------------
void valTarea(int mes, int dia,int hora_,string carnetU_,string nombre_,string descripcion_, string materia_, string fecha_, string estado_);
bool existStu(string carnet_);

bool isValDate(string date_);
string dameDate(string date, int type);

//-------------------------Cola----------------
void getgraphCola();



#endif
