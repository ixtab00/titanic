from typing import List
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

def make_model(num_neurons: List,
               input_width: int,
               dropout_rate: float):
    '''Makes linear model for binar cls. with spefic parameters'''
    model = Sequential()
    model.add(Dense(num_neurons[0], activation='relu', input_shape = (input_width, )))
    for i in range(1,len(num_neurons)):
        model.add(Dense(num_neurons[i], activation='relu'))
        model.add(Dropout(dropout_rate))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',metrics=['accuracy'])
    return model

