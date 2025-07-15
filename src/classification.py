from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Example preprocessing steps
    data['date'] = pd.to_datetime(data['date'])
    data['amount'] = data['amount'].replace('[\$,]', '', regex=True).astype(float)
    data['category'] = data['description'].apply(classify_transaction)
    return data

def classify_transaction(df):
    def get_category(description):
        desc = str(description).lower()
        if 'food' in desc or 'restaurant' in desc or 'coffee' in desc:
            return 'Food'
        elif 'rent' in desc:
            return 'Rent'
        elif 'utility' in desc or 'electricity' in desc or 'gas' in desc:
            return 'Utilities'
        elif 'shop' in desc or 'amazon' in desc:
            return 'Shopping'
        elif 'uber' in desc or 'transport' in desc or 'bus' in desc:
            return 'Transport'
        elif 'concert' in desc or 'movie' in desc or 'entertainment' in desc:
            return 'Entertainment'
        else:
            return 'Other'

    df['category'] = df['description'].apply(get_category)
    return df

def train_model(data):
    X = data[['amount']]  # Features
    y = data['category']   # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()  # You can switch to LogisticRegression() if needed
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

    return model

def main():
    file_path = '../data/sample_transactions.csv'  # Adjust path as necessary
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    model = train_model(processed_data)

if __name__ == "__main__":
    main()