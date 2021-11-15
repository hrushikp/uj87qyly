import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
def imshow(X, resize=None):
    Img_1 = Image.fromarray(X)
    Img_1 = Img_1.resize(resize)
    Img_1.show()
    return Img_1