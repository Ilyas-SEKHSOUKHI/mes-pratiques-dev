package EX_Fonction;
//EX4
/*
 *  4. Fonction pour calculer une moyenne
    -------------------------------------
    Écris une fonction `moyenne(double n1, double n2, double n3)` qui retourne la moyenne des trois nombres.
 */
public class FonctionPourCalculerUneMoyenne {
    public static double moyenne(double n1,double n2,double n3){
        double somme = n1 + n2 + n3;
        double moyenne = somme/3;
        return moyenne;
    }
    public static void main(String[] args) {
        double A = 1.23;
        double B = 2.654;
        double C = 3.654;
        System.out.println(moyenne(A,B,C));
    }
}
