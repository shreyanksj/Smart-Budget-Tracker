import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

def load_data(file_path):
    return pd.read_excel(file_path)

def prepare_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['amount'] = df['amount'].astype(float)
    return df

def predict_future_spending(df, months_ahead=3):
    df_grouped = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    df_grouped['time'] = np.arange(len(df_grouped))

    X = df_grouped[['time']]
    y = df_grouped['amount']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    future_times = np.arange(len(df_grouped), len(df_grouped) + months_ahead).reshape(-1, 1)
    future_predictions = model.predict(future_times)

    return future_predictions

def main():
    file_path = '../data/processed_transactions.xlsx'
    df = load_data(file_path)
    df = prepare_data(df)
    future_spending = predict_future_spending(df)
    print("Future spending predictions for the next months:", future_spending)

if __name__ == "__main__":
    main()