# xlog - Expense Logger

`xlog` is a CLI utility to log your expenses on to a google sheet.

## Development Setup

### Requirements

- [uv](https://github.com/astral-sh/uv) CLI tool
- Python 3.10+
- Google Spreadsheet Template
  - Copy this [spreadsheet](https://docs.google.com/spreadsheets/d/1lKPskTn3gYfG2Cdl53N_LkOCg9L9oKMfJzg1Sx_AYiE/edit?usp=sharing) to your drive.
  - Now copy and note down the spreadsheet ID.
- Create a `.env` file with the following:
  - `GOOGLE_CLIENT_PATH=<path/to/client_secrets.json>`
  - *Optional* - `GOOGLE_TOKEN_PATH=<path/to/token.jon>`
  - `SPREADSHEET_ID=<spreadsheet-id-from-above-step>`
  - `SHEET_NAME=Sheet1` - This is the name of workin sheet

### Running
- Activate venv:
```sh
source .venv/bin/activate
```
- Run
```sh
xlog "<expense-description>" <amount>
```

**Note**: This would automatically install the dependencies in `pyproject.yaml` under `.venv/`.