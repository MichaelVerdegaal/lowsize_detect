import os
from PIL import Image

movelist = []
ext = ['jpg', 'jpeg', 'png']
for file in os.listdir(os.getcwd()):
    if file.endswith(tuple(ext)):
        width, height = Image.open(file).size
        if width <= 900 or height <= 900:
            movelist.append(file)

newpath = f'{os.getcwd()}\\low_size_images'
if movelist:
    if not os.path.exists(newpath):
        os.makedirs(newpath)
for file in movelist:
    os.rename(f'{os.getcwd()}\\{file}', f'{newpath}\\{file}')
input(f'{len(movelist)} images moved.\nProcess finished, press enter to exit.')
