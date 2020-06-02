"""
Simple operations like matrix multiplication allow for use of gpus.
Batches allow for better generalization when fitting line. Showing too many samples at once can cause overfitting
Adding more batches does increase number of neurons
Transposing a matrix is just swapping the rows and columns
"""

import numpy as np

np.random.seed(0)

X = [[0.5, 1.5, 2.2, 3.3],
     [3.0, 4.67, 1.1, -0.2],
     [-0.8, 3.2, 4.7, 3.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)  # weights that will be size of n_inputs * how many neurons
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4, 5)  # output from layer one is the input to layer 2
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
# print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)