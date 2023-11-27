#include <iostream>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
using namespace std;

int search(char* string[], char letter, int num)
{
    int j=-1;
    for(int i=0;i<num;i++)
    {
        if(string[i][0]==letter) j=i;
    }
    return j;
}

int find(char* string, char letter)
{
    int j=-1;
    for(int i=0;i<strlen(string);i++)
    {
        if(string[i]==letter) j=i; 
    }
    return j;
}

bool check(char* string)
{
    int j=-1;
    for(int i=0;i<strlen(string);i++)
    {
        if(string[i]=='-') j++; //assuming - does not appear anywhere in production (- belongs to production derivation arrow ->)
    }
    if(j>0){          // CFG contains only a non terminal at deriving part
        return false;
    }
    int idx = find(string, '/');
    if(idx!=(strlen(string)-2) && idx!=-1){
        // alternate derivation has more than 1 symbol
        return false;
    }
    while(j>=0)
    {
        if(isupper(string[j])) return true;
        j--;
    }
    return false;
}

int main()
{
    int op;
    cout<<"Want to initialise program(0/1)-";
    cin>>op;
    if(op==0){
        cout<<"Program terminated\n";
        return 0;
    }
    int num;
    cout<<"Enter number of productions in the grammar:-\n";
    cin>>num;
    char* prodarr[num];
    for(int i=0;i<num;i++)
    {
        int len;
        cout<<"Enter production "<<i+1<<" length:-";
        cin>>len;
        prodarr[i] = new char[len+3]; //2 for ->, 1 for NULL character, len shows number of symbols in production
        cout<<"Enter production-\n";
        cin>>prodarr[i];
        if(!check(prodarr[i])){ 
            cout<<"INVALID PRODUCTION!\n";
            return 1;
        }
    }
    cout<<"Given grammar is:-\n";
    for(int i=0;i<num;i++)
    {
        cout<<prodarr[i]<<"\n";
    }
    char letter;
    // assumes that no left recursion or factoring or more than two alternate productions are there
    while(1)
    {
    cout<<"Enter Non Terminal whose First has be computed:-";
    cin>>letter;
    int count_np = 0;  // checking whether non terminal derives or not
    for(int i=0;i<num;i++)
    {
        if(prodarr[i][0]!=letter) count_np++;
    }
    if(count_np==num)
    {
        cout<<"No derivation for the non terminal\n";
        exit(0);
    }
    // derivation exists
    cout<<"The first set is shown as:-\n";
    int len=-1;
    for(int i=0;i<num;i++)
    {
        if(strlen(prodarr[i])>len) len=strlen(prodarr[i]);
    }
    char* str = new char[len+1];
    str = prodarr[search(prodarr,letter,num)];
    int idx,idx1;
    while(1)
    {
        idx = find(str,'>');
        // looking for alternate productions
        idx1 = find(str,'/');
        if(!isupper(str[idx+1]) && !isupper(str[idx1+1]))
        {
            cout<<str[idx+1]<<"\t"<<str[idx1+1]<<"\t";
            break;
        }
        else
        {
            if(str[idx1+1]=='$')
            {
                // NULL character
                cout<<str[idx+1]<<"\t";
            }
            // another non terminal exists on immediate RHS
            int found = search(prodarr,str[idx+1],num);
            str = prodarr[found];
        }
    }
    cout<<"\n";
    int op;
    cout<<"Want to continue:-";
    cin>>op;
    if(op==0) break;
    }
    return 0;
}