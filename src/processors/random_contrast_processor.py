from PIL import ImageEnhance

from src.processors.image_processor import ImageProcessor


class RandomBrightnessProcessor(ImageProcessor):

    def __init__(self, lr_img, gt_img, brightness_range):
        super().__init__(lr_img, gt_img)

    def process(self):
        enhancer = ImageEnhance.Brightness(self.lr_img)
        self.lr_img = enhancer.enhance(0.9)
        enhancer = ImageEnhance.Contrast(self.lr_img)
        self.lr_img = enhancer.enhance(1.1)

        enhancer = ImageEnhance.Brightness(self.gt_img)
        self.gt_img = enhancer.enhance(0.9)
        enhancer = ImageEnhance.Contrast(self.gt_img)
        self.gt_img = enhancer.enhance(1.1)

        return self.lr_img, self.gt_img