package EX_Fonction;
import java.util.Scanner;
//EX10
/*
 *  10. Fonction principale avec menu
    ---------------------------------
    Écris un petit programme qui propose un menu :
    1. Addition
    2. Moyenne
    3. Factorielle
    L'utilisateur choisit une option, entre les valeurs nécessaires, et le programme appelle la fonction correspondante.
 */
public class FonctionPrincipaleAvecMenu {
    public static void Addition(int A,int B){
        int somme = A+B;
        System.out.println("l'addition = "+somme);
    }
    public static double Moyenne(double C,double D,double E){
        double moyenne = (C+D+E)/3;
        return moyenne;
    }
    public static int factorielle(int F){
        int Factorielle = 1;
        for(int i=1;i<=F;i++){
            Factorielle = Factorielle * i;
        }
        return Factorielle;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Entrez une Operation : ");
        String texte = sc.nextLine(); 
        if(texte.equals("Addition")){
            System.out.print("Entrez un entier : ");
            int Number1 = sc.nextInt();
            System.out.print("Entrez un entier : ");
            int Number2 = sc.nextInt();
            Addition(Number1,Number2);
        }else if(texte.equals("Moyenne")){
            System.out.print("Entrez un nombre décimal : ");
            double Num1 = sc.nextDouble();
            System.out.print("Entrez un nombre décimal : ");
            double Num2 = sc.nextDouble();
            System.out.print("Entrez un nombre décimal : ");
            double Num3 = sc.nextDouble();
            System.out.println(Moyenne(Num1,Num2,Num3));
        }else if(texte.equals("Factorielle")){
            System.out.print("Entrez un entier : ");
            int entier = sc.nextInt(); 
            System.out.println(factorielle(entier));
        }else{
            System.out.println("Euror");
        }
        
    }
}
