# credit cards dataset preprocessing 
'''
import pandas as pd

def preprocess_cards(card_file, output_file):
    print("Processing card data...")
    try:
        # Read the dataset with proper encoding
        df = pd.read_csv(card_file, delimiter=',', encoding='utf-8')

        # Drop empty columns
        df = df.dropna(how='all', axis=1)

        # Clean column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Replace "?" with "₹" in specific columns
        currency_columns = ['annual_fee', 'joining_fee', 'reward_points']
        for col in currency_columns:
            df[col] = df[col].str.replace('?', '₹', regex=False)

        # Handle currency formatting and convert numerical columns
        for col in ['annual_fee', 'joining_fee']:
            df[col] = df[col].replace({r'[₹,]': ''}, regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        # Normalize text columns
        df['card_name'] = df['card_name'].str.title()
        df['categories_for_rewards'] = df['categories_for_rewards'].str.title()

        # Save the processed data
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Processed card data saved to {output_file}")
        return df

    except Exception as e:
        print(f"Error processing card data: {e}")
        return None

# File paths
card_file = "credit_cards.csv"  # Replace with your file name
processed_card_file = "processed_credit_cards.csv"

# Process the card dataset
if __name__ == "__main__":
    processed_cards = preprocess_cards(card_file, processed_card_file)

    '''

#transactions datset preprocessing
import pandas as pd

def preprocess_transactions(transaction_file, output_file):
    print("Processing transaction data...")
    try:
        # Read the dataset
        df = pd.read_csv(transaction_file, delimiter=',', encoding='utf-8')

        # Drop empty columns
        df = df.dropna(how='all', axis=1)

        # Clean column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Handle date column
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Normalize text in categorical columns
        text_columns = ['mode', 'names', 'category']
        for col in text_columns:
            df[col] = df[col].str.strip().str.title()

        # Handle numerical columns
        numeric_columns = ['amount', 'balance']
        for col in numeric_columns:
            df[col] = df[col].replace({r'[₹,]': ''}, regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Filter out invalid rows if needed
        df = df.dropna(subset=['date', 'amount', 'balance'])

        # Save the processed data
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Processed transaction data saved to {output_file}")
        return df

    except Exception as e:
        print(f"Error processing transaction data: {e}")
        return None

# File paths
transaction_file = "transactions.csv"  # Replace with your file name
processed_transaction_file = "processed_transactions.csv"

# Process the transactions dataset
if __name__ == "__main__":
    processed_transactions = preprocess_transactions(transaction_file, processed_transaction_file)
