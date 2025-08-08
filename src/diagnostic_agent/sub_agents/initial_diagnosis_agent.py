from google.adk.agents.llm_agent import LlmAgent

from core.settings import diagnostic_settings

PROMPT = f"""
You are an AI doctor - General Practitioner AI.

# Goals
Your only goal is to make an initial diagnosis based on the collected information.

# Instructions
- You will be given the collected information.
- Evaluate the collected information and make an initial diagnosis.


# Collected Information
{{{diagnostic_settings.diagnostic_field}}}

**Make the diagnosis now!**
"""

initial_diagnosis_agent = LlmAgent(
    name="initial_diagnosis_agent",
    model=diagnostic_settings.model_name,
    description="This agent is used to make an initial diagnosis based on the collected information.",
    instruction=PROMPT,
)
