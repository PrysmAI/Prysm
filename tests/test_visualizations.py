import unittest
from src.visualization.insights_dashboard import visualize_trends
import os

class TestVisualizations(unittest.TestCase):
    def test_visualization(self):
        data_path = "../data/trends.json"
        try:
            visualize_trends(data_path)
            self.assertTrue(True)  # Pass if no exception occurs
        except Exception as e:
            self.fail(f"Visualization failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
