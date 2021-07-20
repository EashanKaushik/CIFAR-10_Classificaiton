from flask import url_for, render_template, Flask, request
from app.utils import make_prediction
from keras.preprocessing import image

def home():
    return render_template('home.html', pagname='Home')

def predict():
    file_upload = False

    if request.method == 'POST':
        file_upload = True

        imgfile = request.files['imgfile']

        data = {
            'class_label': class_label,
            'class_prob': class_prob
        }

        return render_template('predict.html', pagename='Predict', file_upload=file_upload, data=data)
    
    return render_template('predict.html', pagename='Predict', file_upload=file_upload)
