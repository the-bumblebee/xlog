from datetime import datetime
from xlog.auth import spreadsheet_service
from xlog.config import SPREADSHEET_ID, SHEET_NAME


def get_last_row_index(cell_range):
    results = (
        spreadsheet_service.spreadsheets()
        .values()
        .get(spreadsheetId = SPREADSHEET_ID, range = f"{SHEET_NAME}!{cell_range}")
        .execute()
    )
    return len(results.get('values', [])) + 1

def add_expense(row_index, description, amount):
    results = (
        spreadsheet_service.spreadsheets()
        .batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body={
                'requests': [
                    {
                        "insertRange": {
                            "range": {
                                "sheetId": 0,
                                "startRowIndex": row_index - 1,
                                "endRowIndex": row_index,
                            },
                            "shiftDimension": "ROWS",
                        }
                    }
                ]
            }
        )
        .execute()
    )
    results = (
        spreadsheet_service.spreadsheets()
        .values()
        .update(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A{row_index}:D{row_index}",
            valueInputOption="USER_ENTERED",
            body={"values": [[datetime.today().strftime("%Y-%m-%d"), description, amount, f"= D{row_index - 1} - C{row_index}"]]},
        )
        .execute()
    )
    return results