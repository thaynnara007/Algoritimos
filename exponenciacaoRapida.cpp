#include <iostream>
#include <stdio.h>
using namespace std;

long long int exponenciacaoRapida(long long int a, long long int b){

  if (b == 0) return 1;
  else if( b % 2 == 0) return exponenciacaoRapida((a * a), (b / 2));
  else return (a * exponenciacaoRapida(a, b - 1));
}

int main(){

  long long int result, a , b;
  cin >> a >> b;
  result = exponenciacaoRapida(a,b);
  cout << result << endl;

  return 0;
}
