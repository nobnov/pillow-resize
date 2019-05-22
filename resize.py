from PIL import Image
from datetime import datetime
from time import sleep
import glob

files = glob.glob('./images/*')

for file_name in files:

    if file_name.endswith(('.png', '.jpeg', '.jpg')):
        img = Image.open(file_name)
        img.thumbnail((500, 500), Image.ANTIALIAS)
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        path = './resizeimages/' + time+'.jpg'
        img.save(path, 'JPEG', quality=100,  optimize=True)

        sleep(1)

    else:
        pass
