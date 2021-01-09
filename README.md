# Employee Promotion Prediction

This is a classification use case which will classify whether an employee will get promotion or not based on various features.

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure :

#### Final_Model

1.templates

i) indext.html -- HTML for taking input from user

ii) predict.html -- HTML form for showing predictions

2. app.py - This contains Flask APIs that receives Employee details through GUI or API calls, computes the precited value based on our model and returns it.

3. final_model.ipynb - This contains code of model training and model testing.

4. model.pkl - contains our serialized trained model which will be used for making predictions.

#### Data_Preprocessing.ipynb

Data_Preprocessing.ipynb - Contains jupyter notebooks of EDA and all dataset Preprocessing and also scaled data.

#### Model_Building

Model_Building.ipynb - A jupyter notebook Where i have applied many Classification algorithms to find out which algorithm gives best accuracy.


#### train.csv

Contains training Dataset.

