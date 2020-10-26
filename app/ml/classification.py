"""
This is a simple classification service. It accepts an url of an
image and returns the top-5 classification labels and scores.
"""
import importlib
import io
import json
import logging
import os

import requests
import torch
from PIL import Image
from torchvision import transforms

from config import Configuration

conf = Configuration()


def fetch_image(image_id):
    image_path = os.path.join(conf.image_folder_path, image_id)
    img = Image.open(image_path)
    return img


def get_labels():
    imagenet_labels_path = "https://raw.githubusercontent.com/" \
                           "anishathalye/imagenet-simple-labels/" \
                           "master/imagenet-simple-labels.json"
    r = requests.get(imagenet_labels_path)
    labels = json.load(io.StringIO(r.text))
    return labels


def get_model(model_id):
    if model_id in conf.models:
        try:
            module = importlib.import_module('torchvision.models')
            return module.__getattribute__(model_id)(pretrained=True)
        except ImportError:
            logging.error("Model {} not found".format(model_id))
    else:
        return None


def classify_image(img_path):
    # fetch model+image and returns top 5 clf scores
    img = fetch_image(img_path)
    model = get_model("resnet18")
    model.eval()
    transform = transforms.Compose((
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )))

    # apply transform from torchvision
    preprocessed = transform(img).unsqueeze(0)

    out = model(preprocessed)
    _, indices = torch.sort(out, descending=True)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    labels = get_labels()
    output = [(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]
    return output


if __name__ == '__main__':
    img_path = 'n01534433_junco.JPEG'
    out = classify_image(img_path)
    for row in out:
        print(row)
