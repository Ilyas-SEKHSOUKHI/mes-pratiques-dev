package EX_Fonction;
//EX6
/*
 *  6. Fonction avec boucle
    -----------------------
    Écris une fonction `compter(int n)` qui affiche les nombres de 1 à n.
 */
public class FonctionAvecBoucle {
    public static void compter(int n){
        for(int i=0;i<n;i++){
            System.out.println(i);
        }
    }
    public static void main(String[] args) {
        int Num = 5;
        compter(Num);
    }
}
