frutas = ['maçã', 'banana', 'cereja']
frutas.append('laranja')
print(frutas)  # ['maçã', 'banana', 'cereja', 'laranja']

numeros = (1, 2, 3)
print(numeros[1])  # 2

conjunto = {1, 2, 3, 4, 4}
print(conjunto)  # {1, 2, 3, 4}

aluno = {'nome': 'João', 'idade': 20, 'curso': 'Engenharia'}
print(aluno['nome'])  # João


## controle de fluxo



idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


for i in range(5):
    print(i)  # 0 1 2 3 4

contagem = 0
while contagem < 5:
    print(contagem)
    contagem += 1


## Funções

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Agnes"))  # Olá, Agnes!


def saudacao(nome="mundo"):
    return f"Olá, {nome}!"

print(saudacao())  # Olá, mundo!

dobro = lambda x: x * 2
print(dobro(5))  # 10



# Manipulação de arquivos

with open('arquivo.txt', 'w') as file:
    file.write("Olá, mundo!")

with open('arquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo) # Olá, mundo!


# Modulos e pacotes

import math
print(math.sqrt(16))  # 4.0

# em outro arquivo
# from meu_modulo import soma
# print(soma(3, 4))  # 7


## Exceções

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero.")

def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print(e)


## Compreensão de listas

quadrados = [x ** 2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



## Decoradores

def decorador_saudacao(func):
    def wrapper(*args, **kwargs):
        print("Saudação!")
        return func(*args, **kwargs)
    return wrapper

@decorador_saudacao
def ola(nome):
    print(f"Olá, {nome}!")

ola("Mundo")  # Saudação! Olá, Mundo!


## Context Managers

class GerenciadorDeContexto:
    def __enter__(self):
        print("Entrando no contexto.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo do contexto.")

with GerenciadorDeContexto():
    print("Dentro do bloco with.")