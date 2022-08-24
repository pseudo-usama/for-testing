from cgi import test
import warnings
warnings.filterwarnings('ignore')

import os

from tensorflow import keras

from keras.layers import Input, Lambda, Dense, Flatten                  

from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import  preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt

IMAGE_SIZE = [224, 224]

train_path = 'Datasests/train'
valid_path = 'Datasets/test'

vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

for layer in vgg.layers:
    layer.trainable = False

    folders = glob('Datasest/train/*')
x = Flatten()(vgg.output)

prediction = Dense(len(folders), activation='softmax')(x)
# creat a model object
model = Model(input=vgg.input, output=prediction)
#view the structure of the model
model.summary()

model.comppile(
    loss='categorical_crossentropy',
    optimizer='adam',
    matrics=['accuracy']
)

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,      
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)




#make sure you provide the same target size as initialized for the image size
training_test = train_datagen.flow_from_directory('C:\\Users\\Shaniii\\Desktop\\New folder (2)\\Lungs X_ray',
                                                 target_size = (256, 256),
                                                 batch_size = 10,
                                                class_models = 'categorical')




test_set = test_datagen.flow_from_directory('C:\\Users\\Shaniii\\Desktop\\New folder (2)\\Lungs X_ray',
                                              target_size = (256, 256),
                                              batch_size = 10,
                                               class_mode = 'catagorical')

r = model.fit_generator(
    training_test,
    validation_data=test_set,
    epocha=1,
    steps_per_epoch=len(training_test),
    validation_steps=len(test_set)
)

import tensorflow as tf
from keras.models import load_model

model.save('chest_xray.hs')

from keras.models import load_model


# In[16]:


from keras.preprocessing import image


# In[17]:


from keras.applications.vgg16 import preprocess_input


# In[18]:


import numpy as np


# In[19]:


model=load_model('chest_xray.hs')


# In[47]:


img=image.load_img('C:\Users\Shaniii\Desktop\New folder')

# In[48]:


x=image.img_to_array(img)


# In[49]:


x=np.expand_dims(x, axis=0)


# In[50]:


img_date=preprocess_input(x)


# In[51]:


classes=model.predict(img_date)


#In[59]:


result=int(classes[0][0])


# In[60]:

if result==0:
    print("Preson is Affected By PNEUMONIA")
else:
    print("Result is Normal")