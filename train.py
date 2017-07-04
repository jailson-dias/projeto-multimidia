import csv
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.externals import joblib

import random

# num_feats = 31 # google
num_feats = 42 # imagga
margem_acerto = 0.02 # para dados normalizados [0,1]

# lendo os dados vindo da api
file = open('data_input.csv', 'r')
reader = csv.reader(file, delimiter=',')

# lendo os dados de followers e likes
followlike = open('followlikes.csv', 'r')
readerfollowlike = csv.reader(followlike, delimiter=',')

# colocando os dados em um array do numpy
reader = np.array(list(reader))
readerfollowlike = np.array(list(readerfollowlike))

# juntando os dados vindos da api com os seguidores e curtidas
dados = np.c_[reader[1:], readerfollowlike[1:]]

print (len(dados))

# """
# funcao utilizada para normalizar os seguidores
def normalize(lista):
    mini = min(lista)
    maxi = max(lista)
    return [(x-mini)/(maxi-mini) for x in lista]

# sepadando os inputs e outputs e convertendo os dados para float
data = dados[:,:num_feats].astype(np.float) # consiste nas saidas da api, de acordo com as labels escolhidas, e o numero de followers
target = dados[:, num_feats].astype(np.float) # consiste no numero de likes, a saida esperada

# normalizando os dados de input e output
datanormalizado = normalize(data[:,0])
targetnormalizado = np.array(normalize(target))

for i in range(1,len(data[0,:])):
    # normalizando os seguidores
    datanormalizado = np.c_[datanormalizado,normalize(data[:,i])]

maior = 0
valores = [27, 18, 14]
vezes = 0 # repetição dos testes

# treinamento da rede ou arvore
def treinamento(data, target):
    global vezes, valores, maior
    while(vezes < 60000):
        
        # Base da api Imagga
        # [22, 27, 13, 14, 40] 50% acertos
        # [36,25,8] 50% acertos 
        # [27,7,10] 50% acertos
        # [18, 29, 20, 40] 60% acertos
        numeros = [18, 29, 20, 40] # tamanho das camadas da MLP

        # Base da api do Google
        # [10, 8, 43, 39, 19, 23] 60% certos
        # numeros = [10, 8, 43, 39, 19, 23]

        # Treinando a rede neural
        reg = MLPRegressor(solver='lbfgs',alpha=1e-5, learning_rate="constant", hidden_layer_sizes=numeros, random_state=2)
        reg.fit(data[10:], target[10:])
        # save model
        joblib.dump(reg, 'model.pkl') 
        

        # verifica quantos acertos no conjunto de treinamento estao classificados errados
        resultado = reg.predict(data[10:]).tolist()
        targetlist = target[10:].tolist()
        for i in range(0,len(resultado)):
            if abs(resultado[i] - targetlist[i]) < margem_acerto:
                print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
            else:
                print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))

        print ("Conjunto de Teste")
        # verifica quantos acertos no conjunto de teste estao classificados errados
        resultado = reg.predict(data[:10]).tolist()
        targetlist = target[:10].tolist()
        certos = 0
        for i in range(0,len(resultado)):
            if abs(resultado[i] - targetlist[i]) < margem_acerto:
                certos += 1
                print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
            else:
                print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))

        print (numeros, "atual")
        if certos > maior:
            valores = numeros
            maior = certos
            print (valores, "melhor")
        
        print ("valores", valores, "quantidade",maior, "interações",vezes)
        
        # vezes += 1
        vezes = 60000

treinamento(datanormalizado, targetnormalizado)