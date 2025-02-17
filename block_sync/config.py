import os
import yaml

def load_config(config_path):
    """
    Load configuration from a YAML file.

    Parameters:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed configuration data.
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
