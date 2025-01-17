import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load training and validation data
X_train = pd.read_csv('transactions_X_train.csv')
y_train = pd.read_csv('transactions_y_train.csv')
X_val = pd.read_csv('transactions_X_val.csv')
y_val = pd.read_csv('transactions_y_val.csv')

# Ensure target column is extracted correctly
y_train = y_train.values.ravel()  # Flatten to 1D array
y_val = y_val.values.ravel()      # Flatten to 1D array

# Handle categorical columns
categorical_columns = X_train.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    
    # Fit encoder on the training data
    X_train[col] = le.fit_transform(X_train[col])
    
    # Add 'Unknown' to handle unseen labels in validation set
    def encode_with_fallback(val):
        return le.transform([val])[0] if val in le.classes_ else len(le.classes_)
    
    le.classes_ = np.append(le.classes_, 'Unknown')
    X_val[col] = X_val[col].apply(encode_with_fallback)
    
    # Save the encoder for future use
    label_encoders[col] = le

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Validate the model
accuracy = model.score(X_val, y_val)
print(f"Model accuracy on validation data: {accuracy:.2f}")

# Save the encoders and model (optional for deployment)
import joblib
for col, le in label_encoders.items():
    joblib.dump(le, f"{col}_encoder.pkl")
joblib.dump(model, "spending_behavior_model.pkl")
