package week3;

import java.util.*;

public class BOJ_2309 {

    public static void main (String []args){

        Scanner scan = new Scanner(System.in);
        int [] arr = new int[9];

        for(int i=0;i<9;i++){
            arr[i] = scan.nextInt();
        }
        findFake(arr);
    }
    public static void findFake(int [] arr){

        
        int totalcount =0;
        int [] arrFin = new int [7];


        for(int j=0;j<9;j++){
            for (int k=0;k<9;k++){
                int [] arr7 = new int [7];
                int count =0;
                int sumTo100=0;
                int tempK=0,tempJ=0,fake1=0,fake2=0;
                for(int i=0;i<9;i++){
                    if (k!=i && j!=i && j!=k){
                        sumTo100 += arr[i];
                        tempK = k;
                        tempJ = j;
                        arr7[count++]=arr[i];
                        
                    }  
                }
                if (sumTo100 == 100&&totalcount==0){
                    Arrays.sort(arr7);

                    for(int p=0;p<count;p++)
                    {
                        System.out.println(arr7[p]);
                    }
                    totalcount++;
                }

            }

        }

    }
    
}

