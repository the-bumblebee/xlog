import os
import dotenv
import importlib.resources
import yaml
from platformdirs import user_config_dir

dotenv.load_dotenv()

def _get_config_path(config_base_dir):
    os.makedirs(config_base_dir, exist_ok=True)
    config_file_path = os.path.join(config_base_dir, "config.yaml")
    return config_file_path

def _load_config(config_file_path = ""):
    if not os.path.exists(config_file_path):
        return {}
    try:
        with open(config_file_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
    except yaml.YAMLError as e:
        print(f"Error loading config file: {e}")
        exit(1)
    return config

def _get_value_from_config(config, key):
    keys = key.split('.')
    value = config
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            raise KeyError(f"Key '{key}' not found in config")
    return value

_RESOURCES_PATH = importlib.resources.files('xlog').joinpath('resources')
_CONFIG_BASE_DIR = user_config_dir(appname="xlog")
_CONFIG = _load_config(_get_config_path(_CONFIG_BASE_DIR))

CONFIG_PATH = _get_config_path(_CONFIG_BASE_DIR)
GOOGLE_CLIENT_PATH = os.getenv('GOOGLE_CLIENT_PATH', _RESOURCES_PATH.joinpath('client_secrets.json'))
GOOGLE_TOKEN_PATH = os.getenv('GOOGLE_TOKEN_PATH') or _get_value_from_config(_CONFIG, 'google.token_path')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID') or _get_value_from_config(_CONFIG, 'google.spreadsheet_id')
SHEET_NAME = os.getenv('SHEET_NAME')