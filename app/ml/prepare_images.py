from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import os
from config import Configuration

img_folder = Configuration().image_folder_path
if not os.path.exists(img_folder):
    zip_url = 'https://github.com/EliSchwartz/imagenet-sample-images/archive/master.zip'
    with urlopen(zip_url) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(img_folder)
