def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

operacoes = {
    "+": soma,
    "-": subtracao,
    "*": multiplicacao,
    "/": divisao
}

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op in operacoes:
    resultado = operacoes[op](a, b)
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida.")
