package HackerEarth;

import java.util.Scanner;

public class ToggleString {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c >= 65 && c <= 90)
                System.out.print(String.valueOf(c).toLowerCase());
            else if(c >= 97 && c <= 122)
                System.out.print(String.valueOf(c).toUpperCase());
        }
        sc.close();
    }
}
