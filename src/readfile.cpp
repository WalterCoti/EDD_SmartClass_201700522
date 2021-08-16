#include "readfile.h"
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include "windows.h"

using namespace std;

string readfiles(string path_){
    ifstream  fileop;
    string text = "";

    fileop.open(path_, ios::in);

    if(!fileop.fail()){
            getline(fileop , text);
        while(!fileop.eof()){
            istringstream div(text);
            cout <<text<< endl;
        }

    fileop.close();
    }else cout << "Error al leer el archivo" << endl;

    return text;
}
