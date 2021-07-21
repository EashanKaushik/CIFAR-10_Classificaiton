from flask import Flask, url_for
from app import views
# from flask.ext.scss import Scss


app = Flask(__name__)
# Scss(app)

# app.add_url_rule('/home', 'home', views.home)
app.add_url_rule('/predict', 'predict', views.predict, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)