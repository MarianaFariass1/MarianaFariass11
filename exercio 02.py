litros = float(input("Quantos litros: "))
tipo = input("Qual o combustível: ")
valor = 0
if tipo == "G" or tipo == "g":
    valor = litros*5.8
    print(f"voce abasteceu com {tipo} e gastou {valor}")
elif tipo == "E" or tipo == "e":
    valor = litros*4.9
    print(f"voce abasteceu com {tipo} e gastou {valor}")
if tipo == "D" or tipo == "d":
    valor = litros*5.6
    print(f"voce abasteceu com {tipo} e gastou {valor}")
else:
    print( "combustível inválido")
