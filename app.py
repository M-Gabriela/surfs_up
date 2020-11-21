#mport the Flask dependency
from flask import Flask

#new Flask instance 

app = Flask(__name__)

#Create Flask Routes 

#defining starting point 

@app.route('/')

#create a function called hello_world()

@app.route('/')
def hello_world():
    return 'Hello world'

#Run a Flask App

