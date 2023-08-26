import math
import os
import random
from PIL import Image

from draw.greyscale_draw import GreyscaleDraw
from generators.synthetic_data_generator import SyntheticDataGenerator


class LineBandingGenerator(SyntheticDataGenerator):

    def __init__(self, config):
        super().__init__(config)
        self.upscale = config.get("upscale", 4)
        self.line_frequency_range = config.get("line_frequency_range", [25, 40])
        self.amplitude_range = config.get("amplitude_range", [2, 3])
        self.frequency_range = config.get("frequency_range", [1, 1.1])
        self.angle_range = config.get("angle_range", [0, 1])
        self.line_width = 2

    def generate_data(self):

        diagonal_distance = int(math.sqrt(self.width ** 2 + self.height ** 2))
        max_offset = diagonal_distance

        for i in range(self.num_images):
            angle = random.uniform(*self.angle_range)
            radians = math.radians(angle)

            lr_image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))
            gt_image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))

            lr_draw = GreyscaleDraw(lr_image)
            gt_draw = GreyscaleDraw(gt_image)

            line_frequency = random.uniform(*self.line_frequency_range)
            line_step = int(diagonal_distance // line_frequency)

            sine_frequency = random.uniform(*self.frequency_range)
            sine_amplitude = random.uniform(*self.amplitude_range)

            scaled_line_width = self.width / line_frequency

            for offset in range(-max_offset, max_offset, line_step):
                sine_value = math.sin(offset * sine_frequency) * sine_amplitude + scaled_line_width
                line_width = abs(sine_value)

                start_x = offset * math.cos(radians + math.pi / 2)
                start_y = offset * math.sin(radians + math.pi / 2)
                end_x = start_x + diagonal_distance * math.cos(radians)
                end_y = start_y + diagonal_distance * math.sin(radians)

                lr_draw.line([(start_x, start_y), (end_x, end_y)], fill=(0, 0, 0), width=line_width)
                gt_draw.line([(start_x, start_y), (end_x, end_y)], fill=(0, 0, 0), width=scaled_line_width)

            if random.choice([True, False]):
                mode = random.choice([Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM])
                lr_image = lr_image.transpose(mode)
                gt_image = gt_image.transpose(mode)

            if random.choice([True, False]):
                lr_image = lr_image.rotate(90)
                gt_image = gt_image.rotate(90)

            lr_image = lr_image.resize((lr_image.size[0] // self.upscale, lr_image.size[1] // self.upscale))

            save_path_lr = os.path.join(self.output_dir, f"image_{i}_lr.{self.extension}")
            save_path_gt = os.path.join(self.output_dir, f"image_{i}_gt.{self.extension}")

            lr_image.convert("L").save(save_path_lr)
            gt_image.convert("L").save(save_path_gt)