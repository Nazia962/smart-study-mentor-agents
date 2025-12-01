# study_agents/main_agent.py
from study_agents.planner_agent import PlannerAgent
from study_agents.quiz_agent import QuizAgent
from study_agents.summarizer_agent import SummarizerAgent
from study_agents.resource_finder_agent import ResourceFinderAgent

class MainAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.quiz = QuizAgent()
        self.summarizer = SummarizerAgent()
        self.resources = ResourceFinderAgent()

    def run(self, topic):
        plan = self.planner.create_plan(topic)
        summary = self.summarizer.generate_summary(topic)
        quiz = self.quiz.generate_quiz(topic)
        materials = self.resources.find_resources(topic)
        return {
            "Study Plan": plan,
            "Summary": summary,
            "Quiz": quiz,
            "Resources": materials
        }

if __name__ == "__main__":
    agent = MainAgent()
    print(agent.run("Electromagnetism"))
