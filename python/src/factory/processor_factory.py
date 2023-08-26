from typing import Any

from PIL import Image

from src.processors.image_processor import ImageProcessor
from src.processors.random_brightness_processor import RandomBrightnessProcessor
from src.processors.random_contrast_processor import RandomContrastProcessor
from src.processors.random_noise_blender_processor import RandomNoiseBlenderProcessor
from src.processors.random_orientation_processor import RandomOrientationProcessor


class ProcessorFactory:

    @staticmethod
    def create_processor(name: str, lr_img: Image, gt_img: Image, config: Any) -> ImageProcessor:
        if name == "random_orientation":
            return RandomOrientationProcessor(lr_img, gt_img)
        elif name == "random_brightness":
            return RandomBrightnessProcessor(lr_img, gt_img, config.get("brightness_range", [0.9, 1.1]))
        elif name == "random_contrast":
            return RandomContrastProcessor(lr_img, gt_img, config.get("contrast_range", [0.9, 1.1]))
        elif name == "random_noise":
            return RandomNoiseBlenderProcessor(lr_img, gt_img, config.get("max_noise_intensity", 0.3))
        else:
            raise NotImplemented
