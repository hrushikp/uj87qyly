import numpy as np
from ipywidgets import interact,fixed
from PIL import Image
def imshow (X,resize=None):
  image=Image.fromarray(X)
  if resize!=None:
    image=image.resize(resize)
  return image.show()
