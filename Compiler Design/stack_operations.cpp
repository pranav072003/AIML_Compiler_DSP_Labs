#include <iostream>
using namespace std;

class Stack   
{
    public:
        int* stack;
        int pointer;
        int size;
        
        Stack(int num)
        {
            stack = new int[num];
            pointer=-1;
            size=num;
            
        }
        
        void push(int a)
        {
            if(pointer==size-1)
            {
                cout<<"Overflow! Nothing can be added\n";
                return;
            }
            pointer++;
            stack[pointer]=a;
            cout<<"Pushed!\n";
            cout<<"Top of the stack is currently "<<stack[pointer]<<"\n";
        }
        
        void pop()
        {
            if(pointer==-1)
            {
                cout<<"Underflow! Nothing can be popped\n";
                return;
            }
            pointer--;
            cout<<"Popped\n";
            if(pointer==-1)
            {
                cout<<"Stack has been emptied\n";
                return;
            }
            cout<<"Top of the stack is currently "<<stack[pointer]<<"\n";
        }
        
        void display()
        {
            if(pointer==-1)
            {
                cout<<"Stack is empty!\n";
                return;
            }
            cout<<"Stack contents are:-\n";
            for(int i=0;i<=pointer;i++)
            {
                cout<<stack[i]<<"\t";
            }
            cout<<"<---TOP\t"<<"\n";
        }
};

int main()
{
    int num;
    cout<<"Enter size of stack:-";
    cin>>num;
    cout<<"Creating empty stack of size "<<num<<".....\n";
    Stack obj = Stack(num);
    while(1)
    {
        int op1;
        cout<<"Which operation to perform:-";
        cin>>op1;
        if(op1==1)
        {
            int n;
            cout<<"Enter number to be added:-";
            cin>>n;
            obj.push(n);
        }
        else if(op1==2)
        {
            obj.pop();
        }
        else if(op1==3)
        {
            obj.display();
        }
        int op;
        cout<<"Want to continue:-";
        cin>>op;
        if(op==0) break;
    }
    cout<<"Program terminated!";
}