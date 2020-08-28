import numpy as np
from keras.models import model_from_json
import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import  to_categorical
'''
keras can take care of all these that I wrote out
watch sentdex deep learning ep1 to remember

Include a way on web and offline to write
 in real time and have it classfied

 
train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()

#Normalization from [0,255] to [-0.5,0.5] to make
#neural net easier to train
train_images = (train_images/255) - 0.5
test_images = (test_images/255) - 0.5

#flatten the images from 28x28 to 784(28x28)
train_images = train_images.reshape((-1,784))
test_images = test_images.reshape((-1,784))

#Building a model with 2 layers of 64 neurons each
#and one last one with 10 neurons from 0-9
model = Sequential()
model.add(Dense(64,activation='relu',input_dim=784))
model.add(Dense(64,activation='relu'))
model.add(Dense(10,activation='softmax'))

#compiling the model to allow for optimization
model.compile(
	optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy']
	)

#training the model
#epochs=> number of iterations,
#batch_size=> number of samples per gradient update

model.fit(
	train_images,
	to_categorical(train_labels),batch_size=32,epochs=5
	)

#evaluate the model

model.evaluate(
	test_images,
	to_categorical(test_labels)
	)

#saving the model to disk

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")'''

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")

#test with your own images
predictions = loaded_model.predict(test_images[-10:-5])
print(np.argmax(predictions,axis=1))
print(test_labels[-10:-5])

#show a plot of the images
'''for i in range(-10,-5):
	image = np.array(test_images[i],dtype='float')
	pixels = image.reshape((28,28))
	plt.imshow(pixels,cmap='gray')
	plt.show()'''