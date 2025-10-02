public class PlusGrand {
    public static void main(String[] args) {
        /*2.  Plus grand de deux nombres Lire deux entiers et afficher le plus
        grand.*/
        int Number1 = 5;
        int Number2 = 10;
        if(Number1 > Number2){
            System.out.println(Number1+" Plus Grand du "+Number2);
        }else if(Number1 < Number2){
            System.out.println(Number2+" Plus Grand du "+Number1);
        }else{
            System.out.println(Number1+"="+Number2);
        }
    }
}
