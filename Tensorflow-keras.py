import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test)= mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis= 1)
x_test = tf.keras.utils.normalize(x_test, axis= 1)



model = tf.keras.models.Sequential()
#important ** add input shape
model.add(tf.keras.layers.Flatten(input_shape = x_train.shape[1:])) #the shape of x_train and creates an array
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation= tf.nn.softmax))

model.compile(optimizer= 'adam' , loss= 'sparse_categorical_crossentropy',
metrics=['accuracy'])

model.fit(x_train,y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test,y_test)
print(val_loss, val_acc)

#can only display one at a time
plt.imshow(x_train[0], cmap = plt.cm.binary)
plt.imshow(x_train[1], cmap = plt.cm.binary)
plt.show()

model.save('num_reader.model')
new_model = tf.keras.models.load_model('num_reader.model')

predictions = new_model.predict([x_test]) #always takes in a list
print(predictions)

print(x_train)
print(x_test)
print(np.argmax(predictions[0]))
print(np.argmax(predictions[1]))

#can only display one at a time
plt.imshow(x_test[0])
plt.imshow(x_test[1])
plt.show()