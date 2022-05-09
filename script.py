from flask import Flask,render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('deploy.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    
    float_feature = [float(x) for x in request.form.values()]
    features = [np.array(float_feature)]

    prediction = model.predict(features)[0]
    

    if prediction ==0:
        result=" Great news you are not diabetic"
    elif prediction==1:
        result ="You are diabetic "

    print(result)
    return render_template("result.html",result=result)

if __name__ =="__main__":
    app.run(debug=True)
