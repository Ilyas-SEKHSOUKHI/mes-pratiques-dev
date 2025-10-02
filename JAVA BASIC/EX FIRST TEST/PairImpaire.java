public class PairImpaire {
    public static void main(String[] args) {
        /*1. Pair ou impair
        Écrire un programme qui prend un entier et affiche s’il est pair ou
        impair. */
        int Nombre = 10;
        System.out.println(Nombre%2);
        if(Nombre%2==0){
            System.out.println("Pair");
        }else{
            System.out.println("Impair");
        }
    }
}
