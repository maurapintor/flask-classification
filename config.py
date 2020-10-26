import os

home = os.path.expanduser("~")


class Configuration:
    """Contains the configuration information for the app."""
    image_folder_path = os.path.join(home, ".pytorch/imagenet_subset")
    models = ('resnet18', 'alexnet', 'vgg16', 'inception_v3',)
