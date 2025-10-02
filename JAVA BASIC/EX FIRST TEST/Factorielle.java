public class Factorielle {
    public static void main(String[] args) {
        /* Factorielle Écrire un programme qui calcule la factorielle d’un
        nombre (ex: 5! = 120).*/
        int N = 5;
        int Factorielle = 1;
        for(int i=1;i<=N;i++){
            Factorielle=Factorielle*i;
        }
        System.out.println("Factorielle du "+N+"="+Factorielle);
    }
}
