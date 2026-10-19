



# from langchain.agents import create_agent

# agent = create_agent(
#     model="gemma3:latest ",
#     tools=[],
#     system_prompt="you are a helpful AI email draft Agent!"
# )


# query = input("Enter Email draft idea: ")

# messages = [
#     {
#         "role":"user",
#         "content":query
#     }
# ]

# result = agent.invoke({"messages":messages})

# print(result["messages"][-1].text)





from langchain.agents import create_agent
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gemma3:latest"
)

agent = create_agent(
    model=model,
    tools=[],
    system_prompt="You are a helpful AI email draft agent. Write clear, professional emails based on the user's idea."
)

query = input("Enter Email draft idea: ")

messages = [
    {
        "role": "user",
        "content": query
    }
]

result = agent.invoke({"messages": messages})

print("\n--- Email Draft ---\n")
print(result["messages"][-1].content)
