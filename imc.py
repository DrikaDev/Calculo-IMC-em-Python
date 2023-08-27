#1. Função para calcular o imc que vai receber os valores peso e altura como parâmetros
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

#2. Função que recebe o valor IMC calculado na função acima e retorna uma mensagem com base nas faixas de valores do IMC

def interpretar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso."
    elif 18.5 <= imc < 24.9:
        return "peso normal."
    elif 25 <= imc < 29.9:
        return "acima do peso."
    elif 30 <= imc < 34.9:
        return "obesidade grau 1."
    elif 35 <= imc < 39.9:
        return "obesidade grau 2."
    else:
        return "obesidade grau 3 - mórbida!"

#função principal que recebe as informações de entrada do usuário: nome, peso e altura
#calcula o IMC e printa na tela o resultado para o usuário.
def main():
    try:
        print("\n=== Cálculo do IMC ===\n")        
        #o programa recebe os valores de entrada com o input:
        usuario = str(input("Digite seu nome: "))
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura (utilize ponto no lugar da vírgula): "))
        
        #o imc é calculado chamando a função calcular_imc
        imc = calcular_imc(peso, altura)
        #o imc é interpretado com a função interpretar_imc e suas condições
        interpretacao = interpretar_imc(imc)
        
        print(f"\n=> {usuario}, seu IMC é {imc:.2f}, o que indica: {interpretacao}\n")

        print("=== Lembre-se, não existe mágica! ===")
        print("Para manter o peso dentro dos valores desejáveis, a melhor opção é ter alimentação balanceada e praticar atividades físicas regularmente.")
        print("Para maiores dúvidas, consulte um médico!\n")

    #tratamento de exceção que impede que o programa rode caso o usuário não informe os valores corretos
    except ValueError:
        print("Por favor, digite valores com ponto no lugar de vírgula.")

#condição que verifica se o script está sendo executado como o programa principal
#os underlines é uma convenção em Python para indicar que essa variável é uma "variável mágica"
if __name__ == "__main__":
    main()