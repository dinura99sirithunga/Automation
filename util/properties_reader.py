import os

def read_properties(file_path):
    config = {}
    # Get the absolute path to the config file
    absolute_path = os.path.join(os.path.dirname(__file__), '..', file_path)

    with open(absolute_path, 'r') as file:
        for line in file:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config
