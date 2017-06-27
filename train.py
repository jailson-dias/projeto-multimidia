import csv
import numpy as np
from sklearn.neural_network import MLPRegressor

num_feats = 1

file = open('trainning_scores.csv', 'r')
reader = csv.reader(file, delimiter=',')
reader = np.array(list(reader))
data = reader[:,0:num_feats]
target = reader[:, num_feats]

reg = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
reg.fit(data, target)
