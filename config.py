from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    agent_name: str = "Text Analyst Agent"
    model_temperature: float = 0.1
    model_top_p: float = 0.9
    memory_window: int = 10


settings = Settings()