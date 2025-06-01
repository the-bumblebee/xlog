import os
from googleapiclient.discovery import build 
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from xlog.config import GOOGLE_CLIENT_PATH, GOOGLE_TOKEN_PATH

SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
]

credentials = None
if os.path.exists(GOOGLE_TOKEN_PATH):
    credentials = Credentials.from_authorized_user_file(GOOGLE_TOKEN_PATH, SCOPES)
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        if not GOOGLE_CLIENT_PATH:
            raise ValueError("Google client secrets file path is not set in environment variable 'GOOGLE_CLIENT_PATH'")
        if not os.path.exists(GOOGLE_CLIENT_PATH):
            raise FileNotFoundError(f"Client secrets file not found at {GOOGLE_CLIENT_PATH}")
        flow = InstalledAppFlow.from_client_secrets_file(
        GOOGLE_CLIENT_PATH, scopes=SCOPES)
        credentials = flow.run_local_server(port=0, open_browser=False)
        with open(GOOGLE_TOKEN_PATH, 'w') as token_file:
            token_file.write(credentials.to_json())

spreadsheet_service = build('sheets', 'v4', credentials=credentials)
