package HackerEarth;

import java.util.Scanner;

public class CountDigits {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        for(int i = 0; i <= 9; i++){
            int c = 0;
            for(int j = 0; j < s.length(); j++){
                if(i == s.charAt(j) - '0')
                    c++;
            }
            System.out.println(i + " " + c);
        }
        sc.close();
    }
}
