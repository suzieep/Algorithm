package week2;

import java.util.Scanner;

public class BOJ_17608 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int stickCount = scan.nextInt();
        int counts = 1;
        int[] stickHeights = new int[stickCount];

        for (int i = 0; i < stickCount ; i++) {
            stickHeights[i] = scan.nextInt();
        }
        
        int top = stickHeights[stickCount-1];

        for (int i = stickCount-1; i > -1; i--) {
            if (top < stickHeights[i]) {
                
                counts++;
                top = stickHeights[i];
        
            }
        }

        System.out.println(counts);

        scan.close();
    
    }
}
