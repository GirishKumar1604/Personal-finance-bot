import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Function to load data from Excel file
def load_data(file_path):
    df = pd.read_excel(file_path)  # Load data from the given Excel file
    return df

# Function to train the classifier
def train_classifier(df):
    # Check for missing values in the 'Label' column
    print(f'Missing values in Label column: {df["Label"].isnull().sum()}')  # Shows NaN count
    
    # Drop rows where the target variable 'Label' has missing values (NaN)
    df = df.dropna(subset=['Label'])
    
    # Check again to ensure no missing values in 'Label'
    print(f'Missing values in Label column after cleaning: {df["Label"].isnull().sum()}')  # Should be 0

    # Assuming 'SMS' is the feature column, and 'Label' is the target
    X = df['SMS']  # Features (SMS text)
    y = df['Label']  # Target (category labels)

    # Convert SMS texts to feature vectors using TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    X_vect = vectorizer.fit_transform(X)

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

    # Initialize and train the Naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = classifier.predict(X_test)

    # Evaluate the classifier
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%')

# Main execution
if __name__ == "__main__":
    # Load the Excel file (adjust file path as needed)
    file_path = 'C:\\Users\\Girish\\Downloads\\Prepared bank transactions SMS dataset .xlsx'  # Replace with your actual file path
    df = load_data(file_path)

    # Check first few rows of the dataset
    print("First 5 rows of the data:")
    print(df.head())

    # Train the classifier and evaluate the model
    train_classifier(df)
