import random

menor = None
maior = None

for i in range(5):
    sorteio = random.randint(0, 10)

    # Atualiza menor e maior
    if menor is None or sorteio < menor:
        menor = sorteio
    if maior is None or sorteio > maior:
        maior = sorteio
    
    print(f" {sorteio} ", end=" > ")

print(f"Fim do Sorteio")
print(f"O menor número sorteado foi {menor}")
print(f"O maior número sorteado foi {maior}")