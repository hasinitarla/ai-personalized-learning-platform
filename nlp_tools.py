def extract_sentiment(feedback: str) -> str:
    feedback = feedback.lower()
    if any(word in feedback for word in ["love", "great", "awesome", "helpful"]):
        return "positive"
    elif any(word in feedback for word in ["bad", "confusing", "difficult", "hate"]):
        return "negative"
    return "neutral"

