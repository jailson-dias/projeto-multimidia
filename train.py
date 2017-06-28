import csv
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import scale

import random

num_feats = 31
margem_acerto = 0.02

# lendo os dados vindo do google
file = open('data_input_google.csv', 'r')
reader = csv.reader(file, delimiter=',')

# lendo os dados de follow e likes
followlike = open('followlikes.csv', 'r')
readerfollowlike = csv.reader(followlike, delimiter=',')

# colocando os dados em um array do numpy
reader = np.array(list(reader))
readerfollowlike = np.array(list(readerfollowlike))

# juntando os dados vindos do google com os seguidores e curtidas
dados = np.c_[reader[1:], readerfollowlike[1:]]


# zero = []
# for i, d in enumerate(dados):
#     if np.count_nonzero(d == '0') > 18:
#         zero.append(i)

# dados = np.array(filter(lambda x: np.count_nonzero(x == '0') >20, dados))
# print (dados)
# dados = np.delete(dados, zero, 0)

# zero = []
# for i, d in enumerate(dados[:,-2]):
#     if float(d)>4000000 or float(d)<100000:
#         zero.append(i)

# print (zero)
# dados = np.delete(dados, zero, 0)
print (len(dados))
# print (len(dados))

# """
# funcao utilizada para normalizar os seguidores
def normalize(lista):
    mini = min(lista)
    maxi = max(lista)
    return [(x-mini)/(maxi-mini) for x in lista]

# sepadando os inputs e outputs e convertendo os dados para float
data = dados[:,:num_feats].astype(np.float)
target = dados[:, num_feats].astype(np.float)

# datanormalizado = normalize(data[:,0])
datanormalizado = np.c_[data[:,:-1],normalize(data[:,-1])]
targetnormalizado = np.array(normalize(target))
# print(targetnormalizado)

# for i in range(1,len(data[0,:])):
#     # normalizando os seguidores
#     datanormalizado = np.c_[datanormalizado,normalize(data[:,i])]

# activation= 'tanh'
# normalizado = np.c_[normalizado, data[:,1]]
# print (datanormalizado)
# """
maior = 0
valores = [27, 18, 14]

vezes = 0

def treinamento(data, target):
    global vezes, valores, maior
    while(vezes < 60000):
        
        # Base da api de marcos
        # numeros = [22, 27, 13, 14, 40] # 50% certos [36,25,8] # 50% certos [27,7,10] 50%
        # [18, 29, 20, 40] 60% certos

        # Base da api do google
        # [10, 8, 43, 39, 19, 23] 60% certos
        numeros = [10, 8, 43, 39, 19, 23]
        # quant = random.randint(3,6)
        # for i in range(0,quant):
        #     numeros.append(random.randint(5,45))

        # Treinando a rede neural
        reg = MLPRegressor(solver='lbfgs',alpha=1e-5, learning_rate="constant", hidden_layer_sizes=numeros, random_state=2)
        reg.fit(data[10:], target[10:])


        # print (reg.loss_)
        # verifica quantos acertos no conjunto de treinamento estao classificados errados
        resultado = reg.predict(data[10:]).tolist()
        targetlist = target[10:].tolist()
        for i in range(0,len(resultado)):
            if abs(resultado[i] - targetlist[i]) < margem_acerto:
                print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
            else:
                print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))


        print ("Conjunto de Teste")

        # print (data[:5], "\n\n")
        # print (np.c_[data[:5],data[28:]], "\n\n")
        # verifica quantos acertos no conjunto de teste estao classificados errados
        resultado = reg.predict(data[:10]).tolist()
        # print (data[:10])
        targetlist = target[:10].tolist()#  + target[:10].tolist()
        # print (reg.score(data[28:],target[28:]))
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
    # if vezes < 6000:
    #     treinamento(data, target)

treinamento(datanormalizado, targetnormalizado)
# """