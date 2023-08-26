from abc import abstractmethod
from typing import Tuple

from PIL.Image import Image


class ImageProcessor:

    def __init__(self, lr_img, gt_img):
        self.lr_img = lr_img
        self.gt_img = gt_img

    @abstractmethod
    def process(self) -> Tuple[Image, Image]:
        pass
