   
#!----------Fisrt Attempt----------------    

from langchain_ollama import OllamaLLM

#load AImodel from Ollama

llm= OllamaLLM(model="gemma:2b")

print("welcome to your AI agent ! ask me anything .")

while True:
    question=input("Your Question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        print("Exiting the AI agent. Goodbye!")
        break
    response = llm.invoke(question)
    print(f"AI Response: {response}")