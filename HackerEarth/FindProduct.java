package HackerEarth;

import java.util.Scanner;

public class FindProduct {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        sc.nextLine();
        int prod = 1;
        for(int i = 0; i < length; i++)
            prod = prod * sc.nextInt();
        System.out.println(prod);
        sc.close();
    }
}
