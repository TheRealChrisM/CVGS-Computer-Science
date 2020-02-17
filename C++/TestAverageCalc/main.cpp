#include <iostream>
#include <sstream>

using namespace std;

string getLetterGrade(int gradeInput);

int main()
{
    bool completed = false;
    int curCount = 0;
    int curVal = 0;
    int tmpVal = 0;
    string tmpStr = "";
    int loopSelect;
    cout << "Please indicate what loop style you want to utilize [1: While | 2: Do While | 3: For]: " << endl;
    cin >> loopSelect;

    if (loopSelect == 1){
        while(!completed){
            cout << "Please input a test score to average! (Enter -1 when you are done inputting scores.): " << endl;
            cin >> tmpStr;
            stringstream newVal(tmpStr);
            newVal >> tmpVal;
            if (tmpVal == -1){
                completed = true;
            }
            else{
                curCount += 1;
                curVal += tmpVal;
            }
        }
    }
    else if (loopSelect == 2){
        do{
            cout << "Please input a test score to average! (Enter -1 when you are done inputting scores.): " << endl;
            cin >> tmpStr;
            stringstream newVal(tmpStr);
            newVal >> tmpVal;
            if (tmpVal == -1){
                completed = true;
            }
            else{
                curCount += 1;
                curVal += tmpVal;
            }
        }while(!completed);
    }
    else if (loopSelect == 3){
        int testNum;
        cout << "Please input the amount of tests you would like to average: " << endl;
        cin >> testNum;
        curCount = testNum;
        for(int i = 1; i<= testNum; i++){
            cout << "Please input test score " << i << ":" << endl;
            cin >> tmpVal;
            curVal += tmpVal;
        }
    }

    int returnVal = (curVal/curCount);
    string grade = getLetterGrade(returnVal);
    cout << endl << "Your Score:" << endl << "[" << grade << "] " << returnVal << "%"<< endl;
    return 0;
}

string getLetterGrade(int gradeInput){
    string letterGrade;
    if (gradeInput >= 89.5){
        letterGrade = "A";
    }
    else if (gradeInput >= 79.5){
        letterGrade = "B";
    }
    else if (gradeInput >= 69.5){
        letterGrade = "C";
    }
    else if (gradeInput >= 59.5){
        letterGrade = "D";
    }
    else{
        letterGrade = "F";
    }
    return letterGrade;
}
