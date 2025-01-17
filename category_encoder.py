import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the training dataset
X_train = pd.read_csv('transactions_X_train.csv')

# Ensure the 'category' column exists
if 'category' not in X_train.columns:
    raise ValueError("The 'category' column is not present in the dataset.")

# Initialize and fit the LabelEncoder for 'category'
category_encoder = LabelEncoder()
category_encoder.fit(X_train['category'])

# Save the encoder to a .pkl file
with open('category_encoder.pkl', 'wb') as file:
    pickle.dump(category_encoder, file)

print("Category encoder has been saved successfully!")
