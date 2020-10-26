from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import os
import shutil
from config import Configuration

img_folder = Configuration().image_folder_path
if not os.path.exists(img_folder):
    zip_url = 'https://github.com/EliSchwartz/imagenet-sample-images/archive/master.zip'
    with urlopen(zip_url) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(img_folder)
else:
    sub_dir = os.path.join(img_folder, 'imagenet-sample-images-master')
    if os.path.exists(sub_dir):
        files = os.listdir(sub_dir)
        for f in files:
            shutil.move(os.path.join(sub_dir, f), img_folder)
        shutil.rmtree(sub_dir)

