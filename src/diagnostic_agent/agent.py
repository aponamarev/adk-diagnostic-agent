"""ManagerAgent: orchestrates data collection vs. diagnosis based on session state."""

from diagnostic_agent.sub_agents.initial_diagnosis_agent import (
    initial_diagnosis_agent,
)
from diagnostic_agent.sub_agents.manager_agent import DiagnosticManagerAgent
from diagnostic_agent.sub_agents.parsing_agent import parsing_agent
from diagnostic_agent.sub_agents.question_generation_agent import (
    question_generation_agent,
)

root_agent = DiagnosticManagerAgent(
    name="diagnostic_agent",
    description="This agent is responsible for orchestrating the diagnostic process.",
    inquiry_agent=question_generation_agent,
    parsing_agent=parsing_agent,
    initial_diagnosis_agent=initial_diagnosis_agent,
)
