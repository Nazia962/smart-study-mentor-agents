# tests/test_agents.py
from study_agents.main_agent import MainAgent

def test_main_agent():
    agent = MainAgent()
    output = agent.run("Physics")
    assert "Study Plan" in output
    assert "Quiz" in output
    print("Test Passed!")
