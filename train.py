import csv
import numpy as np
from sklearn.neural_network import MLPRegressor

num_feats = 26

file = open('data_input.csv', 'r')
reader = csv.reader(file, delimiter=',')

followlike = open('followlikes.csv', 'r')
readerfollowlike = csv.reader(followlike, delimiter=',')

reader = np.array(list(reader))
readerfollowlike = np.array(list(readerfollowlike))

dados = np.c_[reader[1:], readerfollowlike[1:]]





data = dados[:,:num_feats].astype(np.float)
target = dados[:, num_feats].astype(np.float)
# print (data.tolist())
# print ("\n\n\n",target.tolist())
reg = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
reg.fit(data, target)

print (reg)
