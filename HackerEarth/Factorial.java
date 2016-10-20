package HackerEarth;

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int fact = 1;
        for(int i = 2; i <= N; i ++){
            fact = fact *i;
        }
        System.out.println(fact);
        sc.close();
    }
}
