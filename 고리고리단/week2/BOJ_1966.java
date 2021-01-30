package week2;

import java.util.*;

public class BOJ_1966 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int testCase = scan.nextInt();
        int [] output = new int [testCase];

        for (int i = 0; i < testCase; i++) {
            LinkedList<int[]> q = new LinkedList<>();

            int count = 0;

            int n = scan.nextInt();
            int m = scan.nextInt();

            for (int j = 0; j < n; j++)
                q.add(new int[] { j, scan.nextInt() });

            while (!q.isEmpty()) {
                int[] temp = q.poll();
                boolean bool = true;

                for (int[] p : q)
                    if (p[1] > temp[1])
                        bool = false;
                if (bool) {
                    count++;
                    if (temp[0] == m)
                        break;
                } else
                    q.add(temp);
            }
            output[i]=count;
            
        }

        for (int j = 0; j < testCase; j++) {

            System.out.println(output[j]);
        }

    }
}
