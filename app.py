from fastapi import FastAPI
from pydantic import BaseModel

import joblib

from preprocess import preprocess_text
app=FastAPI()

pipeline=joblib.load("model/disaster_pipeline.pkl")

class TweetRequest(BaseModel):
  text: str

@app.get("/")
def home():

  return{
    "message":"Disaster Tweet Classifier API"
  }

@app.post("/predict")
def predict(request: TweetRequest):

  processed_text = preprocess_text(
        request.text
    )
  
  prediction=pipeline.predict(
    [processed_text]
  )[0]

  label = (
    "Disaster"
    if prediction==1
    else
    "Not Disaster"
  )

  return{
    "tweet":request.text,
    "processed_text":processed_text,
    "prediction":int(prediction),
    "label":label
  }