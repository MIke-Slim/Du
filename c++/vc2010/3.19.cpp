#include <iostream>
#include <ctime>
using namespace std;
// int main(){
//     if(1){
//         cout<<"Hello"<<endl; // This will print Hello

//         int target = 10;
//         int guess;
//         int a=0;
       
        
        
//         while(1){
//         cin>>guess;
//         if(target==guess){
//             cout<<"You guessed correctly"<<endl;
//             a=1;}
        
//         if(target!=guess){
//             if(target>=guess)
//                 cout<<"You guessed high"<<endl;
//             if(target<guess)
//                 cout<<"You guessed low"<<endl;
            
//         }
//         if (a==1)
//             break;
//         }


        
//     }
// }

// int main(){
//     int x,y;
//     cin>>x;
//     switch(x){
//         case 1:y=2;break;
//         case 2:y=3;break;
//         case 3:y=4;break;
//         case 4:y=5;break;  
//         case 5:y=6;break;
//         case 6:y=7;break;
//         case 7:y=8;break;   
//         case 8:y=9;break;
//         case 9:y=10;break;
//         default:y=0;}
//         cout<<y<<endl;    
    
// }
// typedef double MYTYPE;
// int main(){
//     MYTYPE x,y;
//     int u;
//     cin>>x;
//     switch(x){
//         case 1.0:y=2;break;
//         case 2.0:y=3;break;
//         case 3.0:y=4;break;
//         case 4.0:y=5;break;  
//         case 5.0:y=6;break;
//         case 6.0:y=7;break;
//         case 7.0:y=8;break;   
//         case 8.0:y=9;break;
// }

// int main(){
//     int tar,gue,found=0;
//     srand(time(0));
//     while(found==0){

//         tar=rand()%10+1;
//         cout<<"Enter your guess: ";
//         cin>>gue;
//         if(gue==tar){
//             cout<<"You found the number!"<<endl;
//             found=1;
//         }
//         else{
//             if(gue>tar)
//                 cout<<"You guessed high"<<endl;
//             else
//                 cout<<"You guessed low"<<endl;
//     }}
    int i=0,sum=1;
    int main(){
    //     while(i<1000){
    //     i++;
    //     sum+=i;

    // }

    // 计算100的阶乘
// for(i=1;i<100;i++){
//         sum*=i;
//         i++;
//     }
// cout<<sum<<endl;
for(i=1;i<100;i++){
    int sum = 1;
    for(int j=1;j<=i;j++){
        sum *= j;
    }
    cout<<sum<<endl;
}



}



