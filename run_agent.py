from relevanceai.resources.agent import Agent
from relevanceai import RelevanceAI

# Initialize the RelevanceAI client with the provided credentials
client = RelevanceAI(
    api_key="sk-Y2UzN2VkZDgtODUxNC00ZGMwLTllYjEtMDAzM2IzNTJkZTQ1",
    region="bcbe5a",
    project="061def26daa5-43d2-b3f6-307e4286c9ef"
)

# Replace 'your_agent_id' with the ID of the agent you want to use or create
AGENT_ID = "061def26daa5-43d2-b3f6-307e4286c9ef"

# Add error handling to capture potential issues with the API call
try:
    # List all agents in the project to verify the agent ID
    agents = client.agents.list_agents()
    print("Available Agents:")
    for agent in agents:
        print(f"Agent ID: {agent.agent_id}, Name: {agent.metadata.name}")

    # Check if the specified agent ID exists
    specified_agent_id = "061def26daa5-43d2-b3f6-307e4286c9ef"
    if not any(agent.agent_id == specified_agent_id for agent in agents):
        print(f"Error: Agent with ID {specified_agent_id} does not exist.")
    else:
        print(f"Agent with ID {specified_agent_id} exists.")
except Exception as e:
    print(f"An error occurred while listing agents: {e}")

# Update metadata for initializing the Agent
metadata = {
    "_id": AGENT_ID,
    "project": "061def26daa5-43d2-b3f6-307e4286c9ef",
    "agent_id": AGENT_ID,
    "name": "My Custom Agent",  # Example name, you can customize it
}

# Initialize the Agent with metadata
agent = Agent(client=client, **metadata)

# Example: List tools associated with the agent
tools = agent.list_tools()
print("Tools:", tools)

# Example: Trigger a task
message = "Hello, Agent!"
response = agent.trigger_task(message=message)
print("Triggered Task Response:", response)