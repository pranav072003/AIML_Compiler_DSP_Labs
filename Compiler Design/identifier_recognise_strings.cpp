#include <iostream>
#include <stdbool.h>
#include <cstring>
#include <cctype>
using namespace std;

bool sub(char* str, char* substr, int len)
{
    int j=0;
    for(int i=0;i<len;i++)
    {
        if(j==strlen(substr))
        {
            break;
        }
        if(str[i]==substr[j])
        {
            j++;
        }
        else if(j!=strlen(substr)-1)
        {
            j=0;
        }
    }
    if(j==strlen(substr)) return true;
    else return false;
}

void checkid(char* id, int len)
{
    char* kw1 = "int";
    char* kw2 = "float";
    char* kw3 = "double";
    char* kw4 = "void";
    char* kw5 = "long";
    char* kw6 = "struct";
    char* kw7 = "class";
    char* kw8 = "char";
    char* kw9 = " ";
    char* kw10 = "!";
    char* kw11 = "#";
    char* kw12 = "@";
    char* kw13 = "%";
    char* kw14 = "enum";
    if(!isalpha(id[0]) && id[0]!='_')
    {
        cout<<"The given string is not a valid identifier.Please try again\n";
        return;
    }
    if(sub(id,kw1,len) || sub(id,kw2,len) || sub(id,kw3,len) || sub(id,kw4,len) || sub(id,kw5,len) || sub(id,kw6,len) || sub(id,kw7,len) || sub(id,kw8,len) || sub(id,kw9,len) || sub(id,kw10,len) || sub(id,kw11,len) || sub(id,kw12,len) || sub(id,kw13,len) || sub(id,kw14,len))
    {
        cout<<"The given string is not a valid identifier.Please try again\n";
        return;
    }
}

int main() 
{
    while(1)
    {
        int len;
        cout<<"Enter string length:-";
        cin>>len;
        char* id = new char[len+1];
        cout<<"Enter the identifier variable name:-";
        scanf(" %[^\n]s",id);
        cout<<"Variable name is "<<id<<"\n";
        checkid(id, len+1);
        int op;
        cout<<"Want to continue:-";
        cin>>op;
        if(op==0) break;
    }
    cout<<"Program terminated\n";
    return 0;
}