#include <iostream>

using namespace std;

struct node {
  int x;
  node *next;
};

node *root;
void addToFront(int val);
int removeFromFront();
void addToEnd(int val);
int removeFromEnd();

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
  addToFront(6);
  cout << root->x << endl;
  cout << root->next->x << endl;
  cout << root->next->next->x << endl << endl << endl;
  addToEnd(12);
  cout << root->x << endl;
  cout << root->next->x << endl;
  cout << root->next->next->x << endl;
  cout << root->next->next->next->x << endl << endl << endl;
  cout << endl << endl << "OLD VAL FROM END: " << removeFromEnd() << endl << endl;
  cout << root->x << endl;
  cout << root->next->x << endl;
  cout << root->next->next->x << endl << endl << endl;
  cout << endl << endl << "OLD VAL FROM FRONT: " << removeFromFront() << endl << endl;
  cout << root->x << endl;
  cout << root->next->x << endl << endl << endl;


}

void addToFront(int val){
    node *tmpRoot = root;
    root = new node;
    root->x = val;
    root->next = tmpRoot;
    //root->next
}

int removeFromFront(){
    int oldVal = 0;
    if ((root == 0) || (root -> next == 0)){
        root = 0;
    }
    else{
        oldVal = root->x;
        root = root->next;

    }
    return oldVal;
}

void addToEnd(int val){
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

int removeFromEnd(){
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
