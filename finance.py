from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from pathlib import Path
from dotenv import load_dotenv
from agno.models.groq import Groq
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

agent = Agent(
    model=Groq(id="openai/gpt-oss-20b"),
    tools=[YFinanceTools(all=True)],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    debug_mode=True)

agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)