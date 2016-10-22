package GreedyAlgorithms;

public class ActivitySelection {
    public static void main(String[] args){
        int s[] =  {1, 3, 0, 5, 8, 5};
        int f[] =  {2, 4, 6, 7, 9, 9};
        int n = s.length;
        
        ActivitySelection as = new ActivitySelection();
        as.printMaxActivities(f, s, n);
    }
    public void printMaxActivities(int f[], int s[], int n){
        int i = 0;
        System.out.print(i + " ");
        for(int  j = 1; j < n; j ++){
            if(s[j] >= f[i]){
                System.out.print(j + " ");
                i = j;
            }
        }
    }
}
