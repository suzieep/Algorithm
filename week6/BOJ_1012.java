package week6;

import java.util.*;

public class BOJ_1012 {
    static boolean[][] visited;
    static int[][] map;
    static int m,n;
    static int dx[] ={-1,1,0,0};
    static int dy[] ={0,0,-1,1};
    static class Box {
        int x;
        int y;

        public Box(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void dfs(int x, int y) {
        
        if(visited[x][y]) return;
		
		visited[x][y]=true;
		for(int i=0; i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx>=0 && ny>=0 && nx<m && ny<n){
                if(map[nx][ny] == 1 && !visited[nx][ny]){
                    dfs(nx, ny);
                }
            }
        }
	}
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int testCase = scan.nextInt();
        int[] count= new int[testCase+1];
        for (int i = 1; i <= testCase; i++) {
            m = scan.nextInt();
            n = scan.nextInt();
            int k = scan.nextInt();
            map = new int[m][n];
            visited = new boolean[m][n];

            for (int j = 0; j < k; j++) {
                map[scan.nextInt()][scan.nextInt()] = 1;
            }

            count[i]=0;
            
            for(int j=0; j<m;j++){
                for(int l=0; l<n; l++){
                    if(map[j][l]==1 && !visited[j][l]){
                        count[i]++;
                        dfs(j,l);
                    }
                }
            }

        }

        for(int i =1; i<=testCase; i++){
            System.out.println(count[i]);       
    }

}
}
