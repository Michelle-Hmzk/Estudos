import java.util.Scanner;

public class x_SalarioLiquida {
    public static void main(String[] args) {
        Scanner pato = new Scanner(System.in);

        System.out.println("Qual seu salário bruto?");
        double bruto = pato.nextDouble();
        System.out.println("\n");
        
        double INSS = 0.1*bruto;
        double IR = 0.2*bruto;

        System.out.println("Qaunto custa a condução diária de ida da casa ao trabalho?");
        double custo = pato.nextDouble();

        double VT = custo * 2 *  22;
        double desc = INSS + IR + custo + VT;
        double total = bruto - desc;

        System.out.println("Seu salário bruto é de R$" +bruto+ " , tem um total de R$" + desc + "em descontos e receberá um líquido de R$"+ total);
    }
    
}
