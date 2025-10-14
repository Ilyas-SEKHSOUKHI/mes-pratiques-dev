package EX3_CompteBancaire_Class;
/*
 * 3. Classe "CompteBancaire"
---------------------------
Crée une classe `CompteBancaire` avec :
- titulaire (String)
- solde (double)

Ajoute :
- une méthode `deposer(double montant)`
- une méthode `retirer(double montant)` qui vérifie que le solde reste positif.
- une méthode `afficherSolde()`
 */
public class CompteBancaire { // Class
    String titulaire;
    double solde;
    public CompteBancaire(String titulaire,double solde){ // Contructer
        this.titulaire = titulaire;
        this.solde = solde;
    }
    public String getTitulaire(){ // methode get pour recupere titulaire
        return titulaire;
    }
    public void setTitulaire(String titulaire){ // methode set pour modifier titulaire
        this.titulaire = titulaire;
    }
    public double getSolde(){ // methode get pour recupere solde
        return solde;
    }
    public void setSolde(double solde){ // methode set pour modifier solde
        this.solde = solde;
    }

    // une méthode `deposer(double montant)`
    public double deposer(double montant){
        solde += montant;
        return solde;
    }
    // une méthode `retirer(double montant)` qui vérifie que le solde reste positif.
    public void retirer(double montant){
        solde -= montant;
        if(solde>0){
            System.out.println("Votre solde est = "+solde);
        }else{
            System.out.println(" Votre solde est < 0");
        }
    }
    // une méthode `afficherSolde()`
    public void afficherSolde(){
        System.out.println(" Titulaire : "+titulaire);
        System.out.println(" Votre solde est : "+solde);
    }
}
