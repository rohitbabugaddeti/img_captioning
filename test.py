# from keras.models import load_model
# import os
# f = r'D:\GitHub\img_captioning\saved_objects\model_encoder.h5'
# model = load_model(f)
# print(model.summary())

from predict import get_caption

print(get_caption(r"D:\GitHub\img_captioning\uploaded image\test.jpg"))