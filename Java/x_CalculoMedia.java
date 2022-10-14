import java.util.Scanner;

public class x_CalculoMedia {
    public static void main(String[] args) {
        Scanner pinguim = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        String nome = pinguim.nextLine();

        System.out.println("Digite a primeira nota: ");
        double nota = pinguim.nextDouble();

        System.out.println("Digite a segunda nota: ");
        double nota1 = pinguim.nextDouble();
        
        double media = (nota+nota1)/2;

        System.out.println("Olá " + nome + " . Sua média foi de " + media);

    }
}
