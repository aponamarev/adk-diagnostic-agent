"""Question generation agent creates questions to ask the patient.

The goal of the question is collect the most relevant information for the diagnostic process.
"""

from google.adk.agents.llm_agent import LlmAgent

from core.settings import diagnostic_settings
from diagnostic_agent.utils.init_state import initialize_state

PROMPT = f"""You are an AI doctor - General Practitioner AI.

# Goals
Your only goal is to collect the most relevant information from the patient for the diagnostic process.

# Instructions
- You will be given existing information about the patient and missing information.
- Evaluate the missing information and generate questions to ask the patient.

# Existing Information
{{{diagnostic_settings.diagnostic_field}}}

# Missing Information
{{{diagnostic_settings.missing_information_field}}}

**Ask the question now!**
"""


question_generation_agent = LlmAgent(
    name="question_generation_agent",
    model=diagnostic_settings.model_name,
    description="This agent is used to generate questions to ask the patient to collect the missing information.",
    instruction=PROMPT,
    before_agent_callback=initialize_state,
)
