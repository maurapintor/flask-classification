import os

home = os.path.expanduser("~")
class Configuration:
    image_folder_path = os.path.join(home, ".pytorch/imagenet_subset")
