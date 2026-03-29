# 🚀 LinkedIn Post Generator
Live on - https://genai-linkedpostgenerator.streamlit.app/
This tool will analyze posts of a LinkedIn influencer and help them create the new posts based on the writing style in their old posts ✍️

<p align="center">
  <img src ="https://github.com/user-attachments/assets/812045bd-79db-4f0f-a6e1-01a7eb0e354e" width="700"/>
</p>

Let's say you are a LinkedIn influencer 🤵‍💼 and you need help in writing yout future posts. so, you can feed your past LinkedIn posts to this tool and it will extract key topics. Then you can select the topic, length, language etc. and use Generate button to create a new post that will match your own writing style ⚡


## 🏗️ Technical Architecture
<p align="center">
  <img src="https://github.com/user-attachments/assets/577f17b6-0145-4186-a4e9-1c7e696c2902" width="650"/>
</p>

- **Stage 1:** 📊  
  Collect LinkedIn posts and extract:
  - 🏷️ Topic  
  - 🌐 Language  
  - 📏 Length  

- **Stage 2:** 🤖  
  Use the selected topic, language, and length to generate a new post.  
  - Relevant past posts are retrieved  
  - These are used as **few-shot examples**  
  - This helps the LLM understand writing style and tone ✨
 
## 🛠️ Tools Used

- 🧠 Llama 4 → Content generation and pre-processing  
- 🔗 LangChain → Workflow & prompt handling  
- 🖥️ Streamlit → User interface  
 

## ⚙️ Setup
- 🔑 Get API key from https://console.groq.com/keys  
- 📁 Add it to `.env`:
  - GROQ_API_KEY=your_api_key_here  

- 📦 Install dependencies:
  - pip install -r requirements.txt  

- ▶️ Run app:
  - streamlit run main.py  
