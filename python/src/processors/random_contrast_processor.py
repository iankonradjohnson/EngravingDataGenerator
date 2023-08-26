import random
from typing import Tuple

from PIL import ImageEnhance
from PIL.Image import Image

from src.processors.image_processor import ImageProcessor


class RandomContrastProcessor(ImageProcessor):

    def __init__(self, lr_img, gt_img, contrast_range):
        super().__init__(lr_img, gt_img)
        self.contrast_range = contrast_range

    def process(self) -> Tuple[Image, Image]:
        contrast = random.uniform(*self.contrast_range)

        enhancer = ImageEnhance.Contrast(self.lr_img)
        self.lr_img = enhancer.enhance(contrast)
        enhancer = ImageEnhance.Contrast(self.gt_img)
        self.gt_img = enhancer.enhance(contrast)

        return self.lr_img, self.gt_img

