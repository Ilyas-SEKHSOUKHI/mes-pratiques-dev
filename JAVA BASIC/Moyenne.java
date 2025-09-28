public class Moyenne {
    public static void main(String[] args) {
        /* Moyenne des
        notes Demander à l’utilisateur d’entrer 5 notes et afficher la moyenne.*/
        int[] Note = new int[]{11,15,14,20}; // list des notes
        int somme = 0;
        int moyenne = 0;
        for(int i=0;i<Note.length;i++){
            somme = somme + Note[i];
        }
        moyenne = somme/Note.length;
        //System.out.println(somme);
        System.out.println("Moyenne : "+moyenne);
    }
}