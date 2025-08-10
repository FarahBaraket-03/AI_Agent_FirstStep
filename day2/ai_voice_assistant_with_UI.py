import streamlit as st 

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import speech_recognition as sr 
import pyttsx3
import pyaudio

import threading
 

llm= OllamaLLM(model="gemma:2b")


#intialize text-to-speech engine

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 180)  # Adjust speaking speed
  #adjsut speaking speed

#Speech Recognition

recongnizer= sr.Recognizer()

#Function to Speak

def speak(text):
    def _speak():
        engine.say(text)
        engine.runAndWait()  

    threading.Thread(target=_speak).start()



#Function to Listen

def listen():
    with sr.Microphone() as source :
        print('\n Listening ....')
        recongnizer.adjust_for_ambient_noise(source)
        audio = recongnizer.listen(source)
    try :
        query=recongnizer.recognize_google(audio)
        print(f"You said : {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry couldn't understand . Try again !")
        return ''
    except sr.RequestError:
        print("Speech recognition Service Unavaible")
        return ""




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




def run_chain(question):
    #retrieve chat history
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])
    
    #run the ai response
    response = llm.invoke(prompt.format(question=question, chat_history=chat_history_text))
    
    #store new user input and ai response in memory
    st.session_state.chat_history.add_user_message(question) 
    st.session_state.chat_history.add_ai_message(response)
    
    return response


# Streamlit Web UI
st.title("🤖 AI Voice Assistant (Web UI)")
st.write("🎙️ Click the button below to speak to your AI assistant!")

# Button to Record Voice Input
if st.button("🎤 Start Listening"):
    user_query = listen()
    if user_query:
        ai_response = run_chain(user_query)
        st.write(f"**You:** {user_query}")
        st.write(f"**AI:** {ai_response}")
        speak(ai_response)  # AI speaks the response

# Display Full Chat History
st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")



