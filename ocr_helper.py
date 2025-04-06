import easyocr
import numpy as np

def extract_text_from_image(image):
    reader = easyocr.Reader(['en'])
    img_array = np.array(image)
    result = reader.readtext(img_array, detail=0)
    return " ".join(result)
