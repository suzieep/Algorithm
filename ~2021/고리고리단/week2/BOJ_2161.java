package week2;
import java.util.*;

public class BOJ_2161 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int cardNum = scan.nextInt();
        Queue<Integer> q = new LinkedList<Integer>();

        for (int i=0;i<cardNum;i++){
            q.offer(i+1);
        }
        
        while(!q.isEmpty()){
            System.out.print(q.poll()+" ");
            if (q.isEmpty()){
                break;
        }
            q.offer(q.poll());
        }
        scan.close();
    }
}