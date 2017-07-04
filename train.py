import csv
import numpy as np
from sklearn.neural_network import MLPRegressor

import random

# num_feats = 31 # google
num_feats = 21 # imagga
margem_acerto = 0.02 # para dados normalizados [0,1]

# lendo os dados vindo da api
file = open('data_input_update.csv', 'r')
reader = csv.reader(file, delimiter=',')

# lendo os dados de followers e likes
followlike = open('followlikes_update.csv', 'r')
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

def denormalize(lista,target):
    mini = min(target)
    maxi = max(target)
    return [(x * (maxi - mini)) + mini for x in lista]

# sepadando os inputs e outputs e convertendo os dados para float
data = dados[:,:num_feats].astype(np.float) # consiste nas saidas da api, de acordo com as labels escolhidas, e o numero de followers
target = dados[:, num_feats].astype(np.float) # consiste no numero de likes, a saida esperada

# normalizando os dados de input e output
datanormalizado = normalize(data[:,0])
targetnormalizado = np.array(normalize(target))

for i in range(1,len(data[0,:])):
    # normalizando os seguidores
    datanormalizado = np.c_[datanormalizado,normalize(data[:,i])]

print(datanormalizado)
print(targetnormalizado)

a = np.less(target, 100000)
datanormalizado = np.extract(a, datanormalizado)
targetnormalizado = np.extract(a, targetnormalizado)
print(datanormalizado)
print(targetnormalizado)
# for i in range(0,len(target[:])):
    # if target[i] < 100000:


maior = 0
valores = [27, 18, 14]
vezes = 0 # repetição dos testes

# treinamento da rede ou arvore
def treinamento(data, target, target_a):
    global vezes, valores, maior
    while(vezes < 60000):
        
        numeros = []
        quant=random.randint(2,15)
        for i in range(0,quant):
            numeros.append(random.randint(3,120))

        # Base da api Imagga
        # [22, 27, 13, 14, 40] 50% acertos
        # [36,25,8] 50% acertos 
        # [27,7,10] 50% acertos
        # [18, 29, 20, 40] 60% acertos
        # numeros = [18, 29, 20, 40] # tamanho das camadas da MLP

        # Base da api do Google
        # [10, 8, 43, 39, 19, 23] 60% certos
        # numeros = [10, 8, 43, 39, 19, 23]
        numeros = [67, 20, 5, 106, 80, 46, 42, 37, 101, 29, 20, 45, 94]
        # [101, 54, 106]
        # [21, 55, 24, 26, 85, 39] 5/10
        # [85, 4, 106] 6/10

        # Treinando a rede neural
        reg = MLPRegressor(
            solver='adam',
            alpha=1e-9,
            activation='tanh',
            # learning_rate='adaptive',
            hidden_layer_sizes=numeros,
            random_state=200)
        reg.fit(data[40:], target[40:])

        # verifica quantos acertos no conjunto de treinamento estao classificados errados
        # resultado = reg.predict(data[10:]).tolist()
        # targetlist = target[10:].tolist()
        # for i in range(0,len(resultado)):
        #     if abs(resultado[i] - targetlist[i]) < margem_acerto:
        #         print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
        #     else:
        #         print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))

        print ("Conjunto de Teste")
        # verifica quantos acertos no conjunto de teste estao classificados errados
        resultado = reg.predict(data[:40]).tolist()
        resultado_a = np.array(denormalize(resultado,target_a))
        targetlist = target[:40].tolist()
        targetlist_a = np.array(denormalize(targetlist,target_a))
        certos = 0
        for i in range(0,len(resultado)):
            if abs(resultado[i] - targetlist[i]) < margem_acerto:
                certos += 1
                print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado_a[i], targetlist_a[i]))
            else:
                print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado_a[i], targetlist_a[i]))

        print (numeros, "atual")
        if certos > maior:
            valores = numeros
            maior = certos
            print (valores, "melhor")
        
        print ("valores", valores, "quantidade",maior, "interações",vezes)
        
        # vezes += 1
        vezes = 60000

# treinamento(datanormalizado, targetnormalizado, target)