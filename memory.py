from typing import List, Dict, Optional


class ConversationMemory:
    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self._messages: List[Dict[str, str]] = []
        self.source_text: Optional[str] = None

    def set_text(self, text: str) -> None:
        self.source_text = text

    def get_text(self) -> Optional[str]:
        return self.source_text

    def add_user_message(self, content: str) -> None:
        self._messages.append({"role": "user", "content": content})
        self._trim()

    def add_ai_message(self, content: str) -> None:
        self._messages.append({"role": "assistant", "content": content})
        self._trim()

    def get_messages(self) -> List[Dict[str, str]]:
        return list(self._messages)

    def clear(self) -> None:
        self._messages.clear()
        self.source_text = None

    def _trim(self) -> None:
        if len(self._messages) > self.max_messages:
            self._messages = self._messages[-self.max_messages:]
            