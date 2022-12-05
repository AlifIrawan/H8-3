import flask
import numpy as np
import pickle


app = flask.Flask(__name__, template_folder='templates')

model = pickle.load(open(
    'D:/Hacktiv8 - Data Science/Test coding/Final Project 3/model/trained_code_model.pkl', 'rb'))


@app.route('/')
def index():
    return(flask.render_template('FP3-003.html'))


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in flask.request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = {0: 'Tidak Terselematkan', 1: 'Terselamat'}

    return flask.render_template('FP3-003.html', prediction_text='Pasien {} dari penyakit jantung'.format(output[prediction[0]]))


if __name__ == '__main__':
    app.run(debug=True)
