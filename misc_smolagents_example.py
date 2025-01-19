#from huggingface_hub import login #see 'login' and model_id to use a HF api call. 
from smolagents import MultiStepAgent, HfApiModel
from typing import Optional
from smolagents import tool, LiteLLMModel
from smolagents.agents import ToolCallingAgent

#login("")
#MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

model = LiteLLMModel(
    model_id="ollama_chat/mistral"
    api_key="ollama"
#    api_base="http://localhost:1234/v1/" local server / or replace api_key with 
)

# First agent - formats the name
first_agent = MultiStepAgent(
    tools=[],
    model=HfApiModel(model_id=MODEL_ID),
    system_prompt="""You are a routing agent.
    Your job is to process the user input and pass it to the correct agent.
    {{managed_agents_descriptions}}
    {{authorized_imports}}""",
)

# Second agent - creates the greeting
second_agent = MultiStepAgent(
    tools=[],
    model=HfApiModel(model_id=MODEL_ID),
    system_prompt="""You are a tool agent.
    Your job is to create, run and debug.
    {{managed_agents_descriptions}}
    {{authorized_imports}}""",
)

# third agent - creates the dataset
third_agent = MultiStepAgent(
    tools=[],
    model=HfApiModel(model_id=MODEL_ID),
    system_prompt="""You are a synthetic data agent.
    Your job is to create fake outputs. Create a dataset of 50 or less based on the input provided.
    {{managed_agents_descriptions}}
    {{authorized_imports}}""",
)

def process_request(user_input):
    # Format the name
    formatted_name = first_agent.run(f"Format this name properly: {user_input}")

    # Create greeting
    greeting = second_agent.run(f"Create a hello world message for: {formatted_name}")

    return greeting


if __name__ == "__main__":
    user_input = input("What's your name? ")
    result = process_request(user_input)
    print("======= final result ======")
    print(result)
