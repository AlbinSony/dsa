int countDigits(int n){
    int count=0,ld;
	while(n>0){
        ld=n%10;
        count=count+1;
        n=n/10;
    }	
    return count;
}

// #include<bits/stdc++.h>
// int count(int n){
//     int count = (int)(log10(n)+1)
//     return count
// }