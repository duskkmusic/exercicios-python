galera = []
menorp = maiorp = None

while True:
    dados = []  # cria uma lista nova para cada pessoa
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    galera.append(dados[:])

    # Atualiza maior e menor
    if maiorp is None or dados[1] > maiorp:
        maiorp = dados[1]
    if menorp is None or dados[1] < menorp:
        menorp = dados[1]

    c = str(input("Deseja continuar? (S/N) ")).strip().upper()[0]
    if c == "N":
        break

print(f"\nAo todo, você cadastrou {len(galera)} pessoas.")

for p in galera:
    if p[1] == maiorp:
        print(f"O maior peso foi de {maiorp}kg. Peso de {p[0]}.")
    if p[1] == menorp:
        print(f"O menor peso foi de {menorp}kg. Peso de {p[0]}.")
print("Programa encerrado.")