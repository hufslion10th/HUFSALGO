#include <iostream>
using namespace std;

int main(void){
    int n, x;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> x;
    int* a = new int[n];
    for(int i = 0;i < n;i++) cin >> a[i];
    for(int i = 0;i < n; i++){
        if(a[i]<x) cout << a[i] << ' ';
    }
}

/*
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, x, t;
    cin >> n >> x;
    while(n--){
        cin >> t;
        if(t < x) cout << t << ' ';
    }
}
*/