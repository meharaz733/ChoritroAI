import numpy as np
from PIL import Image


def image_preprocessor(pil_img: Image.Image):

    """This function expect PIL.Image.Image object. Then it resize the image to 192x192, normalize the pixel value, expand the dimension to match shape and then return the image."""
    
    img = pil_img.resize(size=(192,192))    
    img = np.array(img)/ 255.0
    

    #print(img_array.shape)
    
    img = np.expand_dims(img, axis=0)
    
    #print(img_array.shape)

    return img


#path = input()
