package HackerEarth;

import java.util.Scanner;

public class LifeUniverseEverything {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        for(int i = 0; ; i++){
            int a = sc.nextInt();
            if(a == 42)
                break;
            else
                System.out.println(a);
        }
        sc.close();
    }
}
