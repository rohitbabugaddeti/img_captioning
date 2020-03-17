import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input

def get_encoder_model():
    return load_model(r'D:\GitHub\img_captioning\saved_objects\model_encoder.h5')

def preprocess(image_path):
    # Convert all the images to size 299x299 as expected by the inception v3 model
    # print(type(image_path))
    img = image.load_img(image_path, target_size=(299, 299))
    # Convert PIL image to numpy array of 3-dimensions
    x = image.img_to_array(img)
    # Add one more dimension
    x = np.expand_dims(x, axis=0)
    # preprocess the images using preprocess_input() from inception module
    x = preprocess_input(x)
    return x

def encode(image):
    image = preprocess(image) # preprocess the image
    model_new = get_encoder_model()
    fea_vec = model_new.predict(image) # Get the encoding vector for the image
    fea_vec = np.reshape(fea_vec, fea_vec.shape[1]) # reshape from (1, 2048) to (2048, )
    return fea_vec