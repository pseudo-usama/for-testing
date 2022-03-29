# %%
import numpy as np
import matplotlib as plt

from sklearn.model_selection import train_test_split

import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.callbacks import EarlyStopping

# %%
np.random.seed(0)
green_points = np.random.uniform(low=1, high=10, size=50)
red_points = np.random.uniform(low=-10, high=-1, size=50)

# %%
X = np.concatenate((green_points, red_points))
y = np.concatenate((
    np.ones(50),
    np.zeros(50)
))

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# %%
model = Sequential()

model.add(Dense(1, input_shape=(1,)))
model.add(Dense(1, activation='softmax'))

# %%
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_training = model.fit(X_train, y_train, validation_split=0.3, epochs=5, verbose=1)

# %%
model.evaluate(X_test, y_test)