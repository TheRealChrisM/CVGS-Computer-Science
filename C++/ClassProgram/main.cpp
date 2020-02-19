#include <iostream>

using namespace std;

struct student;
void getStudentInfo(student &s);
void printStudent(student s);

struct student{
    string name;
    string phone;
    int age;
};

int main(){

    int arraySize = 2;

    student studentArray[arraySize];

    for (int i = 0; i < arraySize; i++){
            getStudentInfo(studentArray[i]);
    }

    for (int j = 0; j < arraySize; j++){
            cout << endl;
            printStudent(studentArray[j]);

    }

}

void getStudentInfo(student &s){
    cout << "Enter Name: ";
    cin >> s.name;
    cout << "Enter Phone: ";
    cin >> s.phone;
    cout << "Enter Age: ";
    cin >> s.age;

}

void printStudent(student s){
    cout << "Name: " << s.name << endl;
    cout << "Phone: " << s.phone << endl;
    cout << "Age: " << s.age << endl;
}
