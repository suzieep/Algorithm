package test.algroithm;


public class num1 {

    
        public static String solution(int n, int[][] delivery) {
            int [] bool= new int[n+1];
            String [] outChar = new String[n+1];
            
            for(int i=0; i<n+1 ;i++){
                bool[i] = 2;
                outChar[i]="?";
            }
            
            for (int i=0;i<delivery.length;i++){
                int [] abc = new int[3];
                abc = delivery[i];
                if(abc[2]==1){
                    outChar[abc[0]]="O";
                    bool[abc[0]]=1;
                    outChar[abc[1]]="O";
                    bool[abc[1]]=1;
                    
                    
                }
            }
    

            for (int i=0;i<delivery.length;i++){
                int [] abc = new int[3];
                abc = delivery[i];
                if(abc[2]==0){
                    if(bool[abc[0]]==1 && (bool[abc[1]]==0||bool[abc[1]]==2)){
                        outChar[abc[1]]="X";
                        bool[abc[1]]=0;
                    }
                    else if((bool[abc[0]]==0||bool[abc[0]]==2)&&bool[abc[1]]==1){
                        outChar[abc[0]]="X";
                        bool[abc[0]]=0;
                    }
                    
                }
            }

                    
            String answer = "";
            for (int i=1;i<n+1;i++){
                answer= answer.concat(outChar[i]);
            }
            System.out.println(answer);

            return answer;
        }

    
    public static void main(String[] args) {

        int n = 6;
        int [][] delivery ={{1,3,1},{3,5,0},{5,4,0},{2,5,0}};
        solution(n,delivery);
    }
    
}
