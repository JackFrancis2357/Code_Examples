import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint, CSVLogger, TensorBoard
from time import time
import h5py

start = time()
x = np.load('x_100.npy')
y = np.load('y_100.npy')

# x = (x - 970) / 1319
# y = (y - 970) / 1319

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
y_train = np.reshape(y_train, (y_train.shape[0], y_train.shape[2]))
y_test = np.reshape(y_test, (y_test.shape[0], y_test.shape[2]))

regressor = Sequential()
regressor.add(LSTM(units=500, return_sequences=True, input_shape=(x_train.shape[1], 7921)))
# regressor.add(Dropout(0.1))
regressor.add(LSTM(units=500))
# regressor.add(Dropout(0.1))
regressor.add(Dense(units=7921))
regressor.compile(optimizer='adam', loss='mean_squared_error')
regressor.load_weights('best_weights.hdf5')


# Checkpoint
checkpoint = ModelCheckpoint('best_weights.hdf5', monitor='loss', verbose=1, save_best_only=True, mode='min')
csv_logger = CSVLogger('log.csv', append=True, separator=';')
tensorboard = TensorBoard(log_dir='./logs/{}'.format(time()),
                          write_graph=True, write_images=False)
callbacks_list = [checkpoint, csv_logger, tensorboard]

regressor.fit(x_train, y_train,
              epochs=10,
              batch_size=10,
              callbacks=callbacks_list)

predicted_value = regressor.predict(x_test, batch_size=1)
for i in range(predicted_value.shape[0]):
    new_image = predicted_value[i, :]
    # new_image = new_image * 1319
    # new_image = new_image + 917
    new_image = np.reshape(new_image, newshape=(89, 89))
    jack = plt.imshow(new_image, cmap='jet')
    plt.colorbar(jack)
    plt.show()

score = regressor.evaluate(x_test, y_test, batch_size=1)
print(score)
print(time() - start)
