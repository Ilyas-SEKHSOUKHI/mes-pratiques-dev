public class Somme1jusquaN {
    public static void main(String[] args) {
        /* 5. Somme des N
        premiers entiers Lire un nombre N et calculer la somme de 1 jusqu’à N.*/
        int N = 10;
        int Somme = 0;
        for(int i=0;i<=N;i++){
            Somme=Somme+i;
        }
        System.out.println("Resultat = "+Somme);
    }
}
