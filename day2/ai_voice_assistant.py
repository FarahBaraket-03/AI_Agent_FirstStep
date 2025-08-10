import speech_recognition as sr 
import pyttsx3
import pyaudio
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import time

llm= OllamaLLM(model="gemma:2b")

#intialize Memory
chat_history = ChatMessageHistory()


#intialize text-to-speech engine

engine = pyttsx3.init()
engine.setProperty('rate',160)  #adjsut speaking speed

#Speech Recognition

recongnizer= sr.Recognizer()

#Function to Speak

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)
    
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


# AI chat Prompt
prompt = PromptTemplate(
    input_variables=["chat_history","question"],
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


#main loop

speak("Hello.I'am Your AI assistant.How can I help you today")

while True:
    query=listen()
    if "exit" in query or "stop" in query :
        speak('Goodbye ! Have a great day.')
        break
    if query :
        response=run_chain(query)
        print(f"\n AI Response : {response}")
        speak(response)