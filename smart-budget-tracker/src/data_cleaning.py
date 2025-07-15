import pandas as pd

def load_data(file_path):
    """Load transaction data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(data):
    """Clean the transaction data."""
    # Handle missing values
    data.dropna(subset=['date', 'amount', 'description'], inplace=True)
    
    # Convert 'date' to datetime format
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    
    # Remove any rows with invalid dates
    data.dropna(subset=['date'], inplace=True)
    
    # Ensure 'amount' is numeric
    data['amount'] = pd.to_numeric(data['amount'], errors='coerce')
    
    # Remove any rows with invalid amounts
    data.dropna(subset=['amount'], inplace=True)
    
    return data

def save_to_excel(data, output_file):
    """Save the cleaned data to an Excel file."""
    try:
        data.to_excel(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to Excel: {e}")

if __name__ == "__main__":
    # Example usage
    input_file = '../data/sample_transactions.csv'
    output_file = '../data/processed_transactions.xlsx'
    
    transaction_data = load_data(input_file)
    if transaction_data is not None:
        cleaned_data = clean_data(transaction_data)
        save_to_excel(cleaned_data, output_file)