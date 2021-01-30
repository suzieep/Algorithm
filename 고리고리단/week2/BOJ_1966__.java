package week2;

import java.util.LinkedList;
import java.util.*;

public class BOJ_1966__ {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int testCase = scan.nextInt();

        int[] inputDocs = new int[testCase];
        int[] pointDocs = new int[testCase];
        Queue<Integer> q = new LinkedList<Integer>();
        Queue<Integer> qList = new LinkedList<Integer>();
        int[] topDocs = new int[testCase];
        int[] output = new int[testCase];

        for (int i = 0; i < testCase; i++) {
            inputDocs[i] = scan.nextInt();
            pointDocs[i] = scan.nextInt();

            topDocs[i] = 0;

            for (int j = 0; j < inputDocs[i]; j++) {

                int temp = scan.nextInt();
                q.offer(temp);
                if (topDocs[i] < temp) {
                    topDocs[i] = temp;
                }
            }
            int count = 0;

            System.out.println("topdocs" + topDocs[i]);

            while (!q.isEmpty()) {
                System.out.println("count");

                if (q.peek() >= topDocs[i]) {
                    count++;
                    System.out.println(count);
                    if (pointDocs[i] == q.peek()) {
                        output[i] = count;
                    }
                    q.poll();
                } else {
                    q.offer(q.peek());
                    q.poll();
                }

                for (int j = 0; j < inputDocs[i]; j++) {

                    int temp = q.peek();
                    if (topDocs[i] < temp) {
                        topDocs[i] = temp;
                    }
                }

            }

        }

        System.out.println("coujhnt");

        for (int j = 0; j < testCase; j++) {
            System.out.println("countkj");

            System.out.println(output[j]);
        }

        scan.close();

    }
}