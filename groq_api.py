from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="mistral-saba-24b")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)


# import requests
# import os

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Set in environment or manually

# def query_groq(prompt):
#     url = "https://api.groq.com/openai/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": "llama3-70b-8192",  # Fast + high quality
#         "messages": [{"role": "user", "content": prompt}],
#         "temperature": 0.3
#     }

#     response = requests.post(url, json=data, headers=headers)
#     result = response.json()
#     return result["choices"][0]["message"]["content"]
