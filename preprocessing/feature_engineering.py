import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def extract_features(data_path, output_path):
    """
    Extracts features from user input data (text/symptoms).
    :param data_path: Path to the cleaned data CSV.
    :param output_path: Path to save feature-extracted data.
    """
    # Load data
    data = pd.read_csv(data_path)

    # Example: Feature engineering for text columns
    if 'user_input' in data.columns:
        vectorizer = CountVectorizer(max_features=100)
        text_features = vectorizer.fit_transform(data['user_input']).toarray()
        feature_df = pd.DataFrame(text_features, columns=vectorizer.get_feature_names_out())

        # Combine original data with features
        feature_engineered_data = pd.concat([data, feature_df], axis=1)
        feature_engineered_data.drop('user_input', axis=1, inplace=True)

        # Save output
        feature_engineered_data.to_csv(output_path, index=False)
        print(f"Features extracted and saved to {output_path}")
    else:
        print("No 'user_input' column found in the dataset.")

# Example usage
if __name__ == "__main__":
    extract_features("../data/processed/cleaned_data.csv", "../data/processed/feature_engineered_data.csv")
