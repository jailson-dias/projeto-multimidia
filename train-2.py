import csv
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn import tree
from sklearn.externals import joblib

import random

# funcao utilizada para normalizar os seguidores
def normalize(lista):
    mini = min(lista)
    maxi = max(lista)
    return [(x-mini)/(maxi-mini) for x in lista]

def treinamento(input_predict):
# num_feats = 31 # google
    # num_feats = 42 # imagga
    num_feats = 21 # imagga_update
    margem_acerto = 0.3 # para dados normalizados % [0, 100]
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
    # print(data)
    # print(target)
    # normalizando os dados de input e output
    datanormalizado = normalize(data[:,0])
    # targetnormalizado = np.array(normalize(target))
    # targetnormalizado = np.array(target)
    # readerfollowlike = readerfollowlike[1:].astype(np.float)
    targetnormalizado = np.array([((x[1]*100)/x[0]) for x in readerfollowlike[1:].astype(np.float)]) # likes agora eh a porcetagem relativa a qtde de followers
    # print(targetnormalizado)
    # print(max(targetnormalizado))
    # print(min(targetnormalizado))
    # a = np.sort(targetnormalizado)
    # print(a)
    # print(targetnormalizado)

    for i in range(1,len(data[0,:])):
        # normalizando os seguidores
        datanormalizado = np.c_[datanormalizado,normalize(data[:,i])]
    # print(datanormalizado[:,:num_feats])

    maior = 0
    valores = [27, 18, 14]
    vezes = 0 # repetição dos testes

    # treinamento da rede ou arvore
    while(vezes < 60000):

        # numeros = []
        # quant=random.randint(2,15)
        # for i in range(0,quant):
        #     numeros.append(random.randint(3,120))
        
        # Base da api Imagga
        # numeros = [22, 27, 13, 14, 40] # 53% acertos
        # numeros = [36,25,8] # 53% acertos 
        # numeros = [27,7,10] # 53% acertos
        # numeros = [18, 29, 20, 40] # 53% acertos
        # numeros = [36, 39, 36] # 53% acertos
        # numeros = [37,76,68,59,74] # 60% acertos

        # Base da api Imagga (update)
        # numeros = [43, 39, 19] # 53% teste
        # Base da api do Google
        # numeros = [10, 8, 43, 39, 19, 23] # 60% certos
        # numeros = [37,76,68] # 66,6% acertos
        # numeros = [39, 19, 23] # 60% acertos
        # numeros = [37,33,19] # 66,6% acertos
        # numeros = [37,33,37,76,68] # 73,3% acertos

        # numeros = [50, 20, 72, 32, 16, 17, 29, 32, 78, 82, 77, 94, 97, 75]
        # numeros = [15, 6, 5]
        # numeros = [20,37]
        # numeros = [4, 89]
        # numeros = [23,43,12,70]
        # numeros = [39,38,52,44,3,55,70]
        # numeros = [38, 61, 48, 22, 24, 55, 60, 40, 58, 5, 80, 5, 49]
        # numeros = [95, 48, 103, 69, 28, 41, 6, 9, 37, 59, 55, 9] # 40/144
        # numeros = [51, 64, 70, 6] # 43/144
        numeros = [116, 103, 28, 13, 27, 5] # 63/144 (0.3)

        # Treinando a rede neural
        reg = MLPRegressor(
            solver='adam',
            alpha=1e-9, 
            activation='tanh',
            # learning_rate="tanh", 
            hidden_layer_sizes=numeros, 
            random_state=200)
        reg.fit(datanormalizado[:], targetnormalizado[:])
        # joblib.dump(reg, 'model.pkl')

        # verifica quantos acertos no conjunto de treinamento estao classificados errados
        # resultado = reg.predict(datanormalizado[15:]).tolist()
        # targetlist = targetnormalizado[15:].tolist()
        # resultado = reg.predict(datanormalizado[:]).tolist()
        # targetlist = targetnormalizado[:].tolist()
        # certos = 0
        # quant_certos = len(targetlist)
        # for i in range(0,len(resultado)):
            # if abs(resultado[i] - targetlist[i]) < margem_acerto:
                # certos += 1
                # print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
            # else:
                # print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))

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
        # resultado = reg.predict(datanormalizado[:15]).tolist()
        # targetlist = targetnormalizado[:15].tolist()
        followerslist = readerfollowlike[1:,0].astype(np.float).tolist()
        # print(followerslist)
        resultado = reg.predict(datanormalizado[:]).tolist()
        targetlist = targetnormalizado[:].tolist()
        certos_teste = 0
        quant_teste = len(targetlist)
        for i in range(0,len(resultado)):
            if abs(resultado[i] - targetlist[i]) < margem_acerto:
                certos_teste += 1
                # print ('Resultado: %.2f, Esperado: %.2f (Certo)' % (resultado[i], targetlist[i]))
                print ('Resultado: %.2f --> %.2f, Esperado: %.2f --> %.2f (Certo)' % ((resultado[i]/100)*followerslist[i], resultado[i], (targetlist[i]/100)*followerslist[i], targetlist[i]))
            else:
                # print ('Resultado: %.2f, Esperado: %.2f         (Errado)' % (resultado[i], targetlist[i]))
                print ('Resultado: %.2f --> %.2f, Esperado: %.2f --> %.2f        (Errado)' % ((resultado[i]/100)*followerslist[i], resultado[i], (targetlist[i]/100)*followerslist[i], targetlist[i]))
               
        # print ((certos*100)/quant_certos, "'%' certos")
        print ((certos_teste*100)/quant_teste, "'%' certos")
        print (numeros, " camada")
        if certos_teste > maior:
            valores = numeros
            maior = certos_teste
            print (valores, "melhor")
        
        print ("valores", valores, "quantidade",maior, "interações",vezes)
        
        # vezes += 1
        vezes = 60000

treinamento([])