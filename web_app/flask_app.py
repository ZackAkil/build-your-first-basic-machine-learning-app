
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)
app.debug = True

clf = joblib.load('titanic_predictor.pkl')

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/meetup', methods=['GET','POST'])
def meetup_predictor():

    # if the user is accessing this function normally return the form
    if request.method == 'GET':
        return app.send_static_file('meetup.html')
    
    # if its comming from a form submition, collect data and return the prediction
    elif request.method == 'POST':

      age = int(request.form['age'])
      fare = int(request.form['fare'])
      passenger_class = int(request.form['class'])
      is_female = int(request.form['is_female'])

      # run model with user data
      prediction = clf.predict([[age, fare, passenger_class, is_female]])
      
      # Return message based on the prediction
      if prediction[0] == 1:
        return 'You might survive!'
      else:
        'You\'ll probebly die!'
