package EX7_Cercle_Class;

public class main {
    public static void main(String[] args) {
        Cercle A = new Cercle(5);
        // l'aire
        double Aire = A.calculerAire();
        System.out.println(Aire);
        // le perimetre
        double Perimetre = A.calculerPerimetre();
        System.out.println(Perimetre);
        // affichage
        System.out.println("AFFICHAGE");
        A.afficherInfos();
    }
}
