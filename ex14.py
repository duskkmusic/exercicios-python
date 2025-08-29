expressao = str(input("Digite a expressao: "))

def parenteses_balanceados(expressao):

    pilha = []
    for char in expressao:
        if char == "(":
            pilha.append(char)
        elif char == ")":
            if not pilha:  # tem ")" sem "(" correspondente
                return False
            pilha.pop()
    return len(pilha) == 0


if parenteses_balanceados(expressao):
    print("Expressão válida")
else:
    print("Expressão inválida")