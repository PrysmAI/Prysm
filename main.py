from preprocessing.feature_engineering import extract_features
from models.sentiment_model import analyze_sentiment
from models.classification_model import classify_disorder
from visualization.insights_dashboard import visualize_trends

def main():
    print("Prysm AI - Mental Health Insights")

    # Step 1: Feature Engineering
    print("Extracting features from data...")
    extract_features("data/processed/cleaned_data.csv", "data/processed/feature_engineered_data.csv")

    # Step 2: Sentiment Analysis
    text_input = "I'm feeling overwhelmed and anxious today."
    polarity, label = analyze_sentiment(text_input)
    print(f"Sentiment Analysis - Score: {polarity}, Label: {label}")

    # Step 3: Disorder Classification
    print("Classifying disorders based on symptoms...")
    classify_disorder("data/processed/feature_engineered_data.csv")

    # Step 4: Data Visualization
    print("Visualizing mental health trends...")
    visualize_trends("data/trends.json")

if __name__ == "__main__":
    main()
