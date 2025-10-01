import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import asyncio
from agents import Agent, Runner, function_tool

@function_tool
async def fetch_weather(city: str) -> str:
    """Fetch the weather for a given city.
    
    Args:
        city: The name of the city to fetch the weather for.
    """
    # Simulate weather lookup
    city = city.lower()
    if city == "san francisco":
        return "The weather in San Francisco is foggy ⛅"
    elif city == "delhi":
        return "The weather in Karachi is hot 🔥"
    elif city == "london":
        return "The weather in London is rainy ☔"
    else:
        return f"The weather in {city.title()} is sunny ☀️"

agent = Agent(
    name="Assistant",
    instructions="Always call fetch_weather tool to answer ANY weather-related question. Do not make up weather information.",
    tools=[fetch_weather],
)

async def main():
    # Ask a question that should trigger the tool
    result = await Runner.run(
        agent,
        input="What is the weather in Karachi today?"
    )
    
    print("Agent response:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())