import random
from typing import Tuple

import numpy as np
from PIL import ImageEnhance, Image

from src.processors.image_processor import ImageProcessor


class RandomNoiseBlenderProcessor(ImageProcessor):

    def __init__(self, lr_img, gt_img, max_blend_alpha):
        super().__init__(lr_img, gt_img)
        self.max_blend_alpha = max_blend_alpha

    def process(self):
        blend_alpha = random.uniform(0, self.max_blend_alpha)
        noise = np.random.normal(0, 25, (self.lr_img.height, self.lr_img.width)).astype(np.uint8)

        self.lr_img = self._blend_with_random_noise(self.lr_img, blend_alpha, noise)
        # self.gt_img = self._blend_with_random_noise(self.gt_img, blend_alpha, noise)

        return self.lr_img, self.gt_img

    def _blend_with_random_noise(self, img, blend_alpha, noise):
        # Convert image to grayscale
        img_gray = img.convert("L")

        # Generate random noise
        noise_image = Image.fromarray(noise)

        # Blend the noise with the image using the blend_alpha value
        blended_image = Image.blend(img_gray, noise_image, alpha=blend_alpha)
        return blended_image
