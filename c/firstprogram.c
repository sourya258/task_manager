#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() {
    char *s = malloc(1024*(sizeof(char))+1);
    if (s == NULL) {
    printf("Memory Alloc. Failed");
    return 1;
    }
    scanf("%[^\n]",s);
    int n = strlen(s);
    int a[n], z=0;
    
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int c = i+1; c < n; c++) {
            if (s[i] == s[c]) {
               count++;
            }else {
            continue;
            }
        }
    a[z++] = count;
    }
    
    for (int i = 0; i < sizeof(a); i++) {
        printf("%d",a[i]);
    }
    
    return 0;
}

/*Displaying Current Date & Time

#include<time.h>(required)
int main(){

   //time_t is a data type suitable for storing the calendar
   time and rawtime is a var that hold's the current 
   calendar time.//

   time_t rawtime;
   
   //The tm structure is defined in the <time.h> header file
    and is used to hold the components of calendar time 
    (such as year, month, day, hour, minute, and second)//
    
   struct tm *tmp;
   
   //The time function gets the current calendar time and 
   stores it in rawtime.//

   time(&rawtime);

   //The localtime function converts the calendar time (rawtime)
    to local time and returns a pointer to a struct tm
    containing the components of the local time.//

   tmp = localtime(&rawtime);

   if (tmp != NULL)
   {

   //The asctime function converts the struct tm to a 
   human-readable string.//

    printf("The Date and Time is : %s",asctime(tmp));
   }else
   printf("Failed to get the local time.\n");
   

return 0;
}*/

/*Creating a temporary file and printing elem from it before terminating
int main(){
FILE *ptr = tmpfile();
    char str[] = "Hello GeeksforGeeks";
    if (ptr == NULL)
    {
        printf("Unable to create temp file");
    }else
    printf("The tempfile was successfully created \n");
    
    fprintf(ptr,"%s",str);

    rewind(ptr);

    while (!feof(ptr))
    {
        putchar(fgetc(ptr));
    }
return 0;
}*/

/* QSORT A STRUCT
typedef struct student{
    char *name;
    int roll;
    int age;
}stu;

int compare (const void *p, const void *q);
int main(){
int  i = 0, c = 0;
stu s[2];

    s[0].name = "bd"; 
    s[0].roll = 66;
    s[0].age = 12; 

    s[1].name = "bd"; 
    s[1].roll = 66;
    s[1].age = 11; 

int n = sizeof(s)/sizeof (s[0]);
qsort(s,n,sizeof(stu),compare);

for (i = 0  ; i < n; i++)
{   
       printf("Name : %s, Roll :%d, Age: %d \n",s[i].name, s[i].roll, s[i].age);
}

return 0;
}
int compare (const void *p, const void *q){
    const stu *p1 = p;
    const stu *p2 = q;
    return p1->age - p2->age;
}*/

/*Removing zeros from a string and printing it 

char s[]={"0001234"};
    int n;

    if ((n = strspn(s,"0"))!=0 && s[n]!= '\0')
    {
        printf("%s",&s[n]);
    }
*/

    // for (int i = 0; i < n/2; i++)
    // {
    //     temp[i] = b[i];
    //     b[i]=b[n-i-1];
    //     b[n-i-1] = temp[i];
    // }
    // /

/*Program for array Rotation
void insert(int *arr,int d, int n);
void rotate(int *arr, int n);
int main(){

    int b[]={1,2,3,4,5,6,7};
    int n = sizeof(b)/sizeof(b[0]);
    insert(b,2,n);

    for (int i = 0; i < n; i++)
    {
        printf("%d \t",b[i]);
    }
    
    return 0;   
}

void insert(int *arr,int d, int n){
    for (int i = 0; i < d; i++)
    { 
        rotate(arr,n);
    }    
}
void rotate(int *arr, int n){
    int temp;
    temp = arr[0];
    for (int i = 0; i < n; i++)
    {
        arr[i]=arr[i+1]; 
    }
    arr[n-1]=temp;
}
*/

/*Pascal's Triangle

int main(){
    
    for (int i = 1; i <= 5; i++)
    {
        for (int s = i; s < 5; s++)
        {
            printf(" ");
        }
        int n = 1;
        for (int c = 1; c <= i; c++)
        {
            printf("%d ",n);
            n = n*(i-c)/c;
        }
    printf("\n");
    }
    
return 0;    
}
*/

/*Printing a triangle of numbers like
         1
       2 3 2
     3 4 5 4 3 
   4 5 6 7 6 5 4
 5 6 7 8 9 8 7 6 5
 
int main(){
    int num =1;
    for (int i = 1; i <= 5; i++)
    {
        num = i;
        for (int s = 5; s > i; s--)
        {
            printf(" ");
        }
        for (int c = 1; c <= i; c++)
        {
            printf("%d",num++);
        }
        num--;
        num--;
        for (int h = 1; h < i; h++)
        {
            printf("%d",num--);
        }
        
    printf("\n");   
    }
return 0;    
}*/
