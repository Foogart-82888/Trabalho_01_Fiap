Receita = float(input("Pode inserir por favor o valor de suas Vendas?: "))

bonificação_concedida = 10000.00
bonificação_parcial_1 = 7000.00
bonificação_parcial_2 = 333.00
bonificação_ñ_concedida = 00.00


if Receita >= 10000.00:
    bonificação_concedida = 666.00
    print("congratulations! alcançou as metas de 10000,00 ! bonus de R$ 666,00 concedido!")

elif Receita >= 7000.00:
    bonificação_parcial_1 = 333.00
    print("Parabéns quase lá R$ 333,00")

elif Receita >= 5000.00:
    bonificação_parcial_2 = 66.00
    print("Parabéns! observe no que está errando! ganhou R$66,00!")

else: 
    bonificação_ñ_concedida = 00.00
    print("Não foi dessa vez. Obrigado!")