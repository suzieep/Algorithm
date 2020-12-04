package week9;

import java.util.*;

public class BOJ_2437 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int [] arr = new int[n];
        
        for(int i=0; i<n; i++) {
            arr[i] = scan.nextInt();
        }
        
        Arrays.sort(arr);
        
        int min = 1;
        for(int i=0; i<n; i++) {
            if(min < arr[i]) {
                break;
            }
            min += arr[i];
        }
        System.out.println(min);
    }

}
