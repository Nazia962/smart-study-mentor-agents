# study_agents/quiz_agent.py
class QuizAgent:
    def generate_quiz(self, topic):
        return [
            {
                "question": f"What is the basic concept of {topic}?",
                "options": ["A) Definition", "B) Formula", "C) Use", "D) None"],
                "answer": "A"
            },
            {
                "question": f"Where is {topic} used?",
                "options": ["A) Industry", "B) Daily life", "C) Research", "D) All"],
                "answer": "D"
            }
        ]
