#include <iostream>

using namespace std;

struct node {
  int x;
  node *next;
};

node *root;
void stack(int val);
int pop();

int main()
{
       // This will be the unchanging first node

  root = new node; // Now root points to a node struct
  root->next = 0;  // The node root points to has its next pointer
                   //  set equal to a null pointer
  root->x = 5;     // By using the -> operator, you can modify the node
                   //  a pointer (root in this case) points to.
  root->next = new node;
  root->next->x = 100;
  root->next->next = 0;
  cout << root->x << endl;
  cout << root->next->x << endl << endl << endl;
  stack(6);
  cout << root->x << endl;
  cout << root->next->x << endl;
  cout << root->next->next->x << endl << endl << endl;
  stack(12);
  cout << root->x << endl;
  cout << root->next->x << endl;
  cout << root->next->next->x << endl;
  cout << root->next->next->next->x << endl << endl << endl;
  cout << endl << endl << "OLD VAL FROM END: " << pop() << endl << endl;
  cout << root->x << endl;
  cout << root->next->x << endl;
  cout << root->next->next->x << endl << endl << endl;
  cout << endl << endl << "OLD VAL FROM END: " << pop() << endl << endl;
  cout << root->x << endl;
  cout << root->next->x << endl << endl << endl;


}

void stack(int val){
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

int pop(){
    int oldVal;
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
