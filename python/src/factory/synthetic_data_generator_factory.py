from src.generators.random_banding_generator import RandomBandingGenerator
from src.generators.line_banding_generator import LineBandingGenerator


class SyntheticDataGeneratorFactory:
    @staticmethod
    def create_generators(config_data):
        generators = []

        for generator_config in config_data.get("generators", []):

            generator_type = generator_config.get("type")
            if generator_type == "line_banding":
                generators.append(LineBandingGenerator(generator_config))
            elif generator_type == "random_banding":
                generators.append(RandomBandingGenerator(generator_config))

        return generators
