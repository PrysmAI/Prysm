import pandas as pd

def detect_patterns(data_path):
    """
    Detect behavioral patterns from mental health data.
    :param data_path: Path to the input CSV file.
    :return: Patterns summary.
    """
    data = pd.read_csv(data_path)
    
    # Example pattern: frequency of reported symptoms
    patterns = data['symptom'].value_counts().to_dict()
    
    print("Behavioral Patterns Detected:")
    for symptom, count in patterns.items():
        print(f"{symptom}: {count}")
    return patterns

# Example usage
if __name__ == "__main__":
    detect_patterns('../data/processed/mental_health_data.csv')
