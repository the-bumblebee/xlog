from xlog import utils
import argparse

def start():
    parser = argparse.ArgumentParser(description="Expense Logger CLI")
    parser.add_argument("description", type=str, help="Description of the expense")
    parser.add_argument("amount", type=float, help="Amount of the expense")
    args = parser.parse_args()
    run(args)

def run(args):
    last_row_index = utils.get_last_row_index("A:A")
    results = utils.add_expense(last_row_index, args.description, args.amount)
    print(f"Expense added: \"{args.description}\" - ₹ {args.amount:.2f}")