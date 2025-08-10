import streamlit as st 

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


llm= OllamaLLM(model="gemma:2b")

# Initialize Memory

if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()
    

#define ai chat prompt
prompt = PromptTemplate(
    input_variables=["question", "chat_history"],
   template=(
        "You are a helpful AI assistant. Previous conversation:\n{chat_history}\n"
        "User: {question}\n"
        "Please provide a clear and concise answer without repeating previous responses.\nAI:"
    )
)

# Streamlit app for interactive chatbot

def run_chain(question):
    #retrieve chat history
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])
    
    #run the ai response
    response = llm.invoke(prompt.format(question=question, chat_history=chat_history_text))
    
    #store new user input and ai response in memory
    st.session_state.chat_history.add_user_message(question) 
    st.session_state.chat_history.add_ai_message(response)
    
    return response


#Streamlit UI
st.title("🤖 AI Agent with Memory")
st.write("Ask me anything !")

user_input = st.text_input("🧑 Your question : ")

if user_input :
    response = run_chain(user_input)
    st.write(f"**YOU** {user_input}")
    st.write(f"**AI** {response}")
    
#show full chat history
st.subheader("Chat History")
for msg in st.session_state.chat_history.messages :
    st.write(f"**{msg.type.capitalize()}** : {msg.content}")