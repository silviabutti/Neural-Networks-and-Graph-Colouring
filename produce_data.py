#produce_data.py

#A library to produce training data, validation data, test data for the graph colouring problem

import numpy as np
from sage.graphs.generators.random import RandomGNP
import sage.graphs as graphs

def produce_data(size,p):
  tr_g_mats = []
  tr_c_nums = []
  indices = np.triu_indices(size,k=1)
  for i in range(100000):
    G = RandomGNP(size,p)
    g = G.canonical_label()
    n = g.chromatic_number()
    M = np.array(g.adjacency_matrix())
    M_u = np.array(M[indices])
    tr_g_mats.append(M_u)
    tr_c_nums.append(n)
 training_data = [tr_g_mats ,tr_c_nums]
 
 val_g_mats = []
 val_c_nums = []
  indices = np.triu_indices(size,k=1)
  for i in range(10000):
    G = RandomGNP(size,p)
    g = G.canonical_label()
    n = g.chromatic_number()
    M = np.array(g.adjacency_matrix())
    M_u = np.array(M[indices])
    val_g_mats.append(M_u)
    val_c_nums.append(n)
 validation_data = [val_g_mats ,val_c_nums]
 
 test_g_mats = []
 test_c_nums = []
  indices = np.triu_indices(size,k=1)
  for i in range(10000):
    G = RandomGNP(size,p)
    g = G.canonical_label()
    n = g.chromatic_number()
    M = np.array(g.adjacency_matrix())
    M_u = np.array(M[indices])
    test_g_mats.append(M_u)
    test_c_nums.append(n)
 test_data = [test_g_mats ,test_c_nums]

 return training_data, validation_data, test_data
