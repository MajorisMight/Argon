from models.gemini import GeminiModel
from agent.loop import AgentLoop

model = GeminiModel()
agent = AgentLoop(model)

agent.start()

while True:
    query = input("User: ")

    if query == "/quit":
        break

    response = agent.run(query)

    print("Gemini:", response.text)