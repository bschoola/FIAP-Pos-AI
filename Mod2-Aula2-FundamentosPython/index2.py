def saudacao(parametro):
    print("Olá, seja bem-vindo(a)!" + " " + parametro)
    return "Saudação enviada com sucesso!"

def somar(a, b):
    result = a + b
    print("O resultado da soma é: " + str(result))

retorno = saudacao("João")
print(retorno)
somar(5, 3)