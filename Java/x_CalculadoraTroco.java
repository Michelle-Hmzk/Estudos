import java.util.Scanner;

public class x_CalculadoraTroco {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Quantos custa o produto?");
        double produto = leitor.nextDouble();
        
        System.out.println("Quantos produtos foram vendidos?");
        int venda = leitor.nextInt();

        System.out.println("Quanto se foi pago?");
        double money = leitor.nextDouble();

        double troco = money - (produto*venda);
        System.out.println("Seu troco será de R$" + troco+ ".");
    }    
}
