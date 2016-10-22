package HackerEarth;

import java.util.Scanner;

public class TheGreatKian {
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        int length = sc.nextInt();
        long[] arr = new long[length];
        int i;
        for(i = 0; i < length; i ++)
            arr[i] = sc.nextInt();
        for(i = 0; i < length; i++){
            long sum = 0;
            for(int j = i; j < length; j = j + 3){
                sum += arr[j];
            }
            System.out.print(sum + " ");
        }
        sc.close();
    }
}