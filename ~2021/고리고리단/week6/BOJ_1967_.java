package week6;

import java.util.*;

public class BOJ_1967_ {
    static int n, u, v, w, max, maxIndex;
    static boolean[] visit = new boolean[100001];
    static HashMap<Integer, Integer>[] hm = new HashMap[100001];
    static int[] list = new int[100001];


    public static int dfs(int v)  {
        Arrays.fill(visit, false);
        Stack<Box> s = new Stack<>();
        max = 0;
        maxIndex = 1;
        s.push(new Box(v, 0));
        visit[v] = true;
        while (!s.isEmpty()) {

            Box curNode = s.pop();
            if (max < curNode.w) {
                max = curNode.w; 
                maxIndex = curNode.v;
            }

            for (int key : hm[curNode.v].keySet()) {
                Box e = new Box(key, hm[curNode.v].get(key));
                if (!visit[e.v]) {
                    visit[e.v] = true; 
                    s.push(new Box(e.v, e.w + curNode.w));
                }
            }
        }
        return max;
    }

    private static class Box{
        int v, w;
        Box(int v, int w) {
            this.v = v; 
            this.w = w;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            hm[i] = new HashMap<>();
        }
        for (int i = 1; i <= n - 1; i++) {
            u = sc.nextInt();
            v = sc.nextInt();
            w = sc.nextInt();
            hm[u].put(v, w);
            hm[v].put(u, w);
        }
        dfs(1);
        dfs(maxIndex);
        System.out.println(max);
    }

}
