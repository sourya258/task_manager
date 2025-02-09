#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
    int a[] = {11,25,46,88,99,77,4,3,1,-1,63};
    int n = sizeof(a)/sizeof(a[0]);
    int  key, i ,c;
     
    for (i = 1; i < n; i++)
    {
        key = a[i];
        c = i-1;

        while (c >= 0 && a[c] > key)
        {
            a[c+1] = a[c];
            c -= 1;
        }
        a[c+1] = key;
    }

    for (int j = 0; j < n; j++)
    {
        printf("%d",a[j]);
    }
    
    
return 0;
} 


      
      
      

     

