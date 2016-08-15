import re
import numpy as np

from keras.models import Sequential
import numpy as np
from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation

def get_tokens(text):
    stripped_text = text.rstrip('\n')
    return re.findall(r"[\w']+|[.,!?;]", stripped_text)

def get_data(file):
    return [get_tokens(line) for line in open(file)]

def get_vocabulary_size(data):
    vocabulary = {}

    for line in data:
        for word in line:
            vocabulary[word] = 1

    return len(vocabulary)

def get_max_sentence_length(data):
    max_sentence_length = -1

    for line in data:
        sentence_length = len(line)
        if sentence_length > max_sentence_length:
            max_sentence_length = sentence_length

    return max_sentence_length

data = get_data("training_data.txt")
vocabulary_size = get_vocabulary_size(data)
max_sentence_length = get_max_sentence_length(data)

np.random.seed(1337)

model = Sequential([
    LSTM(128, input_dim=1, return_sequences=False),
    Dense(128, 1),
    Activation("linear")
])

model.compile(loss="mean_squared_error", optimizer="rmsprop")