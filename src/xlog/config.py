import os
import dotenv
import importlib.resources
import yaml
from platformdirs import user_config_dir

dotenv.load_dotenv()

_RESOURCES_PATH = importlib.resources.files('xlog').joinpath('resources')
_CONFIG_BASE_DIR = user_config_dir(appname="xlog")

def _get_config_file_path(config_base_dir = _CONFIG_BASE_DIR):
    os.makedirs(config_base_dir, exist_ok=True)
    return os.path.join(config_base_dir, "config.yaml")

def load_config():
    config_file_path = _get_config_file_path()
    if not os.path.exists(config_file_path):
        return {}
    try:
        with open(config_file_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
    except yaml.YAMLError as e:
        print(f"Error loading config file: {e}")
        exit(1)
    return config

def dump_config(config):
    config_file_path = _get_config_file_path()
    try:
        with open(config_file_path, 'w') as config_file:
            yaml.safe_dump(config, config_file, default_flow_style=False)
    except yaml.YAMLError as e:
        print(f"Error dumping config file: {e}")
        exit(1)

def get_value_from_config(config, key):
    keys = key.split('.')
    value = config
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            raise KeyError(f"Key '{key}' not found in config")
    return value

CONFIG = load_config()
GOOGLE_CLIENT_PATH = os.getenv('GOOGLE_CLIENT_PATH', _RESOURCES_PATH.joinpath('client_secrets.json'))
# GOOGLE_TOKEN_PATH = os.getenv('GOOGLE_TOKEN_PATH') or get_value_from_config(CONFIG, 'google.token_path')
GOOGLE_TOKEN_PATH = ""
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID') or get_value_from_config(CONFIG, 'google.spreadsheet_id')
SHEET_NAME = os.getenv('SHEET_NAME')