import math
import os
import random

from PIL import Image, ImageDraw

from draw.greyscale_draw import GreyscaleDraw
from generators.synthetic_data_generator import SyntheticDataGenerator


class LineBandingGenerator(SyntheticDataGenerator):

    def __init__(self, config):
        super().__init__(config)
        self.line_frequency_range = config.get("line_frequency_range", [10, 50])
        self.amplitude_range = config.get("amplitude_range", [1, 2])
        self.frequency_range = config.get("frequency_range", [0.1, 5])

    def generate_data(self):
        for i in range(self.num_images):
            image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))
            draw = GreyscaleDraw(image)

            line_frequency = random.uniform(*self.line_frequency_range)
            line_step = int(self.width // line_frequency)

            sine_frequency = random.uniform(*self.frequency_range)
            sine_amplitude = random.uniform(*self.amplitude_range)

            for x in range(0, self.width, line_step):
                sine_value = math.sin(x * sine_frequency) * sine_amplitude
                line_width = abs(sine_value)

                draw.line([(x, 0), (x, self.height)], fill=(0, 0, 0), width=line_width)

            save_path = os.path.join(self.output_dir, f"image_{i}.{self.extension}")
            image.convert("L").save(save_path)
