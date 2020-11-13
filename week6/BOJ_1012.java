package week6;
import java.util.*;


public class BOJ_1012 {
    
    static class Box{
        int x;
        int y;
        
        public Box(int x,int y){
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] argss){
        Scanner scan = new Scanner(System.in);
        int testCase = scan.nextInt();
        for(int i=1;i<=testCase;i++){
            int m = scan.nextInt();
            int n = scan.nextInt();
            int k = scan.nextInt();
            int[][] map = new int[m][n];

            boolean[][]visited = new boolean[m][n];

            for (int j=0;j<k;j++){
                map[scan.nextInt()][scan.nextInt()] = 1;
            }

            int count =0;

            Queue<Box> qu = new LinkedList<>();

            for(int j=0;j<m;j++){
                for(int l=0;l<n;l++){
                    if(map[j][l]==1 &&!visited[j][l]){
                        visited[j][l]=true;
                        qu.add(new Box(i,j));
                    while(!qu.isEmpty()){
                        Box tmp = qu.poll();

                        int[] xx={-1,0,1,0};
                        int[] yy= {0,-1,0,1};

                        for(int o =0; o<4;o++){
                            int nx = tmp.x+xx[o];
                            int ny = tmp.y+yy[o];
                            
                            if(nx>=0 && nx<m && ny>=0 && ny<n){
                                if(map[nx][ny]==1&&!visited[nx][ny]){
                                    qu.add(new Box(nx,ny));
                                    visited[nx][ny]=true;
                                }
                            }
                        }
                    }
                    count++;
                }
                    
                }
            }
            System.out.println(count);
        }
       
    }
    
}
