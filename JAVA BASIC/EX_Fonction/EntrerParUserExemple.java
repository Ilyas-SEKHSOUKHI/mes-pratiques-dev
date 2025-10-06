// Importer la classe Scanner pour lire l'entrée utilisateur
package EX_Fonction;
import java.util.Scanner;

public class EntrerParUserExemple {

    public static void main(String[] args) {

        // 🔹 Créer un Scanner pour lire ce que l'utilisateur tape au clavier
        Scanner sc = new Scanner(System.in);

        // ---------------------------------------------------
        // Exemple 1 : Lire un entier
        // ---------------------------------------------------
        System.out.print("Entrez un entier : ");
        int entier = sc.nextInt(); // nextInt() lit un nombre entier
        System.out.println("Vous avez entré l'entier : " + entier);

        // ---------------------------------------------------
        // Exemple 2 : Lire un nombre décimal
        // ---------------------------------------------------
        System.out.print("Entrez un nombre décimal : ");
        double decimal = sc.nextDouble(); // nextDouble() lit un nombre avec virgule
        System.out.println("Vous avez entré le nombre décimal : " + decimal);

        // ---------------------------------------------------
        // Exemple 3 : Lire une ligne de texte
        // ---------------------------------------------------
        sc.nextLine(); // Consommer le saut de ligne restant après nextDouble()
        System.out.print("Entrez une phrase : ");
        String texte = sc.nextLine(); // nextLine() lit toute la ligne
        System.out.println("Vous avez écrit : " + texte);

        // ---------------------------------------------------
        // Exemple 4 : Gestion d'erreur si l'utilisateur entre du texte au lieu d'un nombre
        // ---------------------------------------------------
        System.out.print("Entrez un entier (sécurité) : ");
        String input = sc.nextLine(); // lire en texte
        try {
            int n = Integer.parseInt(input); // convertir en entier
            System.out.println("Vous avez entré le nombre : " + n);
        } catch (NumberFormatException e) {
            System.out.println("Erreur : ce n'est pas un nombre !");
        }

        // 🔹 Toujours fermer le Scanner à la fin
        sc.close();
    }
}
