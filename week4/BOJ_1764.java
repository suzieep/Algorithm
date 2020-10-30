package week4;
import java.util.*;

public class BOJ_1764 {
    public static void main (String []args){

        Scanner scan = new Scanner(System.in);

        int numN = scan.nextInt();
        int numM = scan.nextInt();
        scan.nextLine();
        int count = 0;

        HashSet<String> cantHearSet = new HashSet<>(); 
		ArrayList<String> List = new ArrayList<>(); 
    

        for(int i=0;i<numN;i++){
            String cantHear = scan.nextLine();
			cantHearSet.add(cantHear); // 듣지도 못한 문자열을 HashSet에 저장시키는 과정
        }

        for(int i=0;i<numM;i++){
            String cantSee = scan.nextLine();
			if (cantHearSet.contains(cantSee)) {
				count++;
				List.add(cantSee);
			}
        }


        Collections.sort(List);

		System.out.println(count);
		for (int i = 0; i < List.size(); i++) {
			System.out.println(List.get(i));
		}
    }

}