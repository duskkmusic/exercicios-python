valor = [int(input(f"Digite um valor para a posicao {i}: ")) for i in range(5)]
print("-=-"*30)
print(f"Voce digitou os valores {valor} ")

menor = min(valor)
maior = max(valor)

print(f"O menor valor digitado foi {menor} na posicao {valor.index(menor)}")
print(f"O maior valor digitado foi {maior} na posicao {valor.index(maior)}")