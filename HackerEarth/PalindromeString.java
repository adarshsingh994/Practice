package HackerEarth;

import java.util.Scanner;

public class PalindromeString {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String t = "";
        for(int i = s.length() - 1; i >= 0; i--){
            t = t + s.charAt(i);
        }
        if(t.equals(s))
            System.out.println("YES");
        else
            System.out.println("NO");
        sc.close();
    }
}
