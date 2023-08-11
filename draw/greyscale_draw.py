from PIL import ImageDraw, Image


class GreyscaleDraw:
    def __init__(self, im):
        self.im = im

    def line(self, sequence, fill, width):
        start, end = sequence

        int_width = int(width)
        frac_width = width - int_width

        base_color = int(255 * (1 - frac_width))
        alpha_color = int(255 * frac_width)

        # Draw the thicker part of the line
        draw = ImageDraw.Draw(self.im)
        draw.line((start, end), fill=(fill[0], fill[1], fill[2], base_color), width=int_width)

        # Draw the overlay line, representing the fractional part of the width
        if frac_width > 0:
            overlay = Image.new("RGBA", self.im.size, (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)

            overlay_draw.line((start, end), fill=(fill[0], fill[1], fill[2], alpha_color), width=int_width + 1)
            self.im.paste(Image.alpha_composite(self.im, overlay))
