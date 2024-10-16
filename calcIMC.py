#Calculo da conta do IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#Classificador de IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <+ imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
    

def main():
    print("Calculadora de IMC")

#Inserir os dados de peso e altura!!

peso = float(input("Digite seu peso : ")) 
altura = float(input("Digite sua altura : "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"\nSeu IMC é : {imc: .2f}")
print(f"Classificão: {classificacao} ")

if __name__=="__main__":
    main()