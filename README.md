🎓 AI-Powered Personalized Learning Platform

An interactive Streamlit application that leverages LLMs (Gemini, GPT, etc.) and adaptive learning algorithms to deliver tailored educational experiences. Learners can input their interests, skill levels, and feedback to receive custom learning paths, dynamic quizzes, and personalized study guidance.

✨ Features

📅 Interactive Learner Profiles: Collect name, interests, skill levels, and learning feedback.

🔄 Personalized Content Recommendations: Adaptive pathways based on interests and experience.

✍️ AI-Generated Feedback: Real-time feedback powered by large language models (LLMs).

🖋️ Adaptive Quiz Generation: Custom quizzes based on selected topics and skill levels.

🤔 Sentiment Analysis: Analyze and visualize feedback to assess learner engagement.

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/hasinitarla/ai-personalized-learning-platform.git
cd ai-personalized-learning-platform

2. Install Dependencies

pip install -r requirements.txt

3. Add Your Environment Variables

Create a .env file and add your Gemini (or GPT) API key:

GEMINI_API_KEY=your_key_here

4. Run the Streamlit App

streamlit run main.py

🌐 Project Structure

ai-personalized-learning-platform/
├── main.py                  # Main Streamlit UI
├── services/
│   ├── recommender.py       # Learning path recommender
│   ├── assessment.py        # Adaptive quiz generator
│   └── gemini_api.py        # AI feedback handler
├── ui/
│   └── components.py        # UI components (profile, feedback)
├── utils/
│   └── nlp_tools.py         # Sentiment analysis tools
├── requirements.txt         # Python dependencies
├── .env                     # Your API key (not committed)
└── README.md

📆 Example Usage

Open the app.

Enter your name, topics of interest (e.g., AI, NLP, ML), and your level of expertise.

Submit your profile.

View:

Personalized study paths.

AI-generated suggestions.

Emotional analysis of your feedback.

A quiz tailored to your learning level.

👁️ How It Works

User input is stored using st.session_state.

Recommendations and quizzes are generated dynamically from services.

Feedback is passed to LLMs via Gemini/GPT APIs for context-aware suggestions.

Feedback is also run through sentiment analysis for visualization.

🔒 License

This project is licensed under the MIT License.

✨ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

🚩 Future Enhancements

User authentication and login

Persistent learner history

Gamified quiz system

Integration with external content providers

☑️ Built With

Streamlit

Google Generative AI / Gemini

TextBlob

Python

