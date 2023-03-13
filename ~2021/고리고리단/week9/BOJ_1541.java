package week9;
import java.util.*;
public class BOJ_1541 {
    public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String exp = scan.next();
		String []str = exp.split("-");
		
		String []tmp = str[0].split("\\+");
		int first=0;
		for (String t : tmp) 
			first += Integer.parseInt(t);
		
		int sum = 0;
		for(int i=1; i<str.length; i++){
			String []temp = str[i].split("\\+");
			for (String t : temp)
				sum += Integer.parseInt(t);
		}
		System.out.println(first-sum);
	}
}