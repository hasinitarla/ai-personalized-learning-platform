import streamlit as st

def user_profile_display(profile):
    st.subheader("👤 Learner Profile")
    st.json(profile)

def show_recommendations(recommendations):
    st.subheader("📚 Recommended Learning Path")
    for rec in recommendations:
        st.markdown(f"- {rec}")

def show_feedback_analysis(sentiment):
    st.subheader("🧠 Feedback Sentiment")
    st.write(f"Sentiment detected: **{sentiment}**")
