import java.util.Scanner;

public class x_Idade {
    public static void main(String[] args) {
        Scanner transporte = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        String nome = transporte.nextLine();

        System.out.println("Olá " + nome + " ! Qual o ano de seu nascimento?" );
        int year = transporte.nextInt();

        int anos = 2030 - year;

        System.out.println("Em 2030, você terá " + anos + " anos");
    }
    
}
