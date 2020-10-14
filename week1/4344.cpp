
#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int casenum;
    double per[100]={0};
    
    cin >> casenum;
    for (int c=0 ; c<casenum ; c++){
        int over=0, sum=0, studentnum=0,score=0;
        double mid=0;
        cin >> studentnum;
        int data[casenum][studentnum];
        
        for(int s=0 ; s<studentnum ; s++){
            cin >> score;
            data[c][s]=score;
            sum = sum + data[c][s] ;
            }
        mid = sum/studentnum;
        for(int s=0 ; s<studentnum ; s++){
            if(data[c][s]> mid){
                (over)++;
            }
        }
        
        per[c] = (double)over/studentnum;
        
    }

    
    for(int j=0 ; j<casenum ; j++){
    cout << fixed << setprecision(3) << per[j]*100 << "%" << endl;
    }
}
