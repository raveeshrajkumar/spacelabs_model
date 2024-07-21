##Importing Packages
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np


##Creating Application
app = FastAPI()

##Loading the XGBoost model
xgb_reg = pickle.load(open("C:/MultioutputRegression/Model/xgb_reg.pkl", "rb"))

##Creating a StandardScaler instance
scaler = StandardScaler()

##Pydantic model for input validation
class InputData(BaseModel):
    apogee: float
    perigee: float
    incl: float
    arg_perigee: float
    raan: float


##Define -> Test Route
@app.get("/test")
async def test():
    return {"message": "It Works!!!"}

##Define route -> handle predictions
@app.post("/predict")
async def predict(data: InputData):
    ##Convert input data to a 2D NumPy array
    input_features = np.array([[data.apogee, data.perigee, data.incl, data.arg_perigee, data.raan]])

    ##Scale the input features
    scaled_features = scaler.fit_transform(input_features)

    ##Make predictions using the XGBoost model
    prediction = xgb_reg.predict(scaled_features)

    ##Return the prediction as a JSON response
    return {"prediction": prediction.tolist()}
