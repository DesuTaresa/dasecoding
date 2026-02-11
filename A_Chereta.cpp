#include<iostream>
using namespace std;


int main () {
    int n ;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int max_i = 0 , next_max ;

    for(int j=1; j<n; j++){
        if (arr[max_i] < arr[j])
        {
            next_max = max_i;
            max_i = j;
        }
        else if ( arr[next_max] < arr[j]) {
            next_max = j;
        }
    }
cout << max_i << arr[next_max];

}