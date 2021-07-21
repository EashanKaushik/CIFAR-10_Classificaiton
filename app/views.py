from flask import url_for, render_template, Flask, request
from app.utils import make_prediction
from keras.preprocessing import image
import numpy as np

# def home():
#     return render_template('home.html', pagename='Home')

def predict():
    file_upload = False

    if request.method == 'POST':
        file_upload = True

        imgfile = request.files['imgfile']

        imgfile.save('static/images/upload.JPG')

        img = image.load_img('static/images/upload.JPG', target_size=(32, 32))
        img = image.img_to_array(img)
        img = img/255
        img = np.expand_dims(img, axis=0)

        class_label = make_prediction(img)
        
        data = {
            'class_label': class_label
        }

        return render_template('predict.html', pagename='Predict', file_upload=file_upload, data=data)
    
    return render_template('predict.html', pagename='Predict', file_upload=file_upload)
