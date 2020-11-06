package week5;
import java.util.*;

public class BOJ_2178 {

    static int[][] graph = new int[100][100];
    static boolean[][] visited = new boolean[100][100];
    static int n = 0;
    static int m = 0;
    static int len[] = { 0, 0, 1, -1 };
    static int wid[] = { 1, -1, 0, 0 };

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        m = scan.nextInt();
 
        String nInput = "";
        for (int i = 0; i < n; i++) {
            nInput = scan.next();
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(nInput.charAt(j) + "");
            }
        }
 
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                visited[i][j] = false;
            }
        }
 
        find();
    }
 
    private static void find() {
 
        int cntWay = 0;
        int qMag;
        int temp;
        int r;
        int c;
        int finish = 0;
 
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(0);
 
        while (finish != 1) {
            qMag = q.size();
 
            for (int i = 0; i < qMag; i++) {
                temp = q.poll();
                r = temp / 100;
                c = temp % 100;
 
                if (r == n - 1 && c == m - 1) {
                    cntWay++;
                    System.out.println(cntWay);
                    finish = 1;
                }
 
                for (int j = 0; j < 4; j++) {
                    int numr = r + wid[j];
                    int numc = c + len[j];
 
                    if (numr >= n || numr < 0 || numc >= m || numc < 0)
                        continue;
 
                    if (graph[numr][numc] == 0)
                        continue;
 
                    if (visited[numr][numc])
                        continue;
 
                    visited[numr][numc] = true;
                    q.offer(numr * 100 + numc);
                }
            }
            cntWay++;
        }
    }
}

