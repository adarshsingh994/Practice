package HackerEarth;

import java.util.Scanner;

public class BlackHatTest {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int test = sc.nextInt();
        sc.nextLine();
        for(int j = 0; j < test; j ++){
            String s = sc.nextLine();
            String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
            String cipherText = "";
            for (int i = 0; i < s.length(); i++){
                int charPosition = ALPHABET.indexOf(s.charAt(i));
                int keyVal = (13 + charPosition) % 26;
                while(cipherText.contains(String.valueOf(ALPHABET.charAt(keyVal)))){
                    if(keyVal == 25)
                        keyVal = 0;
                    else
                        keyVal++;
                }
                char replaceVal = ALPHABET.charAt(keyVal);
                cipherText += replaceVal;
            }
            System.out.println(cipherText);
        }
        sc.close();
    }
}