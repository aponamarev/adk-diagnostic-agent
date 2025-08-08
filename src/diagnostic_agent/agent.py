"""ManagerAgent: orchestrates data collection vs. diagnosis based on session state."""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import AgentTool

from core.settings import diagnostic_settings
from diagnostic_agent.sub_agents.initial_diagnosis_agent import initial_diagnosis_agent
from diagnostic_agent.sub_agents.parsing_agent import parsing_agent
from diagnostic_agent.sub_agents.question_generation_agent import (
    question_generation_agent,
)
from diagnostic_agent.utils.init_state import update_missing_information

PROMPT = f"""
You are the ManagerAgent responsible for orchestrating the diagnostic process.

# Goals
Your only goal is to make a decision if we should collect more information or make a diagnosis.

# Instructions
- If any required diagnostic fields are missing, you should use the {question_generation_agent.name} to collect information from the patient.
  - If we asked the question and the patient provided the information, you should execute the following steps:
    1. Use the {parsing_agent.name} to parse user's response and extract relevant information.
    2. Evaluate information extracted by {parsing_agent.name} against the required diagnostic fields.
    3. Make a decision to collect more information or make a diagnosis.
  - On the other hand, if did not provide the information, you should ask the question again.
- If all required diagnostic fields are present, you should use the {initial_diagnosis_agent.name} to make a diagnosis.

# Tools and Agents
You have access to the following agents:
- {question_generation_agent.name}: {question_generation_agent.description}
  -  **Failure**: If the {question_generation_agent.name} returns an error or an empty JSON you should retry call it again.
- {parsing_agent.name}: {parsing_agent.description}
  - **Failure**: If the {parsing_agent.name} returns an error or an empty JSON you should retry call it again.
- {initial_diagnosis_agent.name}: {initial_diagnosis_agent.description}
  - **Failure**: If the {initial_diagnosis_agent.name} returns an error or an empty JSON you should retry call it again.

# Missing Required Diagnostic Fields
- {{{diagnostic_settings.missing_information_field}}}
"""


root_agent = LlmAgent(
    name="diagnostic_agent",
    model=diagnostic_settings.model_name,
    description="Agent that collects patient information necessary to make an initial diagnosis.",
    instruction=PROMPT,
    sub_agents=[question_generation_agent, parsing_agent, initial_diagnosis_agent],
    tools=[AgentTool(parsing_agent, skip_summarization=True)],
    before_agent_callback=update_missing_information,
)
