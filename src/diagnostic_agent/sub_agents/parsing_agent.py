"""Parsing agent that parses the patient's response and extracts the information."""

from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import LlmAgent

from core.diagnostic_types.diagnostic_schema import DiagnosticSchema
from core.settings import diagnostic_settings
from diagnostic_agent.utils.init_state import update_missing_information

SCHEMA = DiagnosticSchema.model_json_schema()

PROMPT = f"""You are a parsing agent responsible for parsing the patient's response and extracting the information.

# Instructions
- You will be given a patient's response to one or more questions.
- Analyze the response to make the best judgement as to what question(s) the user answered.
- You will need to extract the information from the response according to the schema.
- If the response is not related to the schema, you should return an empty JSON.
- You will need to return the information in a structured JSON format.

# Considerations
The user is an older person and may not be able to type well. Please consider the following common response patterns:
- **Simple "yes" or "no" answers:** If the questions can be answered with a single "yes" or "no", interpret the response accordingly.
- **Never treat "no" as missing:** Do not interpret "no", "No", or "NO" (or other casing) as null/None/empty. These are valid answers and must be recorded. Map them to explicit negative/False values in the schema where applicable.
- **"Yes/No to everything":** If the user says "yes to all", "no to all", "all yes", "all no", or something similar, apply that answer to all questions that were asked.
- **Answers by question index:** The user might answer questions by number (e.g., "1. no, 2. yes, 3. no").
- **Vague or brief responses:** Do your best to infer the meaning of short or incomplete sentences.

# Schema
{SCHEMA}
"""


def update_state(callback_context: CallbackContext) -> None:
    """Update the state with the parsed information."""
    state = callback_context.state
    extracted_info = state.get(diagnostic_settings.extracted_information_field, {})
    if not extracted_info:
        return

    diagnostic_info = state.get(diagnostic_settings.diagnostic_field, {})
    if diagnostic_info:
        diagnostics_data = DiagnosticSchema.model_validate(diagnostic_info, strict=True)
        updated_diagnostics_data = diagnostics_data.update(extracted_info)
    else:
        updated_diagnostics_data = DiagnosticSchema.model_validate(
            extracted_info, strict=False
        )
    state_update = updated_diagnostics_data.model_dump(mode="json")

    state[diagnostic_settings.diagnostic_field] = state_update


parsing_agent = LlmAgent(
    name="parsing_agent",
    model=diagnostic_settings.model_name,
    description="Use this agent to parse the patient's response and extract relevant information.",
    instruction=PROMPT,
    output_schema=DiagnosticSchema,
    output_key=diagnostic_settings.extracted_information_field,
    after_agent_callback=[update_state, update_missing_information],
)
