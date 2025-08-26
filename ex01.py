totalcompra = 0
prod1000 = 0
prodbarato = 0

while True:
    print("-=-"*20)
    print("     Lojas Super Baratao       ")
    print("-=-"*20)
    prod = str(input("Nome do Produto: "))
    preco = float(input("R$: "))
    continuar = " "
    
    if preco > 1000:
        prod1000 += 1
    if prodbarato == 0 or preco < prodbarato:
        prodbarato = preco
        nomeprodbarato = prod
    totalcompra += preco

    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        print("Programa Encerrado. Obrigado pelas compras! ")
        break

    #resumo final
print("-=-"*20)
print("     Lojas Super Baratao       ")
print("-=-"*20)
print(f"O total da compra foi de R$ {totalcompra:.2f} ")
print(f"Temos {prod1000} produtos custando mais de R$ 1000.00 ")
print(f"O produto mais barato foi {nomeprodbarato} que custa R$ {prodbarato:.2f} ")

