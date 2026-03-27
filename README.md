# LinkedIn-Post-Generator

This tool will analyze posts of a LinkedIn influencer and help them create the new posts based on the writing style in their old posts

<img width="1293" height="942" alt="image" src="https://github.com/user-attachments/assets/505b53ac-18db-4d22-b3ac-de1e1167bac5" />


Let's say you are a LinkedIn influencer and you need help in writing yout future posts. so, you can feed your past LinkedIn posts to this tool and it will extract key topics. Then you can select the topic, length, language etc. and use Generate button to create a new post that will match your own writing style.


## Technical Architecture
<img width="1200" height="824" alt="ChatGPT Image Mar 27, 2026, 11_57_33 AM" src="https://github.com/user-attachments/assets/577f17b6-0145-4186-a4e9-1c7e696c2902" />


- **Stage 1:**  
  Collect LinkedIn posts and extract:
  - Topic  
  - Language  
  - Length  

- **Stage 2:**  
  Use the selected topic, language, and length to generate a new post.  
  - Relevant past posts are retrieved  
  - These are used as **few-shot examples**  
  - This helps the LLM understand writing style and tone  
