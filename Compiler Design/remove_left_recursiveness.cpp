#include <iostream>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
using namespace std;

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
        if(string[i]=='-') j++; //assuming - does not appear anywhere in production (- belongs to production derivation arraow ->)
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
    cout<<"Grammar after removing the left recursiveness is shown below:-\n";
    for(int i=0;i<num;i++)
    {
        char alpha;
        int idx = find(prodarr[i], '>');
        char* sentence = prodarr[i];
        if(sentence[0]==sentence[idx+1])
        {
            // remove direct left recursiveness
            int idx1 = find(sentence, '/'); // look for alternate production derivation 
            if(idx1==idx+2) alpha='$'; // using $ as NULL character
            else alpha=sentence[idx+2]; // assuming alpha has only 1 character
            if(idx1!=-1){
                // a terminal on alternate derivation exists
                cout<<sentence[0]<<"->"<<sentence[idx1+1]<<sentence[0]<<"'\n";
                if(alpha=='$') cout<<sentence[0]<<"'->"<<sentence[0]<<"'/$\n";
                else cout<<sentence[0]<<"'->"<<alpha<<sentence[0]<<"'/$\n";
            }
            else{
                // a terminal on alternate derivation does not exist
                cout<<sentence[0]<<"->"<<sentence[0]<<"'\n";
                if(alpha=='$') cout<<sentence[0]<<"'->"<<sentence[0]<<"'/$\n";
                else cout<<sentence[0]<<"'->"<<alpha<<sentence[0]<<"'/$\n";
            }
        }
        else
        {
            cout<<prodarr[i]<<"\n";
            continue;
        }
    }
    return 0;
}