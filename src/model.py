from PIL import Image
from io import BytesIO

import numpy as np
import tensorflow as tf

from tensorflow.keras.applications.mobilenet import preprocess_input


input_shape = (224, 224)
digits= ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9"]


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image


def preprocess(image: Image.Image) -> np.ndarray:
    image = image.resize(input_shape)
    image_np = np.asarray(image)

    img_array_scaled = preprocess_input(image_np)
    img_array_expanded_dims = np.expand_dims(img_array_scaled, axis=0)

    return img_array_expanded_dims


def predict_imagefile(img_array: np.ndarray):
    _model = tf.keras.models.load_model('mobilenet')

    proba = _model.predict(img_array)

    idx = np.argmax(proba)
    
    return digits[idx]