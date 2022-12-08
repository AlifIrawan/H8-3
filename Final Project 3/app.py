import flask
import numpy as np
import pickle


app = flask.Flask(__name__, template_folder='templates')

model = pickle.load(open(
    'D:/Github - Job/Praktek Koding/Final Project 3/model/model_FP3.pkl', 'rb'))


@app.route('/')
def index():
    return(flask.render_template('main.html'))


# Route Final Project 1


# Route Final Project 2


# Route Final Project 3
@app.route('/final_project-3')
def final_project3():
    return(flask.render_template('FP3-003.html'))


@app.route('/predict_fp3', methods=['POST'])
def predict_fp3():
    int_features = [int(x) for x in flask.request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = {0: 'Selamat', 1: 'Tidak Selamat'}

    return flask.render_template('FP3-003.html', prediction_text=output[prediction[0]])


if __name__ == '__main__':
    app.run(debug=True)
