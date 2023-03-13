package week4;

import java.util.*;

public class BOJ_2002 {

    public static void main(String[] args) throws Exception{

        Scanner scan = new Scanner(System.in);
        int cars = scan.nextInt();
        HashMap<String, Integer> carNames = new HashMap<>();
        int count = 0;

        for (int i = 0; i < cars; i++) {
            String temp = scan.next();
            carNames.put(temp, i);
        }
        int[] out = new int[cars];

        for (int i = 0; i < cars; i++) {
            String temp = scan.next();
            out[i] = carNames.get(temp);
        }

        for (int i = 0; i < cars - 1; i++) {
            for (int j = i + 1; j < cars; j++) {

                if (out[i] > out[j]) {
                    count++;
                    break;
                }

            }
        }
        System.out.println(count);
        scan.close();
    }
}
