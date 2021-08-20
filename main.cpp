#include <iostream>
#include <Windows.h>
#include "readfile.h";
#include "LogicGen.h"

using namespace std;

void addManual();
void menuPrincipal();
void menuUser();
void menuReport();
void menuTareas();
void menuAddDatosU();

void menuPrincipal(){
    bool salir = false;
    string pathfile = "";
    int opc = 0;
    while(!salir){
    cout << "---------- MENU PRINCIPAL ----------" << endl;
    cout << "|                                  |" << endl;
    cout << "|   1 -> Carga de Usuarios         |" << endl;
    cout << "|   2 -> Carga de Tareas           |" << endl;
    cout << "|   3 -> Ingreso Manual            |" << endl;
    cout << "|   4 -> Reportes                  |" << endl;
    cout << "|   5 -> Salir                     |" << endl;
    cout << "|                                  |" << endl;
    cout << "------------- FIN MENU -------------" << endl;
    cout << "----Ingresar el numero de opcion----" << endl;

    cin >> opc;

    switch(opc){
        case 1:
            cout <<"Escriba la ruta del archivo" << endl;
            cin >> pathfile;
            //getline(cin,pathfile);
            readfiles(pathfile);

            break;
        case 2:
            cout <<"Escriba la ruta del archivo" << endl;

            break;
        case 3:
            addManual();
            break;
        case 4:
            menuReport();
            break;
        case 5:
            salir = true;
            break;
        default:cout <<"seleccione una opcion valida" << endl;
    }
    }
}

void addManual(){
    int opc1 = 0;
    cout << "---- MENU ENTRADA MANUAL -----" << endl;
    cout << "|                            |" << endl;
    cout << "|   1 -> Usuarios            |" << endl;
    cout << "|   2 -> Tareas              |" << endl;
    cout << "|   3 -> Salir / Regresar    |" << endl;
    cout << "|                            |" << endl;
    cout << "---------- FIN MENU ----------" << endl;

    cout << "-Ingresar el numero de opcion-" << endl;

    cin >> opc1;
    switch(opc1){
        case 1:
            menuUser();
            break;
        case 2:
            menuTareas();
            break;
        case 3:
            menuPrincipal();
            break;
        default:cout <<"seleccione una opcion valida" << endl;
    }
}

void menuUser(){
int opcus = 0;
    cout << "------- MENU USUARIOS --------" << endl;
    cout << "|                            |" << endl;
    cout << "|   1 -> Ingresar            |" << endl;
    cout << "|   2 -> Modificar           |" << endl;
    cout << "|   3 -> Eliminar            |" << endl;
    cout << "|   4 -> Salir / Regresar    |" << endl;
    cout << "|                            |" << endl;
    cout << "---------- FIN MENU ----------" << endl;
    cout << "-Ingresar el numero de opcion-" << endl;

    cin >> opcus;
    switch(opcus){
        case 1:
            menuAddDatosU();
            break;
        case 2:
            cout <<"opcion Modificar" << endl;
            break;
        case 3:
            cout << "opcion eliminar" << endl;
            break;
        case 4:
            addManual();
            break;

        default:cout <<"seleccione una opcion valida" << endl;
    }
}

void menuAddDatosU(){
    string carnetU,dpiU,nameU,carreraU,emailU,passU;
    int creditU, edadU;
    cout << "Ingresar No. Carnet" << endl;
    cin.ignore();
    getline(cin,carnetU);
    cout << "Ingresar No. DPI" << endl;

    getline(cin,dpiU);
    cout << "Ingresar Nombre" << endl;

    getline(cin,nameU);
    cout << "Ingresar Carrera" << endl;

    getline(cin,carreraU);
    cout << "Ingresar Correo" << endl;

    getline(cin,emailU);
    cout << "Ingresar Contraseña" << endl;

    getline(cin,passU);
    cout << "Ingresar No. Creditos" << endl;
    cin>> creditU;
    cout << "Ingresar Edad" << endl;
    cin >> edadU;
    valStudent(carnetU,dpiU,nameU,carreraU,emailU,passU,creditU,edadU);

}
void menuTareas(){
int opcus = 0;
    cout << "-------- MENU TAREAS ---------" << endl;
    cout << "|                            |" << endl;
    cout << "|   1 -> Ingresar            |" << endl;
    cout << "|   2 -> Modificar           |" << endl;
    cout << "|   3 -> Eliminar            |" << endl;
    cout << "|   4 -> Salir / Regresar    |" << endl;
    cout << "|                            |" << endl;
    cout << "---------- FIN MENU ----------" << endl;
    cout << "-Ingresar el numero de opcion-" << endl;

    cin >> opcus;
    switch(opcus){
        case 1:
            cout <<"opcion ingresar" << endl;;
            break;
        case 2:
            cout <<"opcion Modificar" << endl;
            break;
        case 3:
            cout << "opcion eliminar" << endl;
            break;
        case 4:
            addManual();
            break;

        default:cout <<"seleccione una opcion valida" << endl;
    }
}

void menuReport(){
int opcrep = 0;
    cout << "---------- MENU REPORTES ----------" << endl;
    cout << "|                                 |" << endl;
    cout << "|   1 -> Lista Usuarios           |" << endl;
    cout << "|   2 -> Linealizacion Tareas     |" << endl;
    cout << "|   3 -> Regresar                 |" << endl;
    cout << "|                                 |" << endl;
    cout << "------------- FIN MENU ------------" << endl;
    cout << "-Ingresar el numero de opcion-" << endl;

    cin >> opcrep;
    switch(opcrep){
        case 1:cout <<"opcion ingresar" << endl;;
            break;
        case 2: cout <<"opcion Modificar" << endl;
            break;
        case 3:  menuPrincipal();
            break;
        default:cout <<"seleccione una opcion valida" << endl;
    }
}


int main()
{
    SetConsoleOutputCP( CP_UTF8 );
    menuPrincipal();
    return 0;
}


