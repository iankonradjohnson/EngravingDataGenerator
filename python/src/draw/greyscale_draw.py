import math

from PIL import ImageDraw, Image


class GreyscaleDraw:
    def __init__(self, im):
        self.im = im

    def line(self, sequence, fill, width):
        start, end = sequence

        # Gradient steps, modify to adjust gradient smoothness
        steps = 5
        step_width = width / steps

        for i in range(1, steps):
            alpha = int(255 * (math.log(i + 1) / math.log(steps)))
            overlay = Image.new("RGBA", self.im.size, (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)

            current_width = (steps - i) * step_width
            overlay_draw.line((start, end), fill=(fill[0], fill[1], fill[2], alpha), width=int(current_width))
            self.im.paste(Image.alpha_composite(self.im, overlay))
