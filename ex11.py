lista = []
for i in range(5):
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    p = lista.index(valor)
    print(f"Adicionado na posição {p}")
lista.sort()
print(f"{lista}")