# pip install -qU "langchain[anthropic]" to call the model

from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model= ChatGoogleGenerativeAI(
        model= "gemini-2.5-flash",
        temperature=1.0,
        max_retries=2,
        google_api_key=api_key
    ),
    tools=[get_weather],
    prompt="You are a helpful assistant"
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
print(response)