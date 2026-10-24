from pathlib import Path

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")


def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        markdown=True,
        instructions="You are a helpful and expert travel agent"
    )


agent = build_agent()
agent.print_response("Which place is best to visit in Europe during the summer for a family vacation?")

