#Importing the Library

import joblib
from flask import Flask, jsonify
from pandas import DataFrame
from flask import request

app = Flask(__name__)

@app.route('/diabetesPrediction', methods=['POST'])        
def diabetesPrediction():
    
            data = request.json    
            df = DataFrame(data["data"]) #converting to data frame
          
           #Drop if any features not required
           #df = df.drop(['Age','TemplateID'],axis=1)
           
            # Dataframe Creation
            df = df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
             
            df.Pregnancies 				= df.Pregnancies.astype('int64')               
            df.Glucose 					= df.Glucose.astype('int64')
            df.BloodPressure     		= df.BloodPressure.astype('int64')
            df.SkinThickness    		= df.SkinThickness.astype('int64')
            df.Insulin    				= df.Insulin.astype('int64')
            df.BMI  					= df.BMI.astype('float64')
            df.DiabetesPedigreeFunction = df.DiabetesPedigreeFunction.astype('float64')
            df.Age   					= df.Age.astype('int64')
     
            test = df.iloc[:,:] #all rows and columns as input

            model = joblib.load('log_model_diabetes_prediction') # This can be your Model Registry/or any cloud location

            output = model.predict(test)
            final_predictions = DataFrame(list(output), columns = ["Your Diabetese Test Is"]).to_dict(orient="records")
 
            return jsonify(final_predictions) 

app.run(debug=False,host = "0.0.0.0", port = 5000)   
