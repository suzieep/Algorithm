package week7;
import java.util.*;

public class BOJ_11399 {
    
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int perNum = scan.nextInt();
        int[] perTime = new int[perNum];

        for(int i=0;i<perNum;i++){
            perTime[i]=scan.nextInt();
        }

        Arrays.sort(perTime);

        int sum =0;
        int suma =0;
        for(int i=0;i<perNum;i++){
            
            suma +=perTime[i];
            sum +=suma;
            
        }
        System.out.println(sum);
    }
}
