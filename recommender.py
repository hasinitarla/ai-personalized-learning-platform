def recommend_learning_path(user_profile: dict) -> list:
    interests = user_profile.get("interests", [])
    levels = user_profile.get("levels", {})

    recommendations = []
    for topic in interests:
        level = levels.get(topic, "beginner")
        if level == "beginner":
            next_level = "intermediate"
        elif level == "intermediate":
            next_level = "advanced"
        else:
            next_level = "mastery"
        recommendations.append(f"Next: {topic} ({next_level} level)")

    return recommendations
