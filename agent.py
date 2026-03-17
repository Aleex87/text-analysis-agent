from langchain.agents import create_agent

from config import settings
from memory import ConversationMemory
from prompts import get_system_prompt
from tools import split_text, search_keyword
from util.models import get_model


class TextAnalystAgent:
    def __init__(self) -> None:
        self.memory = ConversationMemory(settings.memory_window)

        self.model = get_model(
            temperature=settings.model_temperature,
            top_p=settings.model_top_p,
        )

        self.agent = create_agent(
            model=self.model,
            tools=[split_text, search_keyword],
            system_prompt=get_system_prompt(),
        )

    def set_text(self, text: str) -> None:
        self.memory.set_text(text)

    def chat(self, user_input: str) -> str:
        self.memory.add_user_message(user_input)

        source_text = self.memory.get_text() or ""
        messages = self.memory.get_messages()

        messages_with_context = [
            {
                "role": "user",
                "content": f"Here is the source text:\n{source_text}"
            }
        ] + messages

        response = self.agent.invoke({
            "messages": messages_with_context,
        })

        ai_text = response["messages"][-1].content

        if isinstance(ai_text, list):
            ai_text = "".join(
                part.get("text", "") if isinstance(part, dict) else str(part)
                for part in ai_text
            )

        ai_text = str(ai_text).strip()
        self.memory.add_ai_message(ai_text)

        return ai_text

    def reset(self) -> None:
        self.memory.clear()
        