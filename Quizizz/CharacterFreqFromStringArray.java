package Quizizz;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class CharacterFreqFromStringArray {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the size of the array");
        int length = sc.nextInt();
        sc.nextLine();
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int i;
        //Count the freq of each character and store them in a hashmap
        for(i = 0; i < length; i++){
            System.out.println("Enter String at position: " + i);
            String s = sc.nextLine();
            for(int j = 0; j < s.length(); j ++){
                char c = s.charAt(j);
                Integer val = map.get(new Character(c));
                if(val != null){
                    map.put(c, new Integer(val + 1));
                }else{
                    map.put(c, 1);
                }
            }
        }
        //Get the character occuring the most number of time
        Character maxFreqChar = null;
        int max = 0;
        Set key = map.keySet();
        for(Iterator iter = key.iterator(); iter.hasNext();){
            Character k = (Character) iter.next();
            if(map.get(k) > max){
                max = map.get(k);
                maxFreqChar = k;
            }
        }
        System.out.println(maxFreqChar);
        
        sc.close();
    }
}
