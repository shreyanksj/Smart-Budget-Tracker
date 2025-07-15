import pandas as pd

def export_to_excel(dataframe, file_path):
    """
    Exports the given DataFrame to an Excel file at the specified file path.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame to export.
    file_path (str): The path where the Excel file will be saved.
    """
    try:
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            # Convert the dataframe to an XlsxWriter Excel object.
            dataframe.to_excel(writer, sheet_name='Processed Transactions', index=False)
        
        print(f"Data exported successfully to {file_path}")
    except Exception as e:
        print(f"An error occurred while exporting to Excel: {e}")