from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model_loader import load_my_model
from image_preprocess import image_preprocessor
import numpy as np
from data_model import User_data
from fastapi.middleware.cors import CORSMiddleware
import base64
from io import BytesIO
from PIL import Image


app = FastAPI()

model =  load_my_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/predict')
def predict_img(data: User_data):
    img_bytes = base64.b64decode(data.image)
    pil_img = Image.open(BytesIO(img_bytes)).convert("RGB")


    img = image_preprocessor(pil_img=pil_img)

    #print(type(img))
    
    #pil_img.show()
    #print(pil_img)
    #print(pil_img.format)
    #print(pil_img.size)
    #print(pil_img.mode)
    #print(np.array(pil_img).min(), np.array(pil_img).max())
    
    pred = model.predict(img)
    ans = np.argmax(pred)
    print(pred)
    print(ans)

        
    return JSONResponse(status_code=200, content={'message': 'the class name is: ' + str(ans+1) })

@app.post('/sound')
def voice(class_pointer: int):
    pass
