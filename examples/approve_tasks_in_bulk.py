
"""
Approve tasks of an agent in bulk
"""

import time
from dotenv import load_dotenv
load_dotenv()

from relevanceai import RelevanceAI

client = RelevanceAI()

agent_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

message_list = [
    "Research the following company: RelevanceAI relevanceai.com",
    "Research the following company: Vividly govividly.com",
    "Research the following company: Airwallex airwallex.com",
    "Research the following company: Lark larksuite.com",
    "Research the following company: SafetyCulture safetyculture.com",
]

task_ids = [] 

my_agent = client.agents.retrieve_agent(agent_id=agent_id)

# triggers the tasks
for message in message_list: 
    task = my_agent.trigger_task(message)
    task_ids.append(task.conversation_id) # save the ids of the triggered tasks
    time.sleep(1)

tool_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# approving the tasks given a list of task_ids above 
for task_id in task_ids: 
    approved_task = my_agent.approve_task(task_id)

    # approve only a specific tool (optional) -> use the code below instead
    approved_task = my_agent.approve_task(task_id, tool_id=tool_id)







