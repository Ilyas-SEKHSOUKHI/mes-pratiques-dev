public class CategorieAge {
    public static void main(String[] args) {
        /*Catégorie d’âge Améliorer ton code actuel : afficher “Enfant” (<12),
        “Adolescent” (12–17), “Jeune adulte” (18–24), “Adulte” (25–59),
        “Senior” (60+). */
        System.out.println("Categorie d'age Programme");
        int age = 17;
        if(age<=12){
            System.out.println("Enfant");
        }else if(age>12 && age<=17){
            System.out.println("Adolescent");
        }else if(age>=18 && age<=24){
            System.out.println("Jeune adulte");
        }else if(age>=25 && age<=59){
            System.out.println("Adulte");
        }else{
            System.out.println("Senior");
        }
    }
}
