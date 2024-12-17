import pandas as pd
import matplotlib.pyplot as plt

def visualize_trends(data_path):
    """
    Generate visual insights from mental health data trends.
    :param data_path: Path to trends.json file.
    """
    # Load data
    data = pd.read_json(data_path)

    # Example: Plot symptom frequency
    if "symptom_trends" in data.columns:
        data['symptom_trends'].plot(kind="bar", title="Symptom Trends Over Time")
        plt.xlabel("Symptoms")
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("No 'symptom_trends' found in the JSON file.")

# Example usage
if __name__ == "__main__":
    visualize_trends("../data/trends.json")
