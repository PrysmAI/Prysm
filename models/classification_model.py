import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def classify_disorder(data_path):
    """
    Classifies mental health conditions based on symptoms using a simple ML model.
    :param data_path: Path to processed dataset with features and target labels.
    """
    # Load data
    data = pd.read_csv(data_path)
    X = data.drop(columns=["condition"])  # Features
    y = data["condition"]                # Target labels

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predict and evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy:.2f}")
    return model

# Example usage
if __name__ == "__main__":
    classify_disorder("../data/processed/feature_engineered_data.csv")
