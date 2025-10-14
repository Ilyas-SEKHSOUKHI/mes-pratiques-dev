package EX3_CompteBancaire_Class;

public class main {
    public static void main(String[] args) {
        CompteBancaire A = new CompteBancaire("ilyas sekhsoukhi", 50000);
        CompteBancaire B = new CompteBancaire("Elon Musk", 20000);
        // Affichage
        A.afficherSolde();
        B.afficherSolde();
        // Deposer
        System.out.println("+500"+A.deposer(500));
        System.out.println("+200"+B.deposer(200));
        // Affichage
        A.afficherSolde();
        B.afficherSolde();
        // Retirer
        System.out.println("-200");
        A.retirer(200);
        System.out.println("-50");
        A.retirer(50);
    }
}
