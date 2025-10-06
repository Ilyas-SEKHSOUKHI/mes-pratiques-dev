package EX_Fonction;
//EX7
/*
 *  7. Fonction récursive
    ---------------------
    Écris une fonction `factorielle(int n)` qui calcule la factorielle d’un nombre (n!).
 */
//5!=5×4×3×2×1=120
public class FonctionRecursive {
    public static void factorielle(int n){
        int Resultat=1;
        for(int i=1;i<=n;i++){
            Resultat = Resultat * i;
        }
        System.out.println(Resultat);
    }
    public static void main(String[] args) {
        int Num =5;
        factorielle(Num);
    }
}
