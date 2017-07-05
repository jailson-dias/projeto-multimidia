import csv
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn import tree
from sklearn.externals import joblib

import random

input_a = [24.318968319154468,23.33598215943447,19.774264619557073,24.052204755202222,26.36642707936843,14.298552935235646,15.657867305427178,25.465725748241514,15.345421383918884,18.970802325172972,15.407712471081492,16.950958409006233,14.931179814924938,15.828541301254859,18.281967569992453,10.407829410327984,16.31680185797532,15.42009149657441,25.061627541600263,13.565228597838228,1400000]

# funcao utilizada para normalizar os seguidores
def normalize(lista):
    mini = min(lista)
    maxi = max(lista)
    return [(x-mini)/(maxi-mini) for x in lista]

def treinamento(input_predict):
    num_feats = 21
    # lendo os dados vindo da api
    file = open('C:\\Users\\barre\\Documents\\projeto-multimidia\\projeto-multimidia\\data_input_update.csv', 'r')
    reader = csv.reader(file, delimiter=',')

    # lendo os dados de followers e likes
    followlike = open('C:\\Users\\barre\\Documents\\projeto-multimidia\\projeto-multimidia\\followlikes_update.csv', 'r')
    readerfollowlike = csv.reader(followlike, delimiter=',')

    # colocando os dados em um array do numpy
    reader = np.array(list(reader))
    readerfollowlike = np.array(list(readerfollowlike))

    # juntando os dados vindos da api com os seguidores e curtidas
    dados = np.c_[reader[1:], readerfollowlike[1:]]

    print (len(dados))

    # """

    # sepadando os inputs e outputs e convertendo os dados para float
    data = dados[:,:num_feats].astype(np.float) # consiste nas saidas da api, de acordo com as labels escolhidas, e o numero de followers
    target = dados[:, num_feats].astype(np.float) # consiste no numero de likes, a saida esperada

    data = data.tolist()
    data.append(input_predict)
    data = np.array(data)

    # normalizando os dados de input e output
    datanormalizado = normalize(data[:,0])

    targetnormalizado = np.array([((x[1]*100)/x[0]) for x in readerfollowlike[1:].astype(np.float)]) # likes agora eh a porcetagem relativa a qtde de followers


    for i in range(1,len(data[0,:])):
        # normalizando os seguidores
        datanormalizado = np.c_[datanormalizado,normalize(data[:,i])]

    maior = 0
    valores = [27, 18, 14]
    vezes = 0 # repetição dos testes

    # camada escondida da rede (tamanho, qtde_neuronios)
    numeros = [4, 89]

    # Treinando a rede neural
    reg = MLPRegressor(
        solver='adam',
        alpha=1e-9, 
        activation='tanh',
        hidden_layer_sizes=numeros, 
        random_state=200)
    reg.fit(datanormalizado[:144], targetnormalizado[:])

    print ("RESULTADO")
    resultado = reg.predict(datanormalizado[144].reshape(1, -1)).tolist()
    print(resultado)
    # print(input_predict[20])
    # print(np.round((resultado[0]/100) * input_predict[20],decimals=2))

    return (np.round((resultado[0]/100) * input_predict[20],decimals=2))

# treinamento(input_a)