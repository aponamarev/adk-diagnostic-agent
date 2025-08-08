from collections.abc import AsyncGenerator
from typing import override

from google.adk.agents import BaseAgent, LlmAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events.event import Event

from core.default_messages import DiagnosticDefaultMessages
from core.settings import diagnostic_settings
from diagnostic_agent.utils.init_state import initialize_state


class DiagnosticManagerAgent(BaseAgent):
    """This agent is responsible for orchestrating the diagnostic process."""

    inquiry_agent: LlmAgent
    parsing_agent: LlmAgent
    initial_diagnosis_agent: LlmAgent

    def __init__(
        self,
        name: str,
        description: str,
        inquiry_agent: LlmAgent,
        parsing_agent: LlmAgent,
        initial_diagnosis_agent: LlmAgent,
    ):
        super().__init__(
            name=name,
            description=description,
            inquiry_agent=inquiry_agent,
            parsing_agent=parsing_agent,
            initial_diagnosis_agent=initial_diagnosis_agent,
            sub_agents=[inquiry_agent, parsing_agent, initial_diagnosis_agent],
            before_agent_callback=initialize_state,
        )

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        # Parse user response and update state
        async for event in self.parsing_agent.run_async(ctx):
            yield event

        # Check current missing-information status
        missing_info = ctx.session.state.get(
            diagnostic_settings.missing_information_field
        )

        if missing_info != DiagnosticDefaultMessages.ALL_INFORMATION_COLLECTED.value:
            async for event in self.inquiry_agent.run_async(ctx):
                yield event

        else:
            # If everything is already collected, proceed to diagnosis immediately.
            async for event in self.initial_diagnosis_agent.run_async(ctx):
                yield event
        return
