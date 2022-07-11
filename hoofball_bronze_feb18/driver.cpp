#include<iostream>
#include<algorithm>
using namespace std;

int n;
int cow[105];
int pass[105];
	

int target(int i){ // i = 0 
	if(i == 0) {
		return 1;
	}
	else if(i == n - 1){
		return n - 2;
	}
	else if(cow[i] - cow[i - 1] <= cow[i + 1] - cow[i]){
		return i - 1;
	}
	else{
		return i + 1;
	}
}

int main(){
	int cnt1 = 0, cnt2 = 0;
	cin >> n;

	for(int i = 0;i < n;i ++){
		cin >> cow[i];
		pass[i] = 0;
	}
	sort(cow, cow+n);
	
	for(int i = 0; i < n; i ++){
		pass[target(i)] ++;
	}
	for(int i = 0;i< n;i ++){
		if(pass[i] == 0) {
			cnt1 ++;
		}
	}
	for(int i = 1;i < n; i++){
		if(target(i - 1) == i && target(i) == i - 1 && pass[i] == 1 && pass[i - 1] == 1){
			cnt2 ++;
		}
	}
	printf("%d\n", cnt1 + cnt2);
}