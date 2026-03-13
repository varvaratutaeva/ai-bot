#from bot_logic import gen_pass
import random
import tf_keras as keras
from PIL import Image, ImageOps  # Installing pillow instead of PIL
import numpy as np
from keras.models import load_model  # TensorFlow is required for Keras to work


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5",)

# Load the labels
class_names = open("labels.txt", "r").readlines()

def flag_set(model,class_names):

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("Chinatest.png").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)
    return flag_set(model,class_names)

if class_names==0:
    print('Это флаг США, там проживает 345 427 000 человек')
if class_names==1:
    print('Это флаг России, там проживает 144 820 000 человек')
if class_names==2:
    print('Это флаг Индии, там проживает 1 450 936 000 человек')
if class_names==3:
    print('Это флаг Индонезии, там проживает 283 488 000 человек')
if class_names==4:
    print('Это флаг Бразилии, там проживает 211 999 000 человек')
if class_names==5:
    print('Это флаг Бангладеш, там проживает 173 562 000 человек')

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
