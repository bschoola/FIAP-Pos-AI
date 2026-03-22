from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

acao1 = [1, 0, 1] #APPL
acao2 = [0, 1, 0] #GOOGL
acao3 = [1, 1, 1] #MSFT
acao4 = [0, 0, 1] #AMZN
acao5 = [1, 1, 0] #TSLA
acao6 = [0, 1, 0] #FB

dados_treino = [acao1, acao2, acao3, acao4, acao5, acao6]
rotulos_treino = [1, 1, 1, 0, 0, 0 ] #1 para subida no preço , 0 para queda no preço


modelo = LinearSVC()
modelo.fit(dados_treino, rotulos_treino)

# Conjunto de teste
teste1 = [1, 0, 0] 
teste2 = [0, 1, 1] 
teste3 = [1, 1, 0]

dados_teste = [teste1, teste2, teste3]
rotulos_teste = [1, 0, 1] # valores reais de subida ou queda

# Fazer previsões
previsoes = modelo.predict(dados_teste)
# Avaliar a acurácia do modelo
taxa_acerto = accuracy_score(rotulos_teste, previsoes)
print("Previsões:", previsoes)
print("Acurácia: %.2f%%" % (taxa_acerto * 100))
