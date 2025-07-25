from dotenv import load_dotenv
import os 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

agent = Agent(
    name = "Agent Assistant",
    instructions = "You are a helpfull assistant for students. Your works are Answer academic questions, provide study tips, summarize small text passages"
)

response = Runner.run_sync(
    agent,
    input = "Can i get information about HSC make me a summary of it",
    run_config = config
)

print(response)