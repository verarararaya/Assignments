# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

def devide(dataset,n):
	length = len(dataset)
	finalset = []
	for i in range(n):
		one_list = dataset[math.floor(i / n * length):math.floor((i + 1) / n * length)]
		finalset.append(one_list)
	return finalset

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	# split = 0.8
	# loadDataset('iris.csv', split, trainingSet, testSet)
	with open('iris.csv', 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	# print('Train set: ' + repr(len(trainingSet)))
	# print('Test set: ' + repr(len(testSet)))
	# generate predictions
	dataset = devide(dataset,5)
	# predictions=[]
	# k = 6
	for x in range(5):
		trainingSet = []
		testSet = []
		predictions = []
		k = 6
		testSet= testSet+ dataset[x]
		for i in range(5):
			if i != x:
				trainingSet = trainingSet+dataset[i]
		for y in range(len(trainingSet)):
			for z in range(4):
				trainingSet[y][z] = float(trainingSet[y][z])
		for y in range(len(testSet)):
			for z in range(4):
				testSet[y][z] = float(testSet[y][z])
		print('Train set: ' + repr(len(trainingSet)))
		print('Test set: ' + repr(len(testSet)))
		for x in range(len(testSet)):
			neighbors = getNeighbors(trainingSet, testSet[x], k)
			result = getResponse(neighbors)
			predictions.append(result)
			print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
		accuracy = getAccuracy(testSet, predictions)
		print('Accuracy: ' + repr(accuracy) + '%')
	
main()
