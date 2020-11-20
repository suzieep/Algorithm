package week7;

import java.util.*;
public class BOJ_1931 {

    static class Meeting {
        int start;
        int finish;

        public Meeting(int start, int finish){
            this.start= start;
            this.finish=finish;
        }
    }
    public static void main(String []args){

        
        Scanner sc = new Scanner(System.in);
        int meetingNum = sc.nextInt();
        int[][] arr = new int[meetingNum][2];

        for (int i=0;i<meetingNum;i++){
            arr[i][0] =sc.nextInt();
            arr[i][1] =sc.nextInt();
            
        }
        Arrays.sort(arr, new Comparator<int[]>(){
            @Override
            public int compare(int[] start, int[]end){
                if(start[1]==end[1]){
                    return Integer.compare(start[0], end[0]);
                }
                return Integer.compare(start[1], end[1]);
            }

        });

        int cnt =0;
        int end =-1;
        for(int i=0;i<meetingNum;i++){
            if(arr[i][0]>=end){
                end=arr[i][1];
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}

