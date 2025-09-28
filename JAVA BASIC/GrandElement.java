public class GrandElement {
    public static void main(String[] args) {
        /*Maximum dans un tableau Lire un tableau d’entiers et trouver le plus
        grand élément. */
        int[] Numbers = new int[]{12,15,18,20,5};
        int COMP1 = 0;
        for(int i=0;i<Numbers.length;i++){
            if(Numbers[i]>Numbers[i++]){
                COMP1 += Numbers[i];
            }else{
                COMP1 += Numbers[i++];
            }
        }
        System.out.println(COMP1);
    }
}
