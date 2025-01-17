import pandas as pd

# File paths
processed_transaction_file = "processed_transactions.csv"
processed_card_file = "processed_credit_cards.csv"

# Load datasets
transactions_df = pd.read_csv(processed_transaction_file)
cards_df = pd.read_csv(processed_card_file)

# Inspect the data
print("Transactions Data:")
print(transactions_df.head())
print("\nCredit Cards Data:")
print(cards_df.head())
