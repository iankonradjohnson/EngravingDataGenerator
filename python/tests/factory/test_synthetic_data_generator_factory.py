from unittest import TestCase

from src.factory.synthetic_data_generator_factory import SyntheticDataGeneratorFactory
from src.generators.line_banding_generator import LineBandingGenerator


class TestSyntheticDataGeneratorFactory(TestCase):
    def test_create_generators_for_line_banding(self):
        config_data = {
            "generators": [{"type": "line_banding", "image": {}}]
        }
        generators = SyntheticDataGeneratorFactory.create_generators(config_data)
        self.assertEqual(len(generators), 1)
        self.assertIsInstance(generators[0], LineBandingGenerator)
