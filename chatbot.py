from dotenv import load_dotenv
import os

load_dotenv()

print("Key Loaded:", os.getenv("MISTRAL_API_KEY") is not None)

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model="mistral-small-2603")
# to store history
print("choose your ai mode")
print("press 1 for angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")
choice=int(input("tell your response:-"))
if choice ==1:
  mode="you are an angry ai agent. you resposed aggressiovely and impatiently." 
elif choice==2:
  mode="you are an funny ai agent.you responsed with humor and jokes."
elif choice==3:
  mode ="you are sad ai agent."

message=[
  SystemMessage(content=mode)
]

print("----welcome to my chatbot that exit with press 0-------")
while True:

 prompt=input("you:")
 message.append(HumanMessage(content=prompt))
 if prompt=="0":
    break

 response=model.invoke(message)
 message.append(AIMessage(content=response.content))
 print("bot:",response.content)
print(message)
# connect to app.py