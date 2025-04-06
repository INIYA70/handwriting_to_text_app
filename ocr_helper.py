import easyocr
from PIL import Image
import numpy as np

def extract_text(image_file):
    reader = easyocr.Reader(['en'])
    image = Image.open(image_file)
    image_np = np.array(image)
    results = reader.readtext(image_np, detail=0)
    return "\n".join(results)
