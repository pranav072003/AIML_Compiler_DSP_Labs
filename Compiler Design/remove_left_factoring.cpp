#include <iostream>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
using namespace std;

char* common(char* w1, char* w2)
{
    int comlen = 0;
    if(strlen(w1)>=strlen(w2)) comlen = strlen(w2);
    else comlen = strlen(w1);
    char* comm = new char[comlen];
    int k=-1,i=0,j=0;
    while(i<strlen(w1))
    {
        while(j<strlen(w2))
        {
            if(w1[i]==w2[j]){
                k++;
                comm[k]=w1[i];
                i++;
                j++;
                break;
            }
            else{
                return comm;
            }
        }
    }
    return comm;
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
        if(string[i]=='-') j++; //assuming - does not appear anywhere in production (- belongs to production derivation arraow ->)
    }
    if(j>0){          // CFG contains only a non terminal at deriving part
        return false;
    }
    int idx = find(string, '/');
    // if(idx!=(strlen(string)-2) && idx!=-1){
    //     // alternate derivation has more than 1 symbol
    //     return false;
    // }
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
    //assumes only two alternate productions exist
    cout<<"Grammar after removing the left factoring is shown below:-\n";
    for(int i=0;i<num;i++)
    {
        char alpha;
        int idx = find(prodarr[i], '>');
        int idx1 = find(prodarr[i], '/');
        char* sentence = prodarr[i];
        if(idx1!=-1)
        {
            // remove direct left factoring
            int len1 = idx1-(idx+1);
            int len2 = strlen(sentence)-idx1;
            char* word1 = new char[len1];
            char* word2 = new char[len2];
            int k=idx+1;
            for(int i=0;i<len1;i++)
            {
                word1[i] = sentence[k];
                k++;
            }
            k++;
            for(int i=0;i<len2;i++)
            {
                word2[i] = sentence[k];
                k++;
            }
            char* comword = common(word1, word2);
            cout<<sentence[0]<<"->"<<comword<<sentence[0]<<"'"<<"\n";
            cout<<sentence[0]<<"'->";
            int m=0,n=0;
            for(int i=strlen(comword);i<strlen(word1);i++)
            {
                cout<<word1[i];
            }
            cout<<"/";
            for(int i=strlen(comword);i<strlen(word2);i++)
            {
                cout<<word2[i];
            }
            cout<<"\n";
        }
        else
        {
            cout<<prodarr[i]<<"\n";
            continue;
        }
    }
    return 0;
}