import theano
import theano.tensor as T
import theano.tensor.nnet as nnet
import numpy as np

LEARNING_RATE = 0.1
TRAINING_INPUTS = [[0, 0], [0, 1], [1, 0], [1, 1]]
EXPECTED_OUTPUTS = [1, 1, 1, 0]
ITERATIONS = 10000
ITERATION_CHECK_POINT = ITERATIONS / 10 

def get_activation_values(inputs, weights):
    bias = np.array([1], dtype=theano.config.floatX)
    biased_inputs = T.concatenate([inputs, bias])
    weighted_values = T.dot(weights.T, biased_inputs) 
    return nnet.sigmoid(weighted_values)

def get_gradient(cost, weights):
    return weights - (LEARNING_RATE * T.grad(cost, wrt=weights))

def display_neural_network():
    def display(parameter1, parameter2, output):
        print 'f(%d, %d) = %f' % (parameter1, parameter2, output)
 
    for i in range(len(TRAINING_INPUTS)):
        left_operand = TRAINING_INPUTS[i][0]
        right_operand = TRAINING_INPUTS[i][1]
        prediction = feed_forward([left_operand, right_operand])
        display(left_operand, right_operand, prediction)

def train_neural_network(cost_function):
    training_inputs = np.array(TRAINING_INPUTS).reshape(4, 2) 
    expected_output = np.array(EXPECTED_OUTPUTS)
    for i in range(ITERATIONS):
        for k in range(len(training_inputs)):
            cost = cost_function(training_inputs[k], expected_output[k]) 

        if i % ITERATION_CHECK_POINT == 0:
            print "Current Cost: %f" % (cost,)

def main():
    # Create the parameters of our functions
    inputs = T.dvector()
    output = T.dscalar()

    # Create the variables that represents the neural network weights
    hidden_layer_weights = theano.shared(np.array(np.random.rand(3, 3), dtype=theano.config.floatX))
    output_layer_weights = theano.shared(np.array(np.random.rand(4, 1), dtype=theano.config.floatX))

    # Create a function that represents the neural network
    hidden_layer_activations = get_activation_values(inputs, hidden_layer_weights)
    output_layer_value = T.sum(get_activation_values(hidden_layer_activations, output_layer_weights))
    feed_forward = theano.function(inputs=[inputs], outputs=output_layer_value)

    # Create a function that represents the cost function
    cost = (output_layer_value - output)**2
    cost_function = theano.function(inputs=[inputs, output], outputs=cost, updates=[
        (hidden_layer_weights, get_gradient(cost, hidden_layer_weights)),
        (output_layer_weights, get_gradient(cost, output_layer_weights))
    ])

    train_neural_network(cost_function)

    display_neural_network()

main()