package EX2_Etudiant_Class;

public class main {
    public static void main(String[] args) {
        Etudiant A = new Etudiant("Ilyas", 20, 15);
        Etudiant B = new Etudiant("Saad", 22, 8);
        /*System.out.println(A.getName());
        A.setName("sekhsoukhi");
        System.out.println(A.getName());*/
        A.afficher();
        B.afficher();
        A.estAdmis();
        B.estAdmis();
    }
}
