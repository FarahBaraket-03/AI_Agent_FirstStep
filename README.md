# AI Projects Journey

A 4-day journey building different AI applications, from basic agents to RAG systems.

## 📂 Project Structure
```
.
├── day1/ # Basic AI Agent projects
│ ├── basic_ai_agent/ # Simple AI agent using Illama Gemma model
│ ├── agent_with_memory/ # AI agent with memory capabilities
│ └── web_ui_streamlit/ # Web interface for the agent using Streamlit
│
├── day2/ # Voice assistant project
│ └── ai_voice_assistant/ # Voice assistant using pyttsx3 and speech_recognition
│
├── day3/ # Web scraping with AI
│ └── ai_web_scrap/ # AI-powered web scraping
│
└── day4/ # Advanced RAG system
└── qabot/ # Retrieval-Augmented Generation with IBM Watsonx
```


## 📦 Dependencies & Technologies

### Day 1: Basic AI Agent
| Package | Purpose |
|---------|---------|
| `streamlit` | Web interface for the chatbot |
| `langchain-ollama` | Integration with Ollama's Gemma model |
| `langchain-core` | Core LangChain functionality |
| `langchain-community` | Chat message history storage |

### Day 2: AI Voice Assistant
| Package | Purpose |
|---------|---------|
| `pyttsx3` | Text-to-speech conversion |
| `speech_recognition` | Voice input processing |
| `pyaudio` | Audio input/output handling |
| `threading` | Background speech synthesis |

### Day 3: AI Web Scraper
| Package | Purpose |
|---------|---------|
| `requests` | Fetching web page content |
| `beautifulsoup4` | HTML parsing and text extraction |
| `faiss` | Vector similarity search |
| `numpy` | Numerical operations for embeddings |
| `langchain-huggingface` | Sentence embeddings |

### Day 4: Watsonx RAG System
| Package | Purpose |
|---------|---------|
| `ibm-watsonx-ai` | IBM's AI model inference |
| `langchain-ibm` | Watsonx integrations |
| `chromadb` | Vector database for documents |
| `gradio` | Web interface for PDF Q&A |
| `pypdf` | PDF text extraction |


## 🚀 Daily Projects

### Day 1: Basic AI Agents
- **basic_ai_agent**: Simple AI agent implementation using Illama Gemma model
- **agent_with_memory**: Enhanced version with memory capabilities
- **web_ui_streamlit**: Streamlit web interface for interacting with the agent

<img width="1000" height="700" alt="Capture d'écran 2025-08-10 152218" src="https://github.com/user-attachments/assets/0fc7497b-98c0-4b75-a4cb-bab046d0e12a" />


### Day 2: AI Voice Assistant
- Voice-controlled assistant using:
  - `pyttsx3` for text-to-speech
  - `speech_recognition` for speech-to-text
- Features:
  - Voice commands
  - Basic conversation capabilities

<img width="1000" height="700" alt="Capture d'écran 2025-08-10 183503" src="https://github.com/user-attachments/assets/6dec723e-9c80-4da5-86e3-b51ab76f39b3" />


### Day 3: AI Web Scraper
- Web scraping tool enhanced with AI capabilities
- Features:
  - Intelligent content extraction
  - Data processing and analysis

<img width="1000" height="700" alt="Capture d'écran 2025-08-10 204135" src="https://github.com/user-attachments/assets/872202a3-0514-4ef3-8e47-a1eb9f9b11c6" />


### Day 4: Watsonx RAG System
Advanced Retrieval-Augmented Generation system using IBM Watsonx:

```python
# Key components
from ibm_watsonx_ai.foundation_models import ModelInference
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from langchain_community.vectorstores import Chroma

# Features:
- PDF document processing
- Vector embeddings with IBM slate-125m model
- Question answering with Mistral-large LLM
- Gradio web interface
```
<img width="1000" height="562" alt="Capture d'écran 2025-08-08 113247" src="https://github.com/user-attachments/assets/d0a36af8-9f91-4d74-8af2-0cbd440d92af" />
