package EX_Fonction;
//EX3
/*
 *  3. Fonction avec valeur de retour
    ---------------------------------
    Écris une fonction `addition(int a, int b)` qui retourne la somme des deux entiers.
 */
public class FonctionAvecValeurDeRetour {
    public static int addition(int a,int b){
        int somme = a+b;
        return somme;
    }
    public static void main(String[] args) {
        int Num1 = 20;
        int Num2 = 62;
        System.out.println(addition(Num1,Num2));
    }
}
