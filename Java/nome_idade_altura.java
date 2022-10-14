import java.util.Scanner;

public class nome_idade_altura {
    public static void main(String[] args) {
        Scanner gato = new Scanner(System.in); // aqui eu declaro o gato
        // scanner é uma caixa de texto
        System.out.println("Digite seu nome: ");

        String nome = gato.nextLine(); // aqui que a pessoa recebe o comando
        // next line é para sting e para mais de uma palavra
        // o "next" ele serve para atribuir um valor para a variavel, existem varios
        // tipos de "next"
        
        System.out.println("Idade: ");
        int idade = gato.nextInt();

        System.out.println("Altura: "); //aqui, precisamos colocar com vírgula, mas quando for printado, sai com ponto 
        double altura = gato.nextDouble();

        // System.out.println(nome);
        // System.out.println(idade);
        // System.out.println(altura);
        
        System.out.println("---");
        System.out.println("Nome: " + nome + "\nIdade: " + idade + "\nAltura: " + altura);
    }

}
