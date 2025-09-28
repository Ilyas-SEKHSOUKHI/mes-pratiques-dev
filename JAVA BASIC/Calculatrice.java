public class Calculatrice {
    public static void main(String[] args) {
        /* Calculatrice simple (switch) Demander deux nombres et une opération
        (+, -, *, /) puis afficher le résultat. */
        int Number1 = 5;
        int Number2 =10;
        char OP = '*';
        int somme = Number1+Number2;
        int soustraction = Number1-Number2;
        int multiplication = Number1*Number2;
        int division = Number1/Number2;
        switch(OP){
            case '+':
            System.out.println("Resultat = "+somme);
            break;
            case '-':
            System.out.println("Resultat = "+soustraction);
            break;
            case '*':
            System.out.println("Resultat = "+multiplication);
            break;
            case '/':
            System.out.println("Resultat = "+division);
            break;
            default:
            System.out.println("Euror");
            break;
        } 
    }
}
