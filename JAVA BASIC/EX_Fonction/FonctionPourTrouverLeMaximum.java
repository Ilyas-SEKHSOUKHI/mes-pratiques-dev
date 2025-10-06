package EX_Fonction;
//EX8
/*
 *  8. Fonction pour trouver le maximum
    -----------------------------------
    Écris une fonction `maximum(int a, int b, int c)` qui retourne le plus grand des trois nombres.
 */
public class FonctionPourTrouverLeMaximum {
    public static int maximum(int a,int b,int c){
        if(a>b && a>c){
            return a;
        }else if (b>a && b>c){
            return b;
        }else{
            return c;
        }
    }
   public static void main(String[] args) {
        int Num = 1;
        int Num2 = 12;
        int Num3 = 32;
        System.out.println(maximum(Num, Num2, Num3));
   } 
}
