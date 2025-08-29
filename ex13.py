lista = []
par = []
impar = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)

    if valor % 2 == 0:
        par.append(valor)

    elif valor % 2 == 1:
        impar.append(valor)

    continuar = str(input("Deseja continuar? (S/N) ")).strip().upper()[0]
    if continuar == "N":
        break
print("-= Lista =-")
print(f"A lista completa e {lista}")
print(f"A lista de pares e {par}")
print(f"A lista de impares e {impar}")