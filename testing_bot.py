#testing the bot with the testing dataset
import pandas as pd
import pickle
from sklearn.metrics import classification_report, accuracy_score

# Load the test datasets
X_test = pd.read_csv('transactions_X_test.csv')
y_test = pd.read_csv('transactions_y_test.csv')

# Load the trained model
with open('spending_behavior_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the encoders
with open('category_encoder.pkl', 'rb') as file:
    category_encoder = pickle.load(file)

with open('mode_encoder.pkl', 'rb') as file:
    mode_encoder = pickle.load(file)

# Encode categorical columns in X_test
categorical_columns = ['category', 'mode']
for col in categorical_columns:
    if col in X_test.columns:
        X_test[col] = X_test[col].map(
            lambda x: category_encoder.transform([x])[0] if col == 'category' else mode_encoder.transform([x])[0]
        )

# Ensure all columns match the training columns
X_test = X_test.drop(columns=['date'], errors='ignore')  # Drop the 'date' column if present
X_test = X_test.reindex(columns=model.feature_names_in_, fill_value=0)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Model Performance on Test Data")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
