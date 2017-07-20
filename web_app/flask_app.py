
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from sklearn.externals import joblib

app = Flask(__name__)
app.debug = True

clf = joblib.load('mysite/titanic_predictor.pkl')

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/meetup')
def meetup_form():
    return app.send_static_file('meetup.html')


@app.route('/meetup_predictor', methods=['POST'])
def meetup_predictor():
    age = int(request.form['age'])
    fare = int(request.form['fare'])
    passenger_class = int(request.form['class'])
    is_female = int(request.form['is_female'])

    # run model with user data and predict class (1 for survive or 0 for die)
    prediction = clf.predict([[age, fare, passenger_class, is_female]])
    # run model and get probabilities for each class
    probabilities = clf.predict_proba([[age, fare, passenger_class, is_female]])

    # create the probabiliy message
    probability_message = '({0} chance of survival)'.format(probabilities[0][1])

    # Return message based on the prediction
    if prediction[0] == 1:
        return 'You might survive! ' + probability_message
    else:
        return 'You\'ll probebly die! ' + probability_message
    
    
 
