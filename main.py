from models import get_model
from agent.loop import AgentLoop

model = get_model()
agent = AgentLoop(model)

agent.start()

while True:
    query = input("User: ")

    if query == "/quit":
        break

    response = agent.run(query)

    print("Agent:", response.text)