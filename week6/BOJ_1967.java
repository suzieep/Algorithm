package week6;
import java.util.*;
public class BOJ_1967 {
    static boolean visited[];
    static ArrayList<Integer>[] arrL;
    static int[][] arr;
    static Stack<Integer> stack = new Stack<>();
    static Stack<Integer> stackLen = new Stack<>();


    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int numN = scan.nextInt();

        visited = new boolean[numN + 1];
        arr = new int[numN + 1][numN + 1];
        arrL = new ArrayList[numN + 1];


        for (int i = 1; i <= numN; i++) {
            arrL[i] = new ArrayList<Integer>();
            popCnt[i]=0;
        }
        for (int i = 1; i <= numN - 1; i++) {
            int parent = scan.nextInt();
            int child = scan.nextInt();
            arrL[parent].add(child);
            arrL[child].add(parent);
            int edge = scan.nextInt();
            arr[parent][child] = edge;
        }
        for (int i = 1; i <= numN; i++) {
            if (arrL[i].isEmpty()) {
                realChild[i] = true;
            }
        }
        dfs(1);
        System.out.println(maxL);
        System.out.println(maxR);
        System.out.println(maxL + maxR);

        scan.close();
    }
    
}
