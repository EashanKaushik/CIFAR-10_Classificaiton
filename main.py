from flask import Flask
from utils import views

app = Flask(__name__)

app.add_url_rule('/home', 'home', views.home)
app.add_url_rule('/predict', 'predict', views.predict, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)