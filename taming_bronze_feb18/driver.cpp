#include<iostream>

using namespace std;

int main(){
    int n;
    int log[105];
    int uncertain = 0, breakout = 0;
    cin >> n;
    
    for(int i = 0;i < n; i ++){
        cin >> log[i];
    }
    for(int i = 0; i < n; i ++){
        if(log[i] != 0 && log[i] != -1){
            if(log[i] > i) {
                printf("-1\n");
                return 0;
            }
            else break;
        }
    }
    for(int i = 0; i < n; i ++){
        if(log[i] != 0 && log[i] != -1){
            for(int j = log[i] - 1, k = i - 1; j >= 0; j --, k --){
                log[k] = j;
            }
        }
    }
    log[0] = 0;
    for(int i = 0; i < n; i ++){
        if(log[i] == -1){
            uncertain ++;
        }
        else if(log[i] == 0){
            breakout ++;
        }
    }
    printf("%d %d\n", breakout, breakout + uncertain);
}