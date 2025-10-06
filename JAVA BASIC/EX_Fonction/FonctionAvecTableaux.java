package EX_Fonction;
//EX9
/*
 *  9. Fonction avec tableau
    ------------------------
    Écris une fonction `sommeTableau(int[] tab)` qui retourne la somme de tous les éléments du tableau.
 */
public class FonctionAvecTableaux {
    public static int sommeTableau(int[] tab){
        int somme = 0;
        for(int i=0;i<tab.length;i++){
            somme = somme + tab[i];
        }
        return somme;
    }
    public static void main(String[] args) {
        int[] Notes= new int[]{1,5,6,9,8,10};
        System.out.println(sommeTableau(Notes));
    }
}
