#include <iostream>
#include<sstream>

using namespace std;

struct student{
    string fName;
    string lName;
    int testOne;
    int testTwo;
    int testThree;
};

struct node {
  student stud;
  node *next;
  node *previous;
};

node *root;
void addToFront(student val);
student removeFromFront();
void addToEnd(student val);
student removeFromEnd();
string outputStudentInformation();

int main(){
    root = new node;
    root->next = 0;
    root->previous = 0;

    //Student One's info
    student studOne;
    studOne.fName = "Fred";
    studOne.lName = "Bindlebottom";
    studOne.testOne = 98;
    studOne.testTwo = 76;
    studOne.testThree = 88;

    //Student Two's info
    student studTwo;
    studTwo.fName = "Jared";
    studTwo.lName = "Nahtfromsoubway";
    studTwo.testOne = 56;
    studTwo.testTwo = 78;
    studTwo.testThree = 75;

    //Student Three's info
    student studThree;
    studThree.fName = "Ahmerigan";
    studThree.lName = "Eckle";
    studThree.testOne = 98;
    studThree.testTwo = 94;
    studThree.testThree = 97;

    addToEnd(studOne);
    addToEnd(studTwo);
    addToEnd(studThree);

    cout<< endl;

    cout<< outputStudentInformation()<<endl;


}

void addToFront(student val){
    if((root->next != 0)&&(root->next != root)){
        node *tmpRoot = root;
        root = new node;
        root->stud = val;
        root->next = tmpRoot;

        //find end of list
        node *curPos = tmpRoot;
        while(curPos->next != tmpRoot){
            curPos = curPos->next;
        }
        root->previous = curPos;
        curPos->next = root;
        tmpRoot->previous = root;
        //root->next
    }
    else if ((root->next == 0)){
        root = new node;
        root->stud = val;
        root->next = root;
        root->previous = root;
    }
    else if (root->next == root){
        node *tmpRoot = root;
        root = new node;
        root->stud = val;
        root->next = tmpRoot;
        root->previous = tmpRoot;
        tmpRoot->next = root;
        tmpRoot->previous = root;
    }
}

void addToEnd(student val){
    if ((root->next != 0)&&(root->next != root)){
        node *curPos = root;
        while(curPos->next != root){
            curPos = curPos->next;
        }
        curPos->next = new node;
        curPos->next->previous = curPos;
        curPos = curPos->next;
        curPos->stud = val;
        curPos->next = root;
        root->previous = curPos;

    }
    else if ((root->next == 0)){
        root = new node;
        root->stud = val;
        root->next = root;
        root->previous = root;
    }
    else if (root->next == root){
        root->next = new node;
        root->next->stud = val;
        root->next->next = root;
        root->next->previous = root;
        root->previous = root->next;
    }
}

student removeFromFront(){
    student oldVal;
    if (root->next == 0){
       root = new node;
        root->next = 0;
        root->previous = 0;
    }
    else if (root->next == root){
        oldVal = root->stud;
        root = new node;
        root->next = 0;
        root->previous = 0;
    }
    else{
        oldVal = root->stud;
        node *curPosition = root->next;
        curPosition->previous = root->previous;
        curPosition = root->previous;
        curPosition->next = root->next;
        root = root->next;
    }
    return oldVal;
}

student removeFromEnd(){
    student oldVal;
    if (root->next == 0){
       root = new node;
        root->next = 0;
        root->previous = 0;
    }
    else if (root->next == root){
        oldVal = root->stud;
        root = new node;
        root->next = 0;
        root->previous = 0;
    }
    else{
        oldVal = root->stud;
        node *lastNode = root->previous;
        node *secondToLast = lastNode->previous;
        secondToLast->next = root;
        root->previous = secondToLast;
    }
    return oldVal;
}

string outputStudentInformation(){
    string studentInfo = "";

    node *curPosition = root;
    while(curPosition->next != root){
        studentInfo+=(curPosition->stud.lName) + ", " + (curPosition->stud.fName) + ": ";
        int averageScore = ((curPosition->stud.testOne) + (curPosition->stud.testTwo) + (curPosition->stud.testThree))/3;
        stringstream ss;
        ss << averageScore;
        string scoreStr = ss.str();
        studentInfo+= scoreStr;
        studentInfo+=  "%\n";
        curPosition = curPosition->next;
    }
    studentInfo+=(curPosition->stud.lName) + ", " + (curPosition->stud.fName) + ": ";
    int averageScore = ((curPosition->stud.testOne) + (curPosition->stud.testTwo) + (curPosition->stud.testThree))/3;
    stringstream ss;
    ss << averageScore;
    string scoreStr = ss.str();
    studentInfo+= scoreStr;
    studentInfo+=  "%\n";

    return studentInfo;
}
