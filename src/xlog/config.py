import os
import dotenv
import importlib.resources

dotenv.load_dotenv()
_RESOURCES_PATH = importlib.resources.files('xlog').joinpath('resources')

GOOGLE_CLIENT_PATH = os.getenv('GOOGLE_CLIENT_PATH', _RESOURCES_PATH.joinpath('client_secret.json'))
GOOGLE_TOKEN_PATH = os.getenv('GOOGLE_TOKEN_PATH', os.path.join(os.path.dirname(__file__), 'secrets', 'token.json'))
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
SHEET_NAME = os.getenv('SHEET_NAME')