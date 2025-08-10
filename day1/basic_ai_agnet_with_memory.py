
#^ ----------Second  Attempt----------------   

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm= OllamaLLM(model="gemma:2b")

#intialize Memory
chat_history = ChatMessageHistory()

#define ai chat prompt
prompt = PromptTemplate(
    input_variables=["question", "chat_history"],
   template=(
        "You are a helpful AI assistant. Previous conversation:\n{chat_history}\n"
        "User: {question}\n"
        "Please provide a clear and concise answer without repeating previous responses.\nAI:"
    )
)

def run_chain(question):
    #retrieve chat history
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
    #run the ai response
    response = llm.invoke(prompt.format(question=question, chat_history=chat_history_text))
    
    #store new user input and ai response in memory
    chat_history.add_user_message(question) 
    chat_history.add_ai_message(response)
    
    return response


#interactive cli chatbot
print("🤖 Welcome to your AI agent! Ask me anything. Type 'exit' to quit.")
while True:
    question = input("🧑 You : ")
    if question.lower() == 'exit':
        print("Exiting the AI agent. Goodbye!")
        break
    response = run_chain(question)
    print(f"🤖 AI Response: {response}")