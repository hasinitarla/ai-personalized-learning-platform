import json

def load_learner_data():
    with open('data/learners.json') as f:
        return json.load(f)
