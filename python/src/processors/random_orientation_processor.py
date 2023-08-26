import random
from typing import Tuple

from PIL import Image

from src.processors.image_processor import ImageProcessor


class RandomOrientationProcessor(ImageProcessor):
    def __init__(self, lr_img, gt_img):
        super().__init__(lr_img, gt_img)

    def process(self) -> Tuple[Image.Image, Image.Image]:
        if random.choice([True, False]):
            mode = random.choice([Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM])
            self.lr_img = self.lr_img.transpose(mode)
            self.gt_img = self.gt_img.transpose(mode)

        if random.choice([True, False]):
            self.lr_img = self.lr_img.rotate(90)
            self.gt_img = self.gt_img.rotate(90)

        return self.lr_img, self.gt_img
