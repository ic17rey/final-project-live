from flask import Flask, render_template, request

import os
import urllib.request
import cloudpickle as cp

# Downloading the ml model
#url = 'https://butlerunit22.s3.us-east-2.amazonaws.com/pckl_model.sav'
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'pckl_model.sav')
#urllib.request.urlretrieve(url, filename)

with open(filename, mode='rb') as file:
    model = cp.load(file)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/send', methods=["GET", "POST"])
def submit():
    
    # print(type(loaded_model))
    if request.method == "POST":
        
        user_input = []
        text_input = request.form["variable"]
        user_input.append(text_input)
        print(user_input)
        coded_result = model.predict(user_input)
        if (coded_result == [0]):
            result = "FAKE"
        else:
            result = "TRUE"
        print(result)

    return render_template("index.html", results=result)
        

if __name__ == "__main__":
    app.run(debug=True)