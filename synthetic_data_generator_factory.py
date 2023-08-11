from generators.horizontal_lines_banding_generator import HorizontalLinesBandingGenerator
from generators.random_banding_generator import RandomBandingGenerator
from generators.vertical_lines_banding_generator import VerticalLinesBandingGenerator


class SyntheticDataGeneratorFactory:
    @staticmethod
    def create_generators(config_data):
        generators = []

        for generator_config in config_data.get("generators", []):

            generator_type = generator_config.get("type")
            if generator_type == "vertical_lines_banding":
                generators.append(VerticalLinesBandingGenerator(generator_config))
            elif generator_type == "horizontal_lines_banding":
                generators.append(HorizontalLinesBandingGenerator(generator_config))
            elif generator_type == "random_banding":
                generators.append(RandomBandingGenerator(generator_config))

        return generators
