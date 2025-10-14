package EX2_Etudiant_Class;
/*
 * 2. Classe "Etudiant"
--------------------
Crée une classe `Etudiant` avec :
- nom (String)
- age (int)
- moyenne (double)

Ajoute :
- un constructeur pour initialiser les attributs.
- une méthode `afficher()` qui affiche les informations.
- une méthode `estAdmis()` qui retourne vrai si la moyenne >= 10.
 */
public class Etudiant { // Class
    String nom;
    int age;
    double moyenne;
    public Etudiant(String nom,int age,double moyenne){ // Constructer
        this.nom = nom;
        this.age = age;
        this.moyenne = moyenne;
    }
    public String getName(){ // methode pour recupere le nom
        return nom;
    }
    public void setName(String nom){ // methode pour modifier le nom
        this.nom = nom;
    }
    public int getAge(){ // methode pour recupere l 'age
        return age;
    }
    public void setAge(int age){ // methode pour modifier l'age
        this.age = age;
    }
    public double getMoyenne(){ // methode pour recupere la moyenne
        return moyenne;
    }
    public void setMoyenne(double moyenne){ // methode pour modifier la moyenne
        this.moyenne = moyenne;
    }

    //une méthode `afficher()` qui affiche les informations.
    public void afficher(){
        System.out.println(nom);
        System.out.println(age);
        System.out.println(moyenne);
    }

    //une méthode `estAdmis()` qui retourne vrai si la moyenne >= 10.
    public void estAdmis(){
        if(moyenne <10){
            System.out.println("n'est pas Admis");
        }else{
            System.out.println("est Admis");
        }
    }
}
