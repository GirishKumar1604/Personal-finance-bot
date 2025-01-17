# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# Load preprocessed datasets
transactions_df = pd.read_csv('transactions_features.csv')
credit_cards_df = pd.read_csv('credit_cards_features.csv')

# Replace 'target_column_name' with the actual target column name in each dataset
# For demonstration purposes, replace with actual names from your data
target_column_transactions = 'category'  # Example for transactions
target_column_credit_cards = 'reward_points'  # Example for credit cards

# Splitting Transactions Dataset
X_transactions = transactions_df.drop(columns=[target_column_transactions])
y_transactions = transactions_df[target_column_transactions]

# Perform Train, Validation, Test Split for Transactions
X_train_trans, X_temp_trans, y_train_trans, y_temp_trans = train_test_split(
    X_transactions, y_transactions, test_size=0.3, random_state=42
)
X_val_trans, X_test_trans, y_val_trans, y_test_trans = train_test_split(
    X_temp_trans, y_temp_trans, test_size=0.5, random_state=42
)

# Splitting Credit Cards Dataset
X_credit_cards = credit_cards_df.drop(columns=[target_column_credit_cards])
y_credit_cards = credit_cards_df[target_column_credit_cards]

# Perform Train, Validation, Test Split for Credit Cards
X_train_cc, X_temp_cc, y_train_cc, y_temp_cc = train_test_split(
    X_credit_cards, y_credit_cards, test_size=0.3, random_state=42
)
X_val_cc, X_test_cc, y_val_cc, y_test_cc = train_test_split(
    X_temp_cc, y_temp_cc, test_size=0.5, random_state=42
)

# Save the splits to CSV files

# Transactions Data
X_train_trans.to_csv('transactions_X_train.csv', index=False)
X_val_trans.to_csv('transactions_X_val.csv', index=False)
X_test_trans.to_csv('transactions_X_test.csv', index=False)
y_train_trans.to_csv('transactions_y_train.csv', index=False)
y_val_trans.to_csv('transactions_y_val.csv', index=False)
y_test_trans.to_csv('transactions_y_test.csv', index=False)

# Credit Cards Data
X_train_cc.to_csv('credit_cards_X_train.csv', index=False)
X_val_cc.to_csv('credit_cards_X_val.csv', index=False)
X_test_cc.to_csv('credit_cards_X_test.csv', index=False)
y_train_cc.to_csv('credit_cards_y_train.csv', index=False)
y_val_cc.to_csv('credit_cards_y_val.csv', index=False)
y_test_cc.to_csv('credit_cards_y_test.csv', index=False)

print("Data splitting completed! Splits have been saved to CSV files.")
