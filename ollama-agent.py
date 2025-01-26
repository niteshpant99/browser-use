from langchain_ollama import ChatOllama
from browser_use import Agent
from pydantic import SecretStr
import asyncio
from browser_use.agent.views import AgentHistoryList



# Initialize the model
llm=ChatOllama(model="qwen2.5", num_ctx=32000)

# Create agent with the model
# agent = Agent(
#     task="Your task here",
#     llm=llm
# )

# import os

# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

async def run_search() -> AgentHistoryList:
    agent = Agent(
        task="""
        Search on google.com for 'New York  site:https://jobs.ashbyhq.com/' 
        Then, click on tools and set the date to 'Past week'
        For each job listing that matches my profile, open the job on a new tab
        """,
        llm=ChatOllama(
            model="qwen2.5:32b-instruct-q4_K_M",
            num_ctx=32000,
        ),
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())