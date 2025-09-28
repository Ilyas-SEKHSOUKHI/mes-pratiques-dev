public class Triangle {
    public static void main(String[] args) {
        
        int lignes = 5; // nombre de lignes du triangle

        for(int i = 1; i <= lignes; i++){ // pour chaque ligne
            for(int j = 1; j <= i; j++){ // afficher i étoiles
                System.out.print("*");
            }
            System.out.println(); // aller à la ligne suivante
        }
    }
}

  
