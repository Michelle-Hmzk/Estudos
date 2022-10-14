import java.util.Scanner;

public class x_Calorias {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Qual seu nome?");
        String nome = leitor.nextLine();

        System.out.println("Por quanto tempo se aqueceu?");
        int aquecimento = leitor.nextInt();

        System.out.println("Por quanto tempo fez aeróbicos?");
        int aerobicos = leitor.nextInt();
        
        System.out.println("Por quanto tempo fez musculação?");
        int musc = leitor.nextInt();

        int temp = aquecimento + aerobicos + musc;
        int calorias = aquecimento*12 + aerobicos*20 + musc*25;
        
        System.out.println("Olá " + nome + " ! Vôce fez um total de " + temp + " minutos de exercícios e perdeu cerca de " + calorias + "calorias." );
    }
    
}
