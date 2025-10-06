package EX_Fonction;
//EX5
/*
 *  5. Fonction pour vérifier la parité
    -----------------------------------
    Écris une fonction `estPair(int n)` qui retourne `true` si le nombre est pair, sinon `false`.
 */
public class FonctionPourVerifierLaParite {
    public static boolean estPair(int n){
        boolean Resultat = true;
        if(n%2==0){
            Resultat = true;
        }else{
            Resultat = false;
        }
        return Resultat;
    }
    public static void main(String[] args) {
        int Num = 3;
        System.err.println(estPair(Num));
    }
}
