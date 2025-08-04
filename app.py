import streamlit as st
from services.recommender import recommend_learning_path
from services.assessment import generate_adaptive_quiz
from utils.nlp_tools import extract_sentiment
from ui.components import *
from services.gemini_api import get_ai_feedback

st.set_page_config(page_title="AI Education Platform", layout="wide")
st.title("🎓 AI-Powered Personalized Learning")

st.markdown("""
### 📘 How to Use This Platform
1. **Enter your name** — to personalize the experience.
2. **Specify topics you're interested in** — e.g., AI, NLP, ML, Deep Learning, etc.
3. **Choose your level** for each topic — beginner / intermediate / advanced.
   - For example:
     - AI level: How well you understand AI overall.
     - NLP level: How experienced you are with Natural Language Processing.
4. **Provide learning feedback** — so the AI can improve recommendations.
5. **Submit the form** to update your profile.
6. **Review recommendations, feedback, and sentiment analysis**.
7. **Choose a topic and generate an adaptive quiz** tailored to your level.
8. Optional: Use the 🔄 Reset button to start over.
""")

# --- Initialize session state ---
if "profile" not in st.session_state:
    st.session_state.profile = None

# --- Collect Learner Input Interactively ---
with st.form("learner_form", clear_on_submit=False):
    name = st.text_input("👤 Name", "Enter your name")
    interests_input = st.text_input("📚 What topics are you interested in learning? (comma-separated)", "topic")
    interests = [topic.strip() for topic in interests_input.split(",") if topic.strip()]

    st.markdown("📈 Choose your skill level for each topic:")
    levels = {}
    for topic in interests:
        levels[topic] = st.selectbox(f"{topic} level", ["beginner", "intermediate", "advanced"], key=topic)

    feedback = st.text_area("🗣️ Share your feedback or learning experience")

    submitted = st.form_submit_button("Update Profile")

if submitted:
    st.session_state.profile = {
        "name": name,
        "interests": interests,
        "levels": levels,
        "feedback": feedback
    }

# --- Use Profile from Session ---
if st.session_state.profile:
    profile = st.session_state.profile

    user_profile_display(profile)

    # Show personalized recommendations
    recs = recommend_learning_path(profile)
    show_recommendations(recs)

    # AI Feedback
    st.subheader("✍️ AI-Generated Learning Feedback")
    feedback_prompt = f"Provide personalized study advice for this learner: {profile}"
    ai_response = get_ai_feedback(feedback_prompt)
    st.write(ai_response)

    # Feedback Sentiment
    sentiment = extract_sentiment(profile["feedback"])
    show_feedback_analysis(sentiment)

    # Adaptive Quiz
    st.subheader("📝 Generate Adaptive Quiz")
    quiz_topic = st.selectbox("Select a topic for quiz", profile["interests"])
    quiz_level = profile["levels"].get(quiz_topic, "beginner")
    if st.button("Generate Quiz"):
        question = generate_adaptive_quiz(quiz_topic, quiz_level)
        st.success(question)

    # Optional: Reset profile
    if st.button("🔄 Reset Profile"):
        st.session_state.profile = None
        st.experimental_rerun()
