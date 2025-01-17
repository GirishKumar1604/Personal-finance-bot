'''

import pandas as pd

# Load datasets
transactions_df = pd.read_csv('processed_transactions.csv')
cards_df = pd.read_csv('D:\\GK\\Personal finance bot\\processed_credit_cards.csv')

print("Data successfully loaded!")

# Check for missing values
print("Missing values in Transactions Data:")
print(transactions_df.isnull().sum())

print("\nMissing values in Credit Cards Data:")
print(cards_df.isnull().sum())

# Convert date to datetime format for transactions
transactions_df['date'] = pd.to_datetime(transactions_df['date'], errors='coerce')
print("\nTransactions data types:")
print(transactions_df.dtypes)


'''
'''
import pandas as pd

# Load the preprocessed datasets
transactions_path = 'processed_transactions.csv'  # Update with your actual file path
credit_cards_path = 'processed_credit_cards.csv'  # Update with your actual file path

transactions_df = pd.read_csv(transactions_path)
credit_cards_df = pd.read_csv(credit_cards_path)

# Handle Missing Values in Credit Cards Data
credit_cards_df['card_name'].fillna("Unknown Card", inplace=True)
credit_cards_df['issuer_bank'].fillna("Unknown Bank", inplace=True)
credit_cards_df['card_type'].fillna("Regular", inplace=True)  # Default to 'Regular'
credit_cards_df['categories_for_rewards'].fillna("Miscellaneous", inplace=True)

# For numeric columns, replace NaN with 0 or another default value
credit_cards_df['cashback_percentage'].fillna("N/A", inplace=True)  # Replace with N/A if text
credit_cards_df['sign-up_bonus'].fillna("None", inplace=True)  # Replace with "None"
credit_cards_df['reward_points'].fillna("No Rewards", inplace=True)

# Remove Duplicates
transactions_df.drop_duplicates(inplace=True)
credit_cards_df.drop_duplicates(inplace=True)

# Save the cleaned data
transactions_cleaned_path = 'transactions_cleaned.csv'
credit_cards_cleaned_path = 'credit_cards_cleaned.csv'

transactions_df.to_csv(transactions_cleaned_path, index=False)
credit_cards_df.to_csv(credit_cards_cleaned_path, index=False)

print("Data cleaning completed!")
print(f"Cleaned Transactions Data saved at: {transactions_cleaned_path}")
print(f"Cleaned Credit Cards Data saved at: {credit_cards_cleaned_path}")

'''

import pandas as pd

# Load the preprocessed datasets
transactions_path = 'processed_transactions.csv'  # Update with your actual file path
credit_cards_path = 'processed_credit_cards.csv'  # Update with your actual file path

transactions_df = pd.read_csv(transactions_path)
credit_cards_df = pd.read_csv(credit_cards_path)

# Handle Missing Values in Credit Cards Data
credit_cards_df['card_name'] = credit_cards_df['card_name'].fillna("Unknown Card")
credit_cards_df['issuer_bank'] = credit_cards_df['issuer_bank'].fillna("Unknown Bank")
credit_cards_df['card_type'] = credit_cards_df['card_type'].fillna("Regular")  # Default to 'Regular'
credit_cards_df['categories_for_rewards'] = credit_cards_df['categories_for_rewards'].fillna("Miscellaneous")

# For numeric/text fields, replace NaN with defaults
credit_cards_df['cashback_percentage'] = credit_cards_df['cashback_percentage'].fillna("N/A")  # Replace with N/A if text
credit_cards_df['sign-up_bonus'] = credit_cards_df['sign-up_bonus'].fillna("None")  # Replace with "None"
credit_cards_df['reward_points'] = credit_cards_df['reward_points'].fillna("No Rewards")

# Remove Duplicates
transactions_df = transactions_df.drop_duplicates()
credit_cards_df = credit_cards_df.drop_duplicates()

# Save the cleaned data
transactions_cleaned_path = 'transactions_cleaned.csv'
credit_cards_cleaned_path = 'credit_cards_cleaned.csv'

transactions_df.to_csv(transactions_cleaned_path, index=False)
credit_cards_df.to_csv(credit_cards_cleaned_path, index=False)

print("Data cleaning completed!")
print(f"Cleaned Transactions Data saved at: {transactions_cleaned_path}")
print(f"Cleaned Credit Cards Data saved at: {credit_cards_cleaned_path}")
