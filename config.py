import yaml


def get_config():
    with open('config.yaml', 'r') as f:
        cfg = yaml.safe_load(f)
    return cfg


config = get_config()