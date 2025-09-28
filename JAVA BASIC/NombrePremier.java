public class NombrePremier {
    public static void main(String[] args) {
        /*Nombre premier Vérifier si un nombre donné est premier.*/
        int Nombre = 7;
        int div = 0;
        if(Nombre<=1){
            System.err.println("faux");
        }else{
            for(int i=2;i<Nombre;i++){
                div = Nombre%i;
                if(div == 0){
                    System.out.println("Faux");
                    break; // on arrête car ce n'est pas premier
                }
                if(i == Nombre -1){ // si on arrive à la fin sans diviseur
                    System.out.println("Vrai");
                    break;
                }
            }
        }
    }
}
