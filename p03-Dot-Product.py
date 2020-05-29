"""

1D Array = Vector
2D Array = Matrix - Array of vectors
3D Array = Tensor
A tensor is an object that can be represented as an array, not just an array.
"""

import numpy as np

inputs = [4, 5, 6, 7]

weights = [[0.1, 0.3, -0.5, 0.402],
           [0.584, 0.102, -0.808, 0.404],
           [0.27, 0.53, -0.511, 0.22]]  # Matrix of vectors

biases = [5, 2, .5]

output = np.dot(weights, inputs) + biases # First element that is passed is how return value is indexed
print(output)

'''
layer_outputs = []  # outputs of current layer

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
    print(layer_outputs)

'''

