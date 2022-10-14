import java.util.Scanner;

public class x_CadastroUsuario {
    public static void main(String[] args) {
        Scanner gato = new Scanner(System.in);

        System.out.println("Digite seu login: ");
        String login = gato.nextLine();

        System.out.println("Digite sua senha: ");
        String senha = gato.nextLine();

        System.out.println("Posso errar: ");
        int erro =  gato.nextInt();

        System.out.println("Seu login é " + login + " e sua senha é " + senha + ".Você tem " + erro + " tentativas antes de ser bloqueado.");
    }
}
