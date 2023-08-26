import random
from typing import Tuple

from PIL import ImageEnhance
from PIL.Image import Image

from src.processors.image_processor import ImageProcessor


class RandomBrightnessProcessor(ImageProcessor):

    def __init__(self, lr_img, gt_img, brightness_range):
        super().__init__(lr_img, gt_img)
        self.brightness_range = brightness_range

    def process(self) -> Tuple[Image, Image]:
        brightness = random.uniform(*self.brightness_range)

        enhancer = ImageEnhance.Brightness(self.lr_img)
        self.lr_img = enhancer.enhance(brightness)
        enhancer = ImageEnhance.Brightness(self.gt_img)
        self.gt_img = enhancer.enhance(brightness)

        return self.lr_img, self.gt_img
