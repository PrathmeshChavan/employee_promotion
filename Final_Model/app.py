from flask import Flask , render_template , request
import pickle
import numpy as np
import requests

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/' , methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict' , methods = ['POST'])
def predict():
    
    avg_training_score = int(request.form['avg_training_score'])
        
    awards_won = int(request.form['awards_won'])
    if(awards_won == 'Yes'):
        awards_won = 1
    else:
        awards_won = 0
                
    KPIs_met = int(request.form['KPIs_met'])
    if(KPIs_met == 'Yes'):
        KPIs_met = 1
    else:
        KPIs_met = 0
            
    previous_year_rating = int(request.form['previous_year_rating'])
        
    department_Operations = int(request.form['department_Operations'])
    if(department_Operations == 'Operations'):
        department_Operations = 1
        department_Procurement = 0
        department_Sales & Marketing = 0
        department_Technology = 0
        department_other = 0
            
    elif(department_Procurement == 'Procurement'):
        department_Operations = 0
        department_Procurement = 1
        department_Sales & Marketing = 0
        department_Technology = 0
        department_other = 0
            
    elif(department_Sales & Marketing == 'Marketing'):
        department_Operations = 0
        department_Procurement = 0
        department_Sales & Marketing = 1
        department_Technology = 0
        department_other = 0
                
    elif(department_Technology == 'Technology'):
        department_Operations = 0
        department_Procurement = 0
        department_Sales & Marketing = 0
        department_Technology = 1
        department_other = 0
                
    else:
        department_Operations = 0
        department_Procurement = 0
        department_Sales & Marketing = 0
        department_Technology = 0
        department_other = 1
            
            
            
        pre_args = [avg_training_score , awards_won , KPIs_met , previous_year_rating , 
                department_Operations , department_Procurement , department_Sales & Marketing ,
                department_Technology , department_other]

        pred_agrs_arr = np.array(pred_agrs)
        pred_agrs_arr = pred_agrs_arr.reshape(1 , -1)

        model_pred = model.predict(pred_agrs_arr)
        model_pred = round(float(model_pred))
        return render_template('predict.html' , prediction = model_pred)

if __name__=="__main__":
    app.run(debug=True)
                
                
                


