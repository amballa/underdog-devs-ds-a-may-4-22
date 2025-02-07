from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


vader = SentimentIntensityAnalyzer()


def vader_score(text: str):
    """Return an intuitive string (Positive, Negative or Neutral) base on the compound score of text from vader analysis."""
    score = vader.polarity_scores(text)["compound"]
    if score > 0.3:
        return "Positive"
    elif score < -0.3:
        return "Negative"
    else:
        return "Neutral"


if __name__ == '__main__':
    print(vader_score("good but not great"))
    """
    This is to test the expected result requested in api.py

    """
    # Numeric
    print({"Result": vader_score("Astring is so cool wow hot damn")})
    # String text.
    print({"Result": vader_score("Astring is so cool wow hot damn")})

