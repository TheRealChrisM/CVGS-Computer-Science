#include <iostream>
#include <stdlib.h>
#include <ctime>

using namespace std;

int rollDice();
void startGame();
void roundTwo(int pointEstablished);
void loseGame();
void winGame();

int main()
{
    startGame();
}

int rollDice(){
    int randInt = rand()%6+1;
    return randInt;
}

void startGame(){
    unsigned seed = time(0);
    srand(seed);

    int rollOne = rollDice();
    int rollTwo = rollDice();
    int diceSum = rollOne + rollTwo;

    cout << "You rolled a " << rollOne << " and " << rollTwo << " which equals " << diceSum << "." << endl;

    if ((diceSum == 2)||(diceSum == 3)||(diceSum == 12)){
        loseGame();
    }
    else if ((diceSum == 7)||(diceSum == 11)){
        winGame();
    }
    else{
        roundTwo(diceSum);
    }

}

void roundTwo(int pointEstablished){
    int gameStatus = 0;
    while(gameStatus == 0){
        int rollOne = rollDice();
        int rollTwo = rollDice();
        int diceSum = rollOne + rollTwo;

        cout << "You rolled a " << rollOne << " and " << rollTwo << " which equals " << diceSum << "." << endl;

        if (diceSum == 7){
            gameStatus = -1;
            loseGame();
        }
        else if (diceSum == pointEstablished){
            gameStatus = 1;
        }
    }
    if (gameStatus == -1){
        loseGame();
    }
    else if (gameStatus == 1){
        winGame();
    }
}

void loseGame(){
    string playAgain = "";
    cout << "You lose. Play again? [Y/N]: ";
    cin >> playAgain;
    cout << endl;
    if ((playAgain == "Y")||(playAgain == "y")){
        startGame();
    }
    else{
        exit(0);
    }
}

void winGame(){
    string playAgain = "";
    cout << "You win! Play again? [Y/N]: ";
    cin >> playAgain;
    cout << endl;
    if ((playAgain == "Y")||(playAgain == "y")){
        startGame();
    }
    else{
        exit(0);
    }
}
