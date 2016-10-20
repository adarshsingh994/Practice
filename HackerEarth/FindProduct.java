package HackerEarth;

import java.util.Scanner;

public class FindProduct {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        sc.nextLine();
        long prod = 1;
        for(int i = 0; i < length; i++)
            prod = (prod * sc.nextInt()) % (long)(Math.pow(10, 9) + 7);
        System.out.println(prod);
        sc.close();
    }
}
