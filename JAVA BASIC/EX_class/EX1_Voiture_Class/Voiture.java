package EX1_Voiture_Class;
/*
 * 1. Classe "Voiture"
-------------------
Crée une classe `Voiture` avec les attributs :
- marque (String)
- modele (String)
- annee (int)
- vitesse (int)

Ajoute :
- une méthode `accelerer(int valeur)` qui augmente la vitesse.
- une méthode `ralentir(int valeur)` qui diminue la vitesse sans aller en dessous de 0.
- une méthode `afficherInfos()` qui affiche toutes les informations de la voiture.
 */
class Voiture{  // Class
    String marque ;
    String modele ;
    int annee ;
    int vitesse ;
    public Voiture(String marque,String modele,int annee,int vitesse){ // Constructer
        this.marque = marque;
        this.modele = modele;
        this.annee = annee;
        this.vitesse = vitesse;
    }
    public String getMarque(){ // Methode get pour recupere la valeur de marque
            return marque;
    }
    public void setMarque(String marque){ // Methode set pour modifier la valeur de marque
        this.marque = marque;
    }
    public String getModele(){ // Methode get pour recupere la valeur de modele 
        return modele;
    }
    public void setModele(String modele){ // Methode set pour modifier la valeur de modele
        this.modele = modele;
    }
    public int getAnnee(){ // Methode pour recupere la valeur de annee
        return annee;
    }
    public void setAnnee(int annee){ // Methode pour modifier la valeur de annee
        this.annee = annee;
    }
    public int getVitesse(){ // Methode pour recupere la valeur de vitesse
        return vitesse;
    }
    public void setVitesse(int vitesse){ // Methode pour modifier la valeur de vitesse
        this.vitesse = vitesse;
    }

    // une méthode `accelerer(int valeur)` qui augmente la vitesse.
    public int accelerer(int valeur){ 
        vitesse += valeur;
        return vitesse;
    }

    // une méthode `ralentir(int valeur)` qui diminue la vitesse sans aller en dessous de 0.
    public int ralentir(int valeur){
        if(vitesse>0){
            vitesse -= valeur;
        }else{
            System.out.println("Vitesse = 0");
        }
        return vitesse;
    }

    // une méthode `afficherInfos()` qui affiche toutes les informations de la voiture.
    public void afficherInfos(){
        System.out.println(getMarque());
        System.out.println(getModele());
        System.out.println(getAnnee());
        System.out.println(getVitesse());
    }

} 