import os
import dotenv

dotenv.load_dotenv()
GOOGLE_CLIENT_PATH = os.getenv('GOOGLE_CLIENT_PATH', os.path.join(os.path.dirname(__file__), 'secrets', 'client_secrets.json'))
GOOGLE_TOKEN_PATH = os.getenv('GOOGLE_TOKEN_PATH', os.path.join(os.path.dirname(__file__), 'secrets', 'token.json'))
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
SHEET_NAME = os.getenv('SHEET_NAME')