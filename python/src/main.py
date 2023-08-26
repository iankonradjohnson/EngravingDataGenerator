import yaml
import sys

from src.factory.synthetic_data_generator_factory import SyntheticDataGeneratorFactory


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <config_file>")
        return

    config_file = sys.argv[1]

    with open(config_file, 'r') as config_stream:
        config_data = yaml.safe_load(config_stream)

    generators = SyntheticDataGeneratorFactory.create_generators(config_data)

    for generator in generators:
        generator.generate_data()


if __name__ == "__main__":
    main()
