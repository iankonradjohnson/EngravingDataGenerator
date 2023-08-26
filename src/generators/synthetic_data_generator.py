from abc import abstractmethod


class SyntheticDataGenerator:
    def __init__(self, config):
        self.width = config.get("image").get("width", 400)
        self.height = config.get("image").get("height", 400)
        self.output_dir = config.get("output_dir", "")
        self.num_images = config.get("num_images", 100)
        self.extension = config.get("extension", "png")

    @abstractmethod
    def generate_data(self):
        pass
