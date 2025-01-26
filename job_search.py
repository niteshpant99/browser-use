from langchain_anthropic import ChatAnthropic
from browser_use import Agent, Browser
from pydantic import SecretStr
import asyncio
from browser_use.agent.views import AgentHistoryList

# Initialize the model
llm=ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            temperature=0.0,
            timeout=100, # Increase for complex tasks
)

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
        
    )
)

from browser_use.browser.context import BrowserContextConfig

# config = BrowserContextConfig(
#     cookies_file="path/to/cookies.json",
#     wait_for_network_idle_page_load_time=3.0,
#     browser_window_size={'width': 1280, 'height': 1100},
#     locale='en-US',
#     user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
#     highlight_elements=True,
#     viewport_expansion=500,
#     allowed_domains=['google.com', 'wikipedia.org'],
# )

# Create agent with the model
async def run_search() -> AgentHistoryList:
    agent = Agent(
        task="""
        Search on google.com for 'New York  site:https://jobs.ashbyhq.com/' 
        Then, click on tools and set the date to 'Past week'
        For each job listing that matches my profile, open the job on a new tab
        """,
        llm=ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            temperature=0.0,
            timeout=100,                 # Increase for complex tasks
            
        ),
        browser=browser,
        browser_context=context,
        use_vision=True,             # Enable vision capabilities
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)

    input('Press Enter to close the browser...')
    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())