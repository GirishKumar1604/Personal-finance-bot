import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load cleaned datasets
transactions_df = pd.read_csv('transactions_cleaned.csv')
credit_cards_df = pd.read_csv('credit_cards_cleaned.csv')

# =======================
# Feature Engineering for Transactions Data
# =======================

# Extract temporal features
transactions_df['date'] = pd.to_datetime(transactions_df['date'])
transactions_df['year'] = transactions_df['date'].dt.year
transactions_df['month'] = transactions_df['date'].dt.month
transactions_df['day'] = transactions_df['date'].dt.day
transactions_df['weekday'] = transactions_df['date'].dt.day_name()

# Encode categorical features
le_mode = LabelEncoder()
transactions_df['mode_encoded'] = le_mode.fit_transform(transactions_df['mode'])

le_category = LabelEncoder()
transactions_df['category_encoded'] = le_category.fit_transform(transactions_df['category'])

# Scale numerical features
scaler = MinMaxScaler()
transactions_df[['amount_scaled', 'balance_scaled']] = scaler.fit_transform(
    transactions_df[['amount', 'balance']]
)

# Save transactions features
transactions_df.to_csv('transactions_features.csv', index=False)
print("Transactions features saved to transactions_features.csv")

# =======================
# Feature Engineering for Credit Cards Data
# =======================

# Encode categorical features
le_issuer_bank = LabelEncoder()
credit_cards_df['issuer_bank_encoded'] = le_issuer_bank.fit_transform(credit_cards_df['issuer_bank'])

le_card_type = LabelEncoder()
credit_cards_df['card_type_encoded'] = le_card_type.fit_transform(credit_cards_df['card_type'])

# Extract numerical values from cashback_percentage (if applicable)
def extract_cashback(value):
    try:
        return float(value.strip('%')) if '%' in value else 0.0
    except:
        return 0.0

credit_cards_df['cashback_percentage_numeric'] = credit_cards_df['cashback_percentage'].apply(extract_cashback)

# Scale numerical features
credit_cards_df[['annual_fee_scaled', 'joining_fee_scaled']] = scaler.fit_transform(
    credit_cards_df[['annual_fee', 'joining_fee']]
)

# Save credit cards features
credit_cards_df.to_csv('credit_cards_features.csv', index=False)
print("Credit Cards features saved to credit_cards_features.csv")
