import unittest
import pandas as pd
from src.preprocessing.feature_engineering import extract_features

class TestPreprocessing(unittest.TestCase):
    def test_feature_extraction(self):
        input_path = "data/processed/cleaned_data.csv"
        output_path = "data/processed/test_features.csv"
        extract_features(input_path, output_path)
        
        data = pd.read_csv(output_path)
        self.assertTrue(len(data.columns) > 1, "Feature extraction failed")

if __name__ == "__main__":
    unittest.main()
