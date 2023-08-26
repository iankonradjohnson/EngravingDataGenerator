from unittest import TestCase
from unittest.mock import MagicMock

from PIL import Image

from src.draw.greyscale_draw import GreyscaleDraw


class TestGreyscaleDraw(TestCase):

    def setUp(self) -> None:
        self.mock_image = MagicMock(spec=Image.Image)
        self.mock_overlay = MagicMock(spec=Image.Image)

        self.greyscale_draw = GreyscaleDraw(self.mock_image)

    def test_line(self):
        self.fail()
