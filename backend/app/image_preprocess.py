from tensorflow.keras.preprocessing import image
import numpy as np


def image_preprocessor(img_path: str):
    img = image.load_img(img_path, target_size=(192, 192))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0

    #print(img_array.shape)
    img_array = np.expand_dims(img_array, axis=0)
    #print(img_array.shape)

    return img_array


#path = input()
#image_preprocessor(path)
