package week9;

import java.util.*;

public class BOJ_1339 {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        String [] arr = new String[n];
        int [] al = new int[26];
        for(int i=0; i<n; i++){
            arr[i] = scan.next();
        }


        for(int i=0; i<n; i++){
            int temp = (int)Math.pow(10,arr[i].length()-1);
            for(int j=0; j<arr[i].length(); j++){
                al[(int)arr[i].charAt(j)-65]+=temp;
                temp /=10;
            }
        }

        Arrays.sort(al);
        int idx = 9;
        int sum =0;
        for(int i=al.length-1; i>=0; i--){
            if(al[i] == 0){
                break;
            }
            sum+= al[i]*idx;
            idx--;
        }
        System.out.println(sum);
    }
}
