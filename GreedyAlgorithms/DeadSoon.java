package GreedyAlgorithms;

import java.util.Scanner;

public class DeadSoon {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        sc.nextLine();
        int[] a = new int[length];
        for(int i = 0; i < length; i++)
            a[i] = sc.nextInt();
        sort(a);
        sc.close();
    }
    
    protected static void sort(int arr[]){
        int length = arr.length;
    }
}
