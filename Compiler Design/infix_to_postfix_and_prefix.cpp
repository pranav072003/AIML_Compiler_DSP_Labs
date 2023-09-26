/*
write prgm to recognise identifiers 
write prgm to convert infix to prefix and postfix
*/

/*
https://www.javatpoint.com/convert-infix-to-prefix-notation - referred this for infix to prefix conversion
*/

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

void stringReverse(char* str, char* str_rev, int len)
{
    int j=0;
    for(int i=len-2;i>=0;i--)  //skipping NULL character 
    {
        str_rev[j] = str[i];
        j++;
    }
    str_rev[j] = '\0'; //setting last character as a NULL character
}

void traversal(char arr[],int size)
{
    for(int p=0;p<size;p++)
    {
        printf("%c",arr[p]);
    }
}

int pop_element(char arr[],int size)
{
    size--;
    return size;
}

int push_element(char arr[],int size,char c)
{
    size++;
    arr[size-1]=c;
    return size;
}

int operator_precedence(char z)
{
    int n;
    if(z=='^')
    n=3;
    else if(z=='/' || z=='*')
    n=2;
    else if(z=='+' || z=='-')
    n=1;
    else
    n=0;
    return n;
}

void check_infix_expression(char arr[],int size)
{
    int w=0;
    while(arr[w+2]!='\0')
    {
        if(isspace(arr[w]))
        {
            printf("Invalid infix expression\n");
            exit(0);
        }
        if(operator_precedence(arr[w])>0 && operator_precedence(arr[w+1])>0)
        {
            printf("Invalid infix expression\n");
            exit(0);
        }
        if(isalpha(arr[w]) && isalpha(arr[w+1]))
        {
            printf("Invalid infix expression\n");
            exit(0);
        }
        if(isdigit(arr[w]))
        {
            printf("Invalid infix expression\n");
            exit(0);
        }
    w++;
    }
    if(operator_precedence(arr[0])>0 || operator_precedence(arr[size-2])>0)
    {
        printf("Invalid infix expression\n");
        exit(0);
    }
}

void infix_to_postfix(char arr[],int size)
{
    //passing infix and length+1 as arguments
    arr[size-1]=')';
    char charstack[size];
    char postfix[size];
    int TOSa=-1;
    int TOSb=-1;
    int nA=TOSa+1;
    int nB=TOSb+1;
    nA=push_element(charstack,nA,'(');
    charstack[nA-1]='(';
    for(int i=0;i<size;i++)
    {
        char letter=arr[i];
        if(letter=='(')
        {
            nA=push_element(charstack,nA,letter);
            charstack[nA-1]='(';
        }
        if(letter==')')
        {
            int o;
            int j=nA-1;
            while(charstack[j]!='(')
            {
                    o=operator_precedence(charstack[j]);
                    nB=push_element(postfix,nB,charstack[j]);
                    postfix[nB-1]=charstack[j];
                    nA=pop_element(charstack,nA);
                    j--;
            }
            nA=pop_element(charstack,nA);
            //pop operators from charstack and push to postfix till ( is encountered
        }
        if(isalpha(letter))
        {
            nB=push_element(postfix,nB,letter);
            postfix[nB-1]=letter;
        }
        if(operator_precedence(letter)>0)
        {
            int k=nA-1;
            while(operator_precedence(charstack[k])>=operator_precedence(letter))
            {
                nB=push_element(postfix,nB,charstack[k]);
                postfix[nB-1]=charstack[k];
                nA=pop_element(charstack,nA);
                k--;
            }
            nA=push_element(charstack,nA,letter);
            charstack[nA-1]=letter;
            //check for ^ in charstack.pop if there and push to postfix else push encountered to charstack
        }
    }
    traversal(postfix,nB);
}

void infix_to_prefix(char arr[],int size)
{
    //passing infix and length+1 as arguments
    arr[size-1]='(';
    char chstack[size];
    char prefix_rev[size];
    int TOSc=-1;
    int TOSd=-1;
    int nC=TOSc+1;
    int nD=TOSd+1;
    nC=push_element(chstack,nC,')');
    chstack[nC-1]=')';
    for(int i=0;i<size;i++)
    {
        char letter = arr[i];
        if(letter==')')
        {
            nC=push_element(chstack,nC,letter);
            chstack[nC-1]=')';
        }
        if(letter=='(')
        {
            int o;
            int j=nC-1;
            while(chstack[j]!=')')
            {
                    o=operator_precedence(chstack[j]);
                    nD=push_element(prefix_rev,nD,chstack[j]);
                    prefix_rev[nD-1]=chstack[j];
                    nC=pop_element(chstack,nC);
                    j--;
            }
            nC=pop_element(chstack,nC);
            //pop operators from charstack and push to postfix till ( is encountered
        }
        if(isalpha(letter))
        {
            nD=push_element(prefix_rev,nD,letter);
            prefix_rev[nD-1]=letter;
        }
        if(operator_precedence(letter)>0 && nC==1)
        {
            nC=push_element(chstack,nC,letter);
            chstack[nC-1]=letter;
        }
        if(operator_precedence(letter)>0 && letter=='^')
        {
            int k=nC-1;
            while(operator_precedence(chstack[k]) == operator_precedence(letter))
            {
                nD=push_element(prefix_rev,nD,chstack[k]);
                prefix_rev[nD-1]=chstack[k];
                nC=pop_element(chstack,nC);
                k--;
            }
            nC=push_element(chstack,nC,letter);
            chstack[nC-1]=letter;
        }
        if(operator_precedence(letter)>0 && letter!='^')
        {
            int k=nC-1;
            while(operator_precedence(chstack[k])>operator_precedence(letter))
            {
                nD=push_element(prefix_rev,nD,chstack[k]);
                prefix_rev[nD-1]=chstack[k];
                nC=pop_element(chstack,nC);
                k--;
            }
            nC=push_element(chstack,nC,letter);
            chstack[nC-1]=letter;
        }
    }
    char prefix[nD+1];
    stringReverse(prefix_rev,prefix,nD+1);
    traversal(prefix,nD);
}

int main()
{
    int length;
    int key;
    while(1)
    {
        printf("\nWant to initialise the program or not(Y/N)-");
        scanf("%d",&key);
        if(key==0)
        break;
        if(key!=0 && key!=1)
        {
            printf("Wrong key. Try again\n");
            continue;
        }
        printf("\nEnter the size of infix notation:-");
        scanf("%d",&length);
        char infix[length+1];
        char infix_rev[length+1];
        printf("Enter infix notation:\n");
        scanf("%s",infix);
        check_infix_expression(infix,length+1);
        printf("Inputs correct....moving forward\n");
        stringReverse(infix,infix_rev,length+1);
        printf("The postfix expression is-\n");
        infix_to_postfix(infix,length+1);
        //checking whether string reverse is functioning properly or not
        //printf("%s",infix_rev);
        //write infix_to_prefix function
        printf("\nThe prefix expression is-\n");
        infix_to_prefix(infix_rev,length+1);
    }
    printf("**Program Terminated*");
    return 0;
}