# PROJETO CALCULADORA DE DESCONTO EM PORCENTAGEM!!!

# MENCIONAR O VALOR DO DESCONTO

valor_do_produto = float(input("Digite o valor do Produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# verificar se o percentual do desconto está no limite de 0 a 100!!!

if percentual_desconto < 0 or percentual_desconto > 100:
    print("O percentual de desconto deve estar entre 0 e 100.")
else:
    # calcular o desconto
    desconto = valor_do_produto * (percentual_desconto / 100)
    valor_final = valor_do_produto - desconto
    
    # valor final da compra
    print(f"Seu desconto é: R$ {desconto:.2f}")
    print(f"Valor final da compra: R$ {valor_final:.2f}")


