import csv
import numpy as np
import random

# Start with a random city
# Establish all nodes as next possible cities
# for each ant, keep track of visited cities
# terminate ant path - update pheromones - when visited all 29 cities

random.seed()

def createTour(matrix):
  tour = []
  while (len(tour) < 29):
    tempVal = random.randint(0, 28)
    while tempVal in tour:
      tempVal = random.randint(0, 28)
    tour.append(tempVal)
  return tour

def readMatrix(fileName):
  matrix = []
  with open(fileName, mode='r', encoding='utf-8-sig') as inp:
    reader = csv.reader(inp, delimiter=',')
    for row in reader:
      matrix.append(list(map(int, row)))
  return matrix

fileName = 'bays29.csv'
matrix = readMatrix(fileName)

print(createTour(matrix))
