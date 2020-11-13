package week6;
import java.util.*;

public class BOJ_2667 {
    static int[][] map;
    static int n;
    static int cnt;
    static int size;
    static int[] aparts;
    static boolean[][] visited;
    static int dx[] ={-1,1,0,0};
    static int dy[] ={0,0,-1,1};
    static ArrayList arrL = new ArrayList();

    static void dfs(int x,int y){
        visited[x][y] = true;
        aparts[cnt]++;

        for(int i=0; i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx>=0 && ny>=0 && nx<size && ny<size){
                if(map[nx][ny] == 1 && !visited[nx][ny]){
                    dfs(nx, ny);
                }
            }
        }
    }
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        size = scan.nextInt();
        map = new int[size+1][size+1];
        aparts = new int [size*size];
        visited = new boolean[size+1][size+1];

        for(int i=0;i<size;i++){

            String line = scan.next();
            String[]c = line.split("");
            
            for(int j=0;j<size;j++){

                int temp = Integer.parseInt(c[j]);
                map[i][j]=temp;
            }
        }

        for(int i=0; i<size;i++){
            for(int j=0; j<size; j++){
                if(map[i][j]==1 && !visited[i][j]){
                    cnt++;
                    dfs(i,j);
                }
            }
        }

        Arrays.sort(aparts);
        System.out.println(cnt);

        for(int j=0; j<aparts.length; j++){
            if(aparts[j]!=0){
                System.out.println(aparts[j]);
            }
        }
    }
}
