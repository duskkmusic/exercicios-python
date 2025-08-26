print("=" * 50)
print("                  Banco CEV                  ")
print("=" * 50)

saque = int(input("Qual valor você quer sacar? R$ "))

total = saque
cedula50 = total // 50
total = total % 50

cedula10 = total // 10
total = total % 10

cedula1 = total // 1
total = total % 1

print(f"Total de {cedula50} cédulas de R$50")
print(f"Total de {cedula10} cédulas de R$10")
print(f"Total de {cedula1} cédulas de R$1")
print("=" * 50)
print("Volte sempre ao Banco CEV! Tenha um bom dia!")
