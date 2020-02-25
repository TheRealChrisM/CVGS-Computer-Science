#include <iostream>

using namespace std;

struct node {
  char x;
  node *next;
};

node *root;
void stack(char val);
char pop();
void stackWord(string word);
bool checkPalindrome(string word);

int main(){
    string goAgain = "y";
    while((goAgain == "y") || (goAgain == "Y")){
        cout << "Please enter a word [Only use lowercase letters!]: ";
        string wordInput = "";
        cin >> wordInput;
        cout << endl;
        if(checkPalindrome(wordInput)==1){
            cout << wordInput << " is a palindrome!" << endl;
        }
        else if (checkPalindrome(wordInput)==0){
            cout << wordInput << " is not a palindrome!" << endl;
        }
        else{
            cout << wordInput << " resulted in an ERROR." << endl;
        }
        cout << endl << "Try again? [Y/N] ";
        cin >> goAgain;
        cout << endl;
    }

}

void stackWord(string word){
    for(int i = 0; i<word.length(); i++){
        stack(word[i]);
    }
}

bool checkPalindrome(string word){
    bool isPalindrome = true;
    stackWord(word);
    string reversedWord = "";
    for (int j = 0; j<word.length(); j++){
        if(word[j] != pop()){
            isPalindrome = false;
        }
    }
    return isPalindrome;
}

void stack(char val){
    if (root != 0){
        node *curPos = root;
        while(curPos->next != 0){
            curPos = curPos->next;
        }
        curPos->next = new node;
        curPos = curPos->next;
        curPos->x = val;
        curPos->next = 0;
    }
    else{
        root = new node;
        root->x = val;
        root->next = 0;
    }
}

char pop(){
    char oldVal;
    if (root == 0){
        oldVal = -1;
    }
    else if (root->next == 0){
        oldVal = root->x;
        root = 0;
    }
    else{
        node *curPos = root;

        while(curPos->next != 0){
            curPos = curPos->next;
        }

        oldVal = curPos->x;
        curPos = root;

        while(curPos->next->next != 0){
            curPos = curPos->next;
        }
        curPos->next = 0;
    }
    return oldVal;
}
