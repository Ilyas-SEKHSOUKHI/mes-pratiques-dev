public class FirstProject { // Class Principale
  public static void main(String[] args) { // Fonction Principale
    // les variable
    String Name = "Ilyas SEKHSOUKHI"; // Une variable de type chaine de caractere
    int age = 20; // Une variable de type entier
    boolean Homme = true; // var bool type accepte true or false - 0 or 1
    double le_poids = 50.1; // double = float nombre avec la ,
    char groupes_sanguins = 'A'; // var de type caractere  
    // Affichage
    System.out.println("Le Nom d'utilisateur : "+Name);
    System.out.println("l'age d'utilisatur : "+age);
    System.out.println("est un homme ? "+Homme);
    System.out.println("le poids : "+le_poids+"kg");
    // les condition
    if(age<18){ 
        System.out.println("Petit");
    }else if(age>18 && age<25){
        System.out.println("Jeune");
    }else{
        System.out.println("Vieux");
    }
    // Switch case
    switch(groupes_sanguins){
        case 'A':
        System.out.println("test1"); // code block
        break;
        case 'B':
        System.out.println("test2"); // code block
        break;
        /*case 'AB':
        System.out.println("test3"); // code block
        break;*/
        case 'O':
        System.out.println("test4"); // code block
        break;
        default:
        System.out.println("test5"); // code block
    }

    /*switch(le_poids){ //
        case 50.1:
        System.out.println("test1");
        break;
        case 50.5:
        System.out.println("test2");
        break;
        default:
        System.out.println("test3");
    }
        
    Le switch avec double :
    Java ne supporte pas switch avec des types float ou double. 
    Il faut utiliser int, char, String ou enum. Donc, remplacer par if/else.
    
    */

    // les tableaux
        String[] names = new String[]{"Ilyas","Ahmed","Aziz"}; // liste de type String
        int[] poins = {10,15,20}; // liste de type int
        String[] les_noms = {"ali","Saad"};
        // Affichage
        System.out.println(names[0]); // afficher le name avec l'index 0
        System.out.println(poins[2]); // afficher le int dans la list poins avec l'index 2
        System.out.println(les_noms[1]);
        System.out.println(les_noms); // afficher la list complete
        // codition
        if(names[0]==names[2]){
            System.out.println("meme nom");
        }else{
            System.out.println("diff nom");
        }
        
        if(poins[0]>poins[2]){
            System.out.println(" poin index 0 > poin index 2");
        }else{
            System.out.println("poin index 0 < poin index 2");
        }
    // Tableaux dans un Tableaux
        int[][] numbers={
            {5,7,8},
            {3,2,1},
            {9,1,2}
        };
        //affichage
        System.out.println(numbers[0][2]); //-->Pour afficher 8
        System.out.println(numbers[0][0]); //-->Pour afficher 5
    // une variable string to tableaux
        String pseudos = "ILYAS,SEKHSOUKHI,DEV";
        String[] pseudoss = pseudos.split(","); // String[] pseudos = {"ILYAS","SEKHSOUKHI","DEV"};
        System.out.println(pseudoss[1]); // Pour afficher sekhsoukhi
    // la boucle for
        for(int i=0;i<3;i++){
            System.out.println("test"+i); // afficher test 3 fois
        }
    // la boucle foreach
        String[] Matiere = new String[]{"MATH","ALGORITHME","OOP","SQL"}; // Tableaux de type string
        for(String str : Matiere){ // Boucle pour afficher les element du tableaux
            System.out.println(str); // affichage
        }
        /***********/
        int[] Note = new int[]{10,14,15,20}; // Tableaux avec des element entier
        int calcule=0;
        for(int Notes : Note){ // Boucle pour afficher les element du tableaux
            System.out.println(Notes); // Affichage
            /* Calculer la moyen */
            calcule = calcule + Notes; // la sommes des notes
        }
        System.out.println("La moyenne des notes = "+calcule/Note.length);
        /*
         * calcule/Note.length
         * calcule = la var avec la somme des point
         * Note.length = Combien d'element dans le tableaux
         * calcule/Note.length = la moyenne
         */
    // la boucle while
        int i = 0; // var de type int
        while(i==7){ // une boucle avec la condition d'entrer
            System.out.println("test"); // si i=7 test va se repeter +l'infinie
        }
    // la boucle do while()
        do{ // cette boucle il sexecute au moin une fois 
            System.out.println("test"); // si i !=0 test va se repeter +l'infinie
        }while(i!=0); // condition de sortir
    //Appelle de la fonction
        PremiereFonction();
        Calc(); // Affiche 5
        System.out.println(Calc()); //Affiche 5 la valeur print et Affiche 10 la valeur return
        SommeFunc(5,2); // Pour afficher la somme
        System.out.println(SoustractionFunc(12, 3));// pour afficher la soustraction
  }
  // Les Fonction
  /*Premiere fonction avec une accessibilite private*/
  private static void PremiereFonction(){
    System.out.println("Test Fonction");
  }
  /*Deuxieme fonction de type int + accessibilite public*/
  public static int Calc(){
    System.out.println(5);
    return 10;
  }
  /* Troisieme Fonction void qui calul le nombre de deux entier*/
  public static void SommeFunc(int n1,int n2){
    System.out.println(n1+n2);
  }
  /* Quatrieme Fonction de type int qui calcul la soustraction de deux nombre entier */
  public static int SoustractionFunc(int n1,int n2){
    return n1-n2;
  }
} 
/*
 * Premier projet java 
 * pour appliquer les base
 */