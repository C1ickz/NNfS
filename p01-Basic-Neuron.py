"""
Basic neuron creation
"""
inputs = [1.4, 5.4, 2.7]  # Outputs from three neurons in previous layer
weights = [5.2, 1.5, 6.5]  # Each unique input has its own unique weight
bias = 3  # every unqiue neuron has a unique bias

# output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias # inputs*weights + bias
output = sum(input * weight for input, weight in zip(inputs, weights)) + bias
print(output)

