import unittest

import PIL
import torch

from ml.classification_utils import classify_image, \
    get_model, get_labels, fetch_image

class TestMLUtils(unittest.TestCase):
    def setUp(self):
        self.model_id = 'resnet18'
        self.image_id = 'n01443537_goldfish.JPEG'

    def test_model(self):
        model = get_model(self.model_id)
        self.assertTrue(model)
        self.assertIsInstance(model, torch.nn.Module)

    def test_model_not_found(self):
        nn_model_id = 'not a model'
        with self.assertRaises(ImportError):
            get_model(model_id=nn_model_id)

    def test_get_image(self):
        image = fetch_image(image_id=self.image_id)
        self.assertIsInstance(image, PIL.Image.Image)
        image.close()

    def test_image_not_found(self):
        nn_image_id = 'not an image'
        with self.assertRaises(FileNotFoundError):
            fetch_image(nn_image_id)

    def test_labels(self):
        l = get_labels()
        assert isinstance(l, list)

    def test_classification(self):
        out = classify_image(self.model_id, self.image_id)
        self.assertTrue(out)

