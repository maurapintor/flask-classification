"""
This is a simple classification service. It accepts an url of an
image and returns the top-5 classification labels and scores.
"""
import io
import json

import importlib
import requests
import torch
from PIL import Image
from torchvision import transforms

def fetch_image(url):
    r = requests.get(url)
    img = Image.open(io.BytesIO(r.content))
    return img


def get_labels():
    imagenet_labels_path = "https://raw.githubusercontent.com/" \
                           "anishathalye/imagenet-simple-labels/" \
                           "master/imagenet-simple-labels.json"
    r = requests.get(imagenet_labels_path)
    labels = json.load(io.StringIO(r.text))
    return labels

def get_model(model_id):
    try:
        module = importlib.import_module('torchvision.models')
        return module.__getattribute__(model_id)(pretrained=True)
    except ImportError as e:
        # TODO add something that makes sense
        print("error", str(e))


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
    img_path = 'https://en.upali.ch/wp-content/uploads/2016/11/arikanischer-ruessel.jpg'
    out = classify_image(img_path)
    for row in out:
        print(row)

    get_model('resnet18')