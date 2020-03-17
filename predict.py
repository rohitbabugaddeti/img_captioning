import numpy as np
from keras.preprocessing.sequence import pad_sequences
from decoder import get_decoder_model
from encoder import encode
from pickle import load
from time import time


def get_caption(photo):
    ts = time()
    max_length = 34
    print("loading decoder model..")
    model = get_decoder_model()
    print("done")
    tde = time()
    print("time took: ",tde - ts,"secs")
    print("encoding image..")
    photo = encode(photo)
    print("done")
    tee = time()
    print("time took: ",tee  - tde, "secs")
    # print(photo)
    photo = photo.reshape((1,2048))
    print("opening word to index dict..")
    with open(r"D:\GitHub\img_captioning\saved_objects\wtoix.pkl", "rb") as f:
        wordtoix = load(f)

    with open(r"D:\GitHub\img_captioning\saved_objects\ixtow.pkl", "rb") as f:
        ixtoword = load(f)
    toe = time()
    print("time took: ", toe - tee, "secs")
    print("generating caption")
    in_text = 'startseq'
    for i in range(max_length):
        sequence = [wordtoix[w] for w in in_text.split() if w in wordtoix]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = ixtoword.get(yhat,"")
        in_text += ' ' + word
        if word == 'endseq':
            break
    final = in_text.split()
    final = final[1:-1]
    final = ' '.join(final)
    print("done")
    print("time took: ", time() - toe, "secs")
    return final
