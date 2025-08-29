lista = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    
    continuar = str(input("Deseja continuar? (S/N) ")).strip().upper()[0]
    if continuar == "N":
        break
              
print(f"Voce digitou {len(lista)} elementos!")
print(f"Os valores em ordem decrescente sao: {sorted(lista, reverse=True)}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista.")
else:
    print(f"O valor 5 não faz parte da lista.")
print("Programa encerrado.")
