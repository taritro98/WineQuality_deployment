
# Wine Quality Prediction (End-to-end ML)

An end-to-end machine learning multiclass classification project
to predict the quality of red wine using various parameters.
The aim of this project was to cover all stages of a machine learning
lifecycle starting with data collection and feature engineering
to model building and deployment. 

The final application can be accessed at - https://winequality-prediction-api.herokuapp.com/

Dataset : https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

Model : Random Forest Classifier

Preprocessing : Z-Score Normalization


## Installation

Install my-project with npm

```python
  pip install -r requirements.txt
  python app.py
```
    
## Heroku Deployment

- Create an app in Heroku
- Install Heroku CLI 
- Login to heroku using 
``` bash
heroku login
```
- Add Heroku app as remote in cli
``` bash
heroku git:remote -a {name_of_app}
```
- Push app to Heroku remote
``` bash
heroku push origin main
```