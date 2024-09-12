# Escreva um algoritmo para ler 10 números e ao final
# da leitura escrever a soma total dos 10 números
# lidos.
soma_total = 0
for i in range(10):
    numero = float(input(f"Digite o numero {i + 1}:"))
    soma_total += numero
print (f" A soma total dos 10 números lidos é: {soma_total}")
