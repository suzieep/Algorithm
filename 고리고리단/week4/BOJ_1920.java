package week4;
import java.util.*;

public class BOJ_1920 {
    public static void main (String []args){

        Scanner scan = new Scanner(System.in);
        int numN = scan.nextInt();

        HashSet<Integer> compareHash =  new HashSet<Integer>();
        for (int i=0;i<numN;i++){
            compareHash.add(scan.nextInt());
        }


        int numM = scan.nextInt();
        int [] bIn = new int [numM];

        for (int i=0;i<numM;i++){
            bIn[i] = scan.nextInt();
        }

        for(int i=0; i<numM; i++) { 
            int flag =0;
            if (compareHash.contains(bIn[i])) { 
                flag = 1; 
            } else { 
                flag = 0; } 
            System.out.println(flag); 
        } 
    }
}
