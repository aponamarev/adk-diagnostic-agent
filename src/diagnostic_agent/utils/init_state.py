from google.adk.agents.callback_context import CallbackContext

from core.default_messages import DiagnosticDefaultMessages
from core.settings import diagnostic_settings
from registers.requirements import collect_missing_information


def update_missing_information(callback_context: CallbackContext) -> None:
    """Update the missing information tag in the callback context."""
    missing_information = collect_missing_information(callback_context.state)
    if missing_information:
        content = "The following information is missing: " + ", ".join(
            missing_information
        )
        callback_context.state[diagnostic_settings.missing_information_field] = content
    else:
        callback_context.state[diagnostic_settings.missing_information_field] = (
            DiagnosticDefaultMessages.ALL_INFORMATION_COLLECTED.value
        )


def initialize_state(callback_context: CallbackContext) -> None:
    """Lazy initialization of the diagnostic information fields."""
    if diagnostic_settings.diagnostic_field not in callback_context.state:
        callback_context.state[diagnostic_settings.diagnostic_field] = {}
    if diagnostic_settings.missing_information_field not in callback_context.state:
        update_missing_information(callback_context)
