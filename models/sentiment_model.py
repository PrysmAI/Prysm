from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment polarity of input text.
    :param text: Text input to analyze.
    :return: Sentiment polarity (-1 to 1) and sentiment label.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    sentiment_label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return polarity, sentiment_label

# Example usage
if __name__ == "__main__":
    sample_text = "I'm feeling very hopeful today about my progress."
    score, label = analyze_sentiment(sample_text)
    print(f"Sentiment Score: {score}, Label: {label}")
