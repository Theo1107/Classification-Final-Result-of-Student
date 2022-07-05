from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# initiate model & columns
LABEL =['Pass','Fail']
datacol = ['code_module', 'code_presentation', 'gender', 'highest_education',
       'imd_band', 'age_band', 'num_of_prev_attempts', 'studied_credits',
       'disability']
with open('RF_hyper.pkl','rb') as f:
    model = pickle.load(f)

@app.route('/')
def welcome():
    return '<h3>Selamat Datang di Program Backend Model Saya</h3>'

@app.route("/predict", methods=["GET", "POST"])
def predict_result():
    if request.method == "POST":
        content = request.json
        try:
            new_data = {'code_module': content['codeModule'],
                        'code_presentation': content['codePresentation'],
                        'gender' : content['Gender'],
                        'highest_education' : content['highestEducation'],
                        'imd_band' : content['imdBand'],
                        'age_band' : content['ageBand'],
                        'num_of_prev_attempts' : content['numOfPrevAttempts'],
                        'studied_credits' : content['studiedCredits'],
                        'disability' : content['Disability']}
            new_data = pd.DataFrame([new_data])
            data = preprocesing.transform(new_data)
            res = model.predict(data)
            pred = []
            if res > 0.35:
                pred.append('Churn')
            else:
                pred.append('Not Churn')
            result = {'class':pred[0],
                      'class_name':pred[0]}
            response = jsonify(success=True,
                               result=result)
            return response, 200
        except Exception as e:
            response = jsonify(success=False,
                               message=str(e))
            return response, 400
    # return dari method get
    return "<p>Silahkan gunakan method POST untuk mode <em>inference model</em></p>"

app.run(debug=True)