from keras.models import load_model


def get_decoder_model():
    return load_model(r'D:\GitHub\img_captioning\saved_objects\model_decoder.h5')