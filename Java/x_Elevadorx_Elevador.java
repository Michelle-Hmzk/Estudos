import java.util.Scanner;

public class x_Elevador {
    public static void main(String[] args) {
        Scanner patuu = new Scanner(System.in);

        System.out.println("Qual o limite de peso do elevador?");
        double peso = patuu.nextDouble();

        System.out.println("Qual o limite de pessoas no elevador?");
        int pessoas = patuu.nextInt();

        System.out.println("Qual o peso da primeira pessoa que entrou?");
        double primeira = patuu.nextDouble();

        System.out.println("Qual o peso da segunda pessoa que entrou?");
        double segunda = patuu.nextDouble();
        
        System.out.println("Qual o peso da terceira pessoa que entrou?");
        double terceira = patuu.nextDouble();

        double total = primeira + segunda + terceira;
        
        System.out.println("Entraram 3 pessoas no elevador, no qual cabem " + pessoas + " pessoas.");
        System.out.println("O peso total no elevador é de " + total + " ,sendo que ele suporta " + peso);
    }
}
