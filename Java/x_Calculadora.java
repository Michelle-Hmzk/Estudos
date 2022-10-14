import java.util.Scanner;

public class x_Calculadora {
 public static void main(String[] args) {
    Scanner gato = new Scanner(System.in);

    System.out.println("Digite um número: ");
    double numero = gato.nextDouble();
    System.out.println("\n");

    System.out.println("Digite outro número: ");
    double numero1 = gato.nextDouble();
    System.out.println("\n");

    double soma = numero + numero1;
    double subtracao = numero - numero1;
    double mult = numero * numero1;
    double div = numero/numero1;

    System.out.println("Resultado da soma: " + "\n" + soma + "\n");
    System.out.println("Resultado da subtração: " + "\n" + subtracao + "\n");
    System.out.println("Resultado da multiplicação: " + "\n" + mult + "\n");
    System.out.println("Resultado da divisão: " + "\n" + div + "\n");
 }  
}
