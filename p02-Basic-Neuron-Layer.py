"""
This module shows a layer that contains three neurons.
Each of the neurons has four inputs

"""
# input to a neuron could either be from the true input layer, something like a sensor or group of, or output from neurons themselves
inputs = [4, 5, 6, 7] # Can't change inputs directly but weights and biases can be tuned to affect output values

weights1 = [0.1, 0.3, -0.5, 0.402]
weights2 = [0.584, 0.102, -0.808, 0.404]
weights3 = [0.27, 0.53, -0.511, 0.22]
bias1 = 5
bias2 = 2
bias3 = .5
weights = [[0.1, 0.3, -0.5, 0.402], [0.584, 0.102, -0.808, 0.404], [0.27, 0.53, -0.511, 0.22]]
biases = [5, 2, .5]
output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]

print(output)
