import pandas as pd

def clean_data(input_path, output_path):
    """
    Clean raw mental health data.
    :param input_path: Path to raw data.
    :param output_path: Path to save cleaned data.
    """
    data = pd.read_csv(input_path)
    data.dropna(inplace=True)  # Drop missing values
    data = data.drop_duplicates()  # Remove duplicates
    
    # Save cleaned data
    data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

# Example usage
if __name__ == "__main__":
    clean_data("../data/raw/raw_data.csv", "../data/processed/cleaned_data.csv")
