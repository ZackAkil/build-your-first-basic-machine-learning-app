# Build your first basic machine learning app
Code resources and instructiions for Central London Data Science Project Nights 22nd meetup.

## First off!
Make sure you've got [Annaconda Navigator](https://www.continuum.io/downloads) installed, this will allow you to use Jupyter Notebooks and easily managed you installed libraries.

Then you need to creaet an account with the internet server hosting service we will be using [PythonAnywhere](https://www.pythonanywhere.com/) to host our app, it's free and by far the easiest web server hosting service for this sort of thing!

## The Task
We have provided a starter notebook `starter titanic model.ipynb` that will guide you in making a simple machine learning model for predicting Titanic survivors. Along side that is a finnished solution `complete titanic model.ipynb` notebook incase you get stuck on any part.

After you have built a simple model, you then need to save it (i.e. pickel it!). You can then copy that trained model file onto our server and use it in a simple web app (using the Flask library).

The web app will return to the user a web form, and when the user has entered all the data and submited the form, the user will then be told whether they are or are not likly to survive on the Titanic.

## Starting your Flask web app on PythonAnywhere

[This video](https://www.youtube.com/watch?v=v5ES-RcOJng) will show you how to get your flask app up and running.

### Serving the user a form to input data

In the source directory of the app (the folder with `flask_app.py`) create a folder called `static`. This is where we can put files that we want to send to people from our flask app.
Inside that folder create a file called `meetup.html`.

The file structure so far should look like this:

```
mysite
+-- flask_app.py
+-- static
|   +-- meetup.html
```

Inside the `meetup.html` file copy in the following html code:
```html
<html>
  <head></head>
  <body>

    <h1>Will you survive the Titanic?</h1>

    <form  method="post" action="/meetup_predictor">
      Age:<input type="input" name="age"><br>
      Fare:<input type="input" name="fare"><br>
      Class:<input type="input" name="class"><br>
      Female:<input type="input" name="is_female"><br>

      <input type="submit" name="submit">
    </form> 
  </body>
</html>
```
This consist of a page title and a form that takes in input from the user and sends it to the web app's `/meetup_predictor` endpoint. We will create this endpoint later.

To allow the user to access this we need to serve it from an endpoint.

In our `flask_app.py` we add the endpoint that will serve this html file:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/meetup')
def meetup_form():
    return app.send_static_file('meetup.html')
```

Now if we go to `http://[your user name].pythonanywhere.com/meetup` we should see our form.

### Adding our model
In the source folder of our web app (the folder with flask_app.py), upload the pickle file of our model. 

The file structure so far should look like this:

```
mysite
+-- flask_app.py
+-- titanic_predictor.pkl
+-- static
|   +-- meetup.html
```

Now in our `flask_app.py` we can add the endpoint that will take in data and feed them into the model and then return the prediction. 

```python
from flask import Flask
from sklearn.externals import joblib # <---- import pickle library

app = Flask(__name__)

clf = joblib.load('mysite/titanic_predictor.pkl') # <---- load in our model

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

    # Return message based on the prediction
    if prediction[0] == 1:
    return 'You might survive!'
    else:
    return 'You\'ll probebly die!'
```

Now you should be able to submit the form and get back an answer as to whether or not you will survive, 
#### and its all on the internet for everyone to use!!! :rocket:

### If you get problems with loading the model into the app
Make sure the versions of scikit-learn are the same between the Jupyter notebook and the web app.

You can check the module version by running this code
```python
import sklearn
print(sklearn.__version__)
```

If they are not the same then you can update the web apps version by following [this video](https://www.youtube.com/watch?v=eRwMsMen4hU).

