#include <stdio.h>
#include <Windows.h>
int main(void) {
    int a[10]={1,2,3,4,5,6,7,8,9,10};
    for(int i=0;i<10;i++){
        printf("%d ",a[i]);
        Sleep(500);
    } 
    system("color 5A");
    return 0;
}   
