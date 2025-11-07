import pandas as pd 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
import joblib

from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv(r"C:\Users\deidr\OneDrive\Desktop\Data Science Training\Streamlit\Diabetes App\Diabetes 14.csv")

# Define features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

model = LogisticRegression()
model.fit(X, y)

#Load the dataset 
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv" 
df = pd.read_csv(url) 

#Split the dataset into input(X) and output(y) 
X = df.drop('Outcome', axis=1); y = df['Outcome']

#Train the model model = RandomForestClassifier() 
model.fit(X,y) 

#Save the model 
joblib.dump(model,'diabetes_app.pkl') 
print("The model has been saved successfully")