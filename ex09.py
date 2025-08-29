num2 = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num2 = num2
num = int(input("Digite um numero de 0 a 20: "))
while True:
    if num < 0 or num > 20:
        num = int(input("Digite um numero de 0 a 20: "))
    else:
        break
print(f"Voce digitou o numero {num2[num - 1]}!")