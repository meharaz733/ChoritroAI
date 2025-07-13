from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model_loader import load_my_model
from image_preprocess import image_preprocessor
import numpy as np


app = FastAPI()

model =  load_my_model()


@app.post('/predict')
def predict_img(img_path: str):
    img = image_preprocessor(img_path=img_path)
    pred = model.predict(img)
    ans = np.argmax(pred)

    return JSONResponse(status_code=200, content={'message': 'the class name is: ' + str(ans+1) })

@app.post('/sound')
def voice(class_pointer: int):
    pass

