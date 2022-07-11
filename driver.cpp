#include<iostream>
#include<algorithm>

using namespace std;

int min(int a, int b){
	if(a<b) return a;
	else return b;
}

int max(int a, int b){
	if(a>b) return a;
	else return b;
}

int main(){
	int a, b, x, y;
	int p, q;
	cin >> a >> b >> x >> y;

	p = abs(a-b);
	q = abs(min(a, b) - min(x, y)) + abs(max(a,b) - max(x, y));
	cout << min(p, q) << "\n";
}