package week5;
import java.util.*;

public class BOJ_2606 {
    static int line;
    static int edge;
    static int count;
    static ArrayList<Integer>[] arrList;
    static boolean [] boold;

    public static void dfs(int now){
        boold[now] = true;
        
        for(int i : arrList[now]){
            if(!boold[i]){
                dfs(i);
            }
        }
    }


    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        edge = scan.nextInt();
        line = scan.nextInt();
        int initEdge = 1;
        
        boold = new boolean[edge+1];
        arrList = new ArrayList[edge+1];
        
        for(int i=1; i<=edge; i++){
            arrList[i] = new ArrayList<Integer>();
        }       

        for(int i=1; i<=line; i++){
            int a = scan.nextInt();
            int b = scan.nextInt();
            arrList[a].add(b);
            arrList[b].add(a);
        }
        for(int i=1; i<=edge; i++){
            Collections.sort(arrList[i]);
        }
        dfs(initEdge);
        for(int i=1; i<=edge; i++){
            if(boold[i]){
                count++;
            };
        }
        System.out.println(count-1);
        scan.close();
    }
    
}
