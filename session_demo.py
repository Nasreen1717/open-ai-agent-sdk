import os
from openai import OpenAI
from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession
import asyncio

load_dotenv()

async def main():
    agent = Agent(name="Assistant", instructions="Reply concisely.")

    session = SQLiteSession("conversation_pakistan", "conversation_history.db")

    # Famous landmark: Badshahi Mosque
    result1 = await Runner.run(agent, "In which city is the Badshahi Mosque located?", session=session)
    print(result1.final_output)

    result2 = await Runner.run(agent, "In which province is that city?", session=session)
    print(result2.final_output)

    result3 = await Runner.run(agent, "Which country is it in?", session=session)
    print(result3.final_output)

if __name__ == "__main__":
    asyncio.run(main())
