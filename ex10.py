lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Valor já digitado.")
    elif valor not in lista:
        lista.append(valor)
    continuar = input("Deseja continuar? (S/N) ").strip().upper()[0]
    if continuar == "N":
        break
print(f"Voce digitou os valores {lista}")