package week5;

import java.util.*;

public class BOJ_1260 {
    static int line;
    static int edge;
    static ArrayList<Integer>[] arrList;
    static boolean [] boold;
    static boolean [] boolb;

    public static void dfs(int now){
        boold[now] = true;
        System.out.print(now + " ");
        for(int i : arrList[now]){
            if(!boold[i]){
                dfs(i);
            }
        }
    }

    public static void bfs(int now){
        Queue<Integer> q = new LinkedList<>();
        q.add(now);
        boolb[now] = true;
        while(!q.isEmpty()){
            int temp = q.poll();
            System.out.print(temp + " ");
            for(int i : arrList[temp]){
                if(!boolb[i]) {
                    boolb[i]=true;
                    q.add(i);
                }
            }
        }
    }


    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        edge = scan.nextInt();
        line = scan.nextInt();
        int initEdge = scan.nextInt();
        boolb = new boolean[edge+1];
        boold = new boolean[edge+1];
        arrList = new ArrayList[edge+1];
        
        for(int i=0; i<=edge; i++){
            arrList[i] = new ArrayList<Integer>();
        }       

        for(int i=0; i<line; i++){
            int a = scan.nextInt();
            int b = scan.nextInt();
            arrList[a].add(b);
            arrList[b].add(a);
        }
        for(int i=0; i<line; i++){
            Collections.sort(arrList[i]);
        }
        dfs(initEdge);
        System.out.println("");
        bfs(initEdge);
        scan.close();
    }


}
