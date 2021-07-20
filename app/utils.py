from keras.models import load_model
from pickle import load
import numpy as np

MODEL_PATH = 'model/20210720-184145.h5'
CLASS_LABEL_PATH = 'model/cifar_label_name.pkl'

model = load_model(MODEL_PATH)
class_label = load(open(CLASS_LABEL_PATH, 'rb'))

def make_prediction(image):

    class_prob = list()
    y_pred = model.predict(image)

    for single_prob in y_pred:
        class_prob.append(single_prob * 100)

    class_index = np.argmax(y_pred, axis=1)
    class_label = class_label[class_index]
    class_label = class_label[0].decode('utf-8')

    return class_prob, single_probs
