#basic neural network layer
inputs = [1,3,5]
weights = [ [3.5,0.9,5.6],
			[0.6,3.5,2.6],
			[0.5,9.2,8.8] ] #every layer has input neurons, each of which has an associated weight

bias = [2,5,0.6] #every layer has a bias 

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights,bias):
	neuron_output = 0 #Output of given neuron
	for n_input, weight in zip(inputs, neuron_weights):
		neuron_output += n_input*weight
	neuron_output += neuron_bias
	layer_outputs.append(neuron_output)

print(layer_outputs)


