import torchvision.models as models

model_keys = []
for model in [models.resnet18, models.alexnet,
              models.vgg16, models.inception_v3]:
    m = model(pretrained=True)  # downloads model
    model_keys.append(model.__name__)  # creates list of keys
    del m  # free up memory
