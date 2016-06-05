from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import SGD
from keras.datasets import mnist
from keras.utils import np_utils

print "Creating model..."

# This is the old model. It has an 91% accuracy. Here's the design:
# (1) The input layer has 784 inputs for each pixel of the image.
# (2) The hidden layer has 32 nodes. We have 25088 connections and accordingly 25088 weights. Each node calculates a
#     linear combination of its inputs and weights and feeds that value into a rectified linear function to avoid the
#     vanishing gradient problem. A ReLU also creates a sparse network since nodes that calculate a negative linear
#     combination will output 0.
# (3) The dropout layer matches the output of the hidden layer, which is 32. During training, we have a 50% probability
#     of dropping a node to avoid co-dependence and co-adaptation between nodes.
# (4) The output layer has 10 nodes, one for each digit, and used softmax as the activation function to calculate
#     probabilities.
# model = Sequential([
#     Dense(32, input_dim=784),
#     Activation('relu'),
#     Dropout(0.5),
#     Dense(10),
#     Activation('softmax')
# ])

# The new model has a 99% accuracy. Here's the design:
# (1) The input layer takes into account shape by expecting a 28 * 28 matrix input. This represents the input image.
# (2) The convolution layer applies 32 filters of size 3 * 3 with a stride of 1, which enables the model to perceive
#     location and distance by translating the input into a higher dimensional space. Each filter (or feature map) has its
#     own ReLU.
# (3) The max-pooling layer translates the input into a lower dimensional space by collapsing each 2 * 2 matrix into its
#     max value.
# (4) The dropout layer matches the output of the max-pooling layer.
# (5) The flatten layer simple flattens the input of the dropout layer.
# (6) After this point, we have a normal neural network with a 128-node hidden layer, a dropout layer, and an output
#     layer.
model = Sequential([
    Convolution2D(32, 3, 3, border_mode='valid', input_shape=(1, 28, 28)),
    Activation('relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.5),
    Flatten(),
    Dense(128),
    Activation('relu'),
    Dropout(0.5),
    Dense(10),
    Activation('softmax')
])

print "Compiling model..."
sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

print "Loading training data..."
(training_examples, training_labels), (test_examples, test_labels) = mnist.load_data()

print "Preparing examples..."
training_examples = training_examples.reshape(training_examples.shape[0], 1, 28, 28)
test_examples = test_examples.reshape(test_examples.shape[0], 1, 28, 28)
training_examples = training_examples.astype('float32')
test_examples = test_examples.astype('float32')

print "Normalizing examples..."
training_examples /= 255
test_examples /= 255

print "Preparing labels..."
training_labels = np_utils.to_categorical(training_labels, 10)
test_labels = np_utils.to_categorical(test_labels, 10)

print "Training..."
model.fit(training_examples, training_labels, nb_epoch=15, batch_size=128)

print "Scoring..."
score = model.evaluate(test_examples, test_labels)

print "Results:", score