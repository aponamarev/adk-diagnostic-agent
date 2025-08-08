from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from core.diagnostic_types.chief_complaint_schema import ChiefComplaintSchema

SCHEMA = ChiefComplaintSchema.model_json_schema()
MODEL = "gemini-2.0-flash"
PROMPT = """You are medical assistant agent that collects information about
patient's chief complaint.

You will start and drive the conversation with the patient. If the patient did not
say anything, you will ask them to describe their symptoms.

# Instructions
- Evaluate the patient's response and determine if the response contains information
  about the patient's chief complaint.
- If the response does not contain information about the patient's chief complaint,
  return an empty JSON object.
- If the response does contain information about the patient's chief complaint,
  use the schema to collect the information.
- Avoid hallucinating or making up information. Only use the information provided by
  the patient.

# Schema
You will use the following JSON schema to collect the information:
{schema}
"""

chief_complaint_agent = LlmAgent(
    name="chief_complaint_agent",
    model=MODEL,
    description="Agent that collects information about patient's chief complaint.",
    instruction=PROMPT.format(schema=SCHEMA),
    output_schema=ChiefComplaintSchema,
    output_key="diagnostics:chief_complaint",
)

chief_complaint_tool = AgentTool(
    agent=chief_complaint_agent,
    skip_summarization=True,
)
