package EX1_Voiture_Class;

public class main {
    
    /*public static void affichage_Voiture(Voiture V){ // Fonction pour afficher resultat
        System.out.println(V.marque);
        System.out.println(V.modele);
        System.out.println(V.annee);
        System.out.println(V.vitesse);
    }*/
    public static void main(String[] args) {
        Voiture Voiture1 = new Voiture("BMW", "MSport", 2025,350 );
        Voiture Voiture2 = new Voiture("Ford", "Focus", 2023,210 );
        /*affichage_Voiture(Voiture1);
        affichage_Voiture(Voiture2);*/
        
        /*String A = Voiture1.getModele();
        System.out.println(A);*/

        // afficher tout les info des deux voiture
        System.out.println("Les info des voitures");
        Voiture1.afficherInfos();
        Voiture2.afficherInfos();
        
        // afficher la vitesse apres l'acceleration
        System.out.println("La vitesse des deux Voiture avant l'acceleration");
        System.out.println("Voiture 1 : "+Voiture1.getVitesse());
        System.out.println("Voiture 2 : "+Voiture1.getVitesse());
        System.out.println("La vitesse des deux voiture apres l'acceleration");
        System.out.println("Voiture 1 : "+Voiture1.accelerer(5));
        System.out.println("Voiture 2 : "+Voiture2.accelerer(5));

        // afficher la vitesse apres ralentir
        System.out.println("La vitesse avant ralentir");
        System.out.println("Voiture 1 : "+Voiture1.getVitesse());
        System.out.println("Voiture 1 : "+Voiture2.getVitesse());
        System.out.println("La vitesse des deux voiture apres ralentir");
        System.out.println("Voiture 1 : "+Voiture1.ralentir(5));
        System.out.println("Voiture 1 : "+Voiture2.ralentir(5));
    }

}
