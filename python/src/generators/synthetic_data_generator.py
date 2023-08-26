import os
from abc import abstractmethod


class SyntheticDataGenerator:
    def __init__(self, config):
        self.width = config.get("image").get("width", 400)
        self.height = config.get("image").get("height", 400)
        self.lr_output_dir = config.get("lr_output_dir", "result")
        self.gt_output_dir = config.get("gt_output_dir", "result")
        self.num_images = config.get("num_images", 100)
        self.extension = config.get("extension", "png")

        if not os.path.exists(self.lr_output_dir):
            os.mkdir(self.lr_output_dir)
        if not os.path.exists(self.gt_output_dir):
            os.mkdir(self.gt_output_dir)

    @abstractmethod
    def generate_data(self):
        pass
