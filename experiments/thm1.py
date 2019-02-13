"""
In this file we generate our set of states until H(Z) drops below 
epsilon for varying levels of epsilon. We analyze results over
various input sets. 
"""

import numpy as np 
from scipy.stats import entropy
import sys
from random import randint
import matplotlib.pyplot as plt
import pandas as pd



# Routine to read in DS from data.txt file 
# @params filepath of structured data
# @return X. X is a dictoinary key'd by x valued by a list of states 
def read_in_x(filepath, start, end): 
	X = {}

	offset = 0
	states = []
	with open(filepath) as infile:
    for line in infile:
        if line[0:5] == 'block':
        	X[input_block] = states

        	states = []
        	input_block = line[7:]
        	offset = 0
        else if offset >= start and offset <= end: 
        	states.append(line)
        
        offset = offset + 1

	return X


def read_in_x_b(filepath, b):
	b_start = b[0]
	b_end = b[1]
	return read_in_x(b_start, b_end)


#computes the entropy given the list Z
def computeEntropy(Z, base):
	value,counts = np.unique(labels, return_counts=True)
  	return entropy(counts, base=base)


def theorem_1_routine(e, X):
	entropy = sys.maxsize
	N = len(X)
	Z = []

	while entropy > e:
		rand_index = randint(0, N)
		inputs = X.keys()
		x = inputs[rand_index]
		z = X[x]
		Z.extend(z)
		entropy = computeEntropy(Z, 2)


	return entropy #filler 




"""
Given a block, computes the number of examples 
needed to get H(Z) < epsilon over datasets
"""
def computeBlock(b, epsilon):
	dataset_paths = ['data0.txt', 'data1.txt', 'data2.txt']

	for ds_path in dataset_paths:
		res = computeDataset(ds_path, b, epsilon)
		plot(res)

"""
Given a dataset, computes the number of examples 
needed to get H(Z) < epsilon
"""
def computeDataset(ds_path, b, epsilon):
	res = dict()
	epsilon_res = []


	for e in epsilon: 
		X = read_in_x_b(ds_path, b)
		m = theorem_1_routine(e, X)
		epsilon_res.append(m)

	res[ds_path] = epsilon_res

	return res


#generates a line plot over values of epsilon 
def plot(res, epsilon):
	df=pd.DataFrame({'x': epsilon, 'y1': res['data0.txt'], 'y2': res['data1.txt'], 'y3': res['data2.txt'] })
	
	# multiple line plot
	plt.plot( 'x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label="data0.txt")
	plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2, label="data1.txt")
	plt.plot( 'x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="data2.txt")
	plt.legend()




if __name__ == "__main__":
	epsilon = np.arange(0, 1, step=.05)
	blocks = [[0, 15], [16,31], [32,47], [48,63]]

	for b in blocks:
		computeBlock(b, epsilon)

	









