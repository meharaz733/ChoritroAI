from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model_loader import load_my_model
from image_preprocess import image_preprocessor
import numpy as np
from data_model import User_data, Response_data  #Pydantic Model for data validation
from fastapi.middleware.cors import CORSMiddleware
import base64
from io import BytesIO
from PIL import Image
from utils.class_list import class_name_


app = FastAPI()

model =  load_my_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/predict', response_model=Response_data)
def predict_img(data: User_data):
    img_bytes = base64.b64decode(data.image)
    pil_img = Image.open(BytesIO(img_bytes)).convert("RGB")
    img = image_preprocessor(pil_img=pil_img)

    #prediction
    pred = model.predict(img)
    ans = np.argmax(pred)
    
    print("Folder name:", class_name_(ans))
        
    return Response_data(class_folder=class_name_(ans))
