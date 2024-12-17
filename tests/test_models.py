import unittest
from src.models.sentiment_model import analyze_sentiment
from src.models.classification_model import classify_disorder

class TestModels(unittest.TestCase):
    def test_sentiment_analysis(self):
        text = "I feel very happy and optimistic today."
        polarity, label = analyze_sentiment(text)
        self.assertGreater(polarity, 0)
        self.assertEqual(label, "Positive")

    def test_disorder_classification(self):
        # Dummy test for classification
        result = classify_disorder("../data/processed/cleaned_mental_health_data.csv")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
