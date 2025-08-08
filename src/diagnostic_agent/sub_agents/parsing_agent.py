"""Parsing agent that parses the patient's response and extracts the information."""

from google.adk.agents.llm_agent import LlmAgent

from core.diagnostic_types.chief_complaint import ChiefComplaintType
from core.settings import diagnostic_settings

SCHEMA = ChiefComplaintType.model_json_schema()

PROMPT = f"""You are a parsing agent responsible for parsing the patient's response and extracting the information.

# Instructions
- You will be given a patient's response.
- You will need to extract the information from the response according to the schema.
- If the response is not related to the schema, you should return an empty JSON.
- You will need to return the information in a structured JSON format.

# Schema
{SCHEMA}
"""

parsing_agent = LlmAgent(
    name="parsing_agent",
    model=diagnostic_settings.model_name,
    description="Use this agent to parse the patient's response and extract relevant information.",
    instruction=PROMPT,
    output_schema=ChiefComplaintType,
    output_key=diagnostic_settings.diagnostic_field,
)
