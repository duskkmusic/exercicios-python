comidas = ("Hamburguer", "Pizza", "Salada", "Suco", "Fruta", "Batata Frita", "Sorvete", "Bolo", "Pudim", "Biscoito", "Torta", "Pipoca", "Brigadeiro", "Bacon", "Coxinha", "Pastel", "Tapioca", "Bolo de Rolo", "Pavê", "Churrasco", "Lasanha")
numero = int(input("Digite um numero de 0 a 20: "))
while True:
    if 0 <= numero <= 20:
        break
    numero = int(input("Tente novamente. Digite um numero de 0 a 20: "))
print(f"Comida escolhida: {comidas[numero]}")