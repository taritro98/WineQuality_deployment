import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
s = np.load('std.npy')
m = np.load('mean.npy')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = (np.array([float_features] - m)) / s

    prediction = int(model.predict(final_features))

    return render_template('index.html', prediction_text='The quality of wine is {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)