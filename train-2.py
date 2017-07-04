import csv
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn import tree

import random

# funcao utilizada para normalizar os seguidores
def normalize(lista):
    mini = min(lista)
    maxi = max(lista)
    return [(x-mini)/(maxi-mini) for x in lista]

def treinamento(input_predict):
# num_feats = 31 # google
    # num_feats = 42 # imagga
    num_feats = 20 # imagga_update
    margem_acerto = 0.8 # para dados normalizados % [0, 100]
    # margem_acerto = 5000 # para dados não normalizados

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

    # sepadando os inputs e outputs e convertendo os dados para float
    data = dados[:,:num_feats].astype(np.float) # consiste nas saidas da api, de acordo com as labels escolhidas, e o numero de followers
    target = dados[:, num_feats].astype(np.float) # consiste no numero de likes, a saida esperada

    # normalizando os dados de input e output
    datanormalizado = normalize(data[:,0])
    # targetnormalizado = np.array(normalize(target))
    targetnormalizado = np.array([((x[1]*100)/x[0]) for x in readerfollowlike[1:].astype(np.float)]) # likes agora eh a porcetagem relativa a qtde de followers
    # print(max(targetnormalizado))
    # print(min(targetnormalizado))
    # a = np.sort(targetnormalizado)
    # print(a)
    # print(targetnormalizado)

    for i in range(1,len(data[0,:])):
        # normalizando os seguidores
        datanormalizado = np.c_[datanormalizado,normalize(data[:,i])]

    maior = 0
    valores = [27, 18, 14]
    vezes = 0 # repetição dos testes

    # treinamento da rede ou arvore
    while(vezes < 60000):
        
        # Base da api Imagga
        # [22, 27, 13, 14, 40] 50% acertos
        # [36,25,8] 50% acertos 
        # [27,7,10] 50% acertos
        # [18, 29, 20, 40] 60% acertos
        # numeros = [36, 39, 36] # tamanho das camadas da MLP
        numeros = [37,76,68,59,74] # tamanho das camadas da MLP

        # Base da api Imagga (update)
        # [43, 39, 19] 95% treinamento 60% teste (!)
        # Base da api do Google
        # [10, 8, 43, 39, 19, 23] 60% certos
        # numeros = [10, 8, 43, 39, 19, 23]

        # Treinando a rede neural
        reg = MLPRegressor(solver='lbfgs',alpha=1e-5, learning_rate="constant", hidden_layer_sizes=numeros, random_state=2)
        reg.fit(datanormalizado[15:], targetnormalizado[15:])

        # verifica quantos acertos no conjunto de treinamento estao classificados errados
        resultado = reg.predict(datanormalizado[15:]).tolist()
        targetlist = targetnormalizado[15:].tolist()
        # resultado = reg.predict(datanormalizado[:139]).tolist()
        # targetlist = targetnormalizado[:139].tolist()
        certos = 0
        for i in range(0,len(resultado)):
            if abs(resultado[i] - targetlist[i]) < margem_acerto:
                certos += 1
                print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
            else:
                print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))

        print ("Conjunto de Teste")
        # resultado = reg.predict(input_predict[:]).tolist()
        # targetlist = target[:10].tolist()
        # certos = 0
        # for i in range(0,len(resultado)):
            # if abs(resultado[i] - targetlist[i]) < margem_acerto:
                # certos += 1
                # print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
            # else:
                # print ('Resultado: %.2f (APLICAÇÃO)' % resultado[i])

        # verifica quantos acertos no conjunto de teste estao classificados errados
        resultado = reg.predict(datanormalizado[:15]).tolist()
        targetlist = targetnormalizado[:15].tolist()
        # resultado = reg.predict(datanormalizado[139:]).tolist()
        # targetlist = targetnormalizado[139:].tolist()
        certos_teste = 0
        for i in range(0,len(resultado)):
            if abs(resultado[i] - targetlist[i]) < margem_acerto:
                certos_teste += 1
                print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
            else:
                print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))
               
        print ((certos*100)/142, "'%' certos")
        print ((certos_teste*100)/15, "'%' certos")
        print (numeros, " camada")
        # if certos > maior:
        #     valores = numeros
        #     maior = certos
        #     print (valores, "melhor")
        
        # print ("valores", valores, "quantidade",maior, "interações",vezes)
        
        # vezes += 1
        vezes = 60000

treinamento([])