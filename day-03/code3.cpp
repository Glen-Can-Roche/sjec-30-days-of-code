#include<iostream.h>
#include<iomanip.h>
#include<conio.h>

int main()
{
    int i, n, num[50], a=0, b;

    cout<<"Enter the size of the array: ";
    cin>>n;
    for(i=0; i<n; i++) {
        cin>>num[i];
        a = a + num[i];
    }
    b = a/n;
    for(i=0; i<n; i++) {
        if(num[i]>b) {
            cout<<num[i]<<"  ";
        }
    }
    return 0;
}