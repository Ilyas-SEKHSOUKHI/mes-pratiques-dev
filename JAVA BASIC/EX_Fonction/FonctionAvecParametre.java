package EX_Fonction;
//EX2
/*
 *  2. Fonction avec paramètre
    --------------------------
    Écris une fonction `saluer(String nom)` qui affiche "Bonjour " suivi du nom passé en paramètre.
 */
public class FonctionAvecParametre {
    public static void saluer(String nom){
        System.out.println("Bonjour : "+nom);
    }
    public static void main(String[] args) {
        String user = "Ilyas SEKHSOUKHI";
        saluer(user);
    }
}
