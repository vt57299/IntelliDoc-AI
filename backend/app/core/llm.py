import requests
from app.config import settings


GROQ_API_KEY = settings.GROQ_API_KEY

def ask_llm(question: str, context: str) -> str:
    prompt = f"""
You are a research assistant. Given the following context from multiple documents, answer the user accurately with references.

Context:
{context}

Question:
{question}

Answer:
"""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if 'error' in data:
            error = data['error']
            if 'message' in error:
                raise Exception(f"API Error: {error['message']}")
            else:
                raise Exception("Unknown API error occured.")
            
        return data['choices'][0]['message']['content']
    
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return "Network error occured. Please try again later."
    
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return f"An error occured: {e}"


# def extract_themes(context: str) -> str:
#     prompt = f"""
# You are a professional analyst. The following excerpts come from many documents.

# Your task:
# 1. Analyze the context and extract key recurring **themes** (e.g., Regulatory Compliance, Legal Penalties, Financial Risk).
# 2. Group relevant documents under each theme (use doc_id from the references).
# 3. Be concise and structured. Keep themes distinct.

# Context:
# {context}

# Output Format:
# Theme 1 - [Title]:
# Summary of the theme...
# Documents: [doc1, doc2, doc3]

# Theme 2 - [Title]:
# Summary of the theme...
# Documents: [doc4, doc7]
# """
    
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": "mistral-7b-8k",
#         "messages": [
#             {"role":"user", "content": prompt}
#         ]
#     }

#     try:
#         response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
#         response.raise_for_status()
#         data = response.json()

#         if "error" in data:
#             error = data["error"]
#             if "message" in error:
#                 raise Exception(f"API Error: {error['message']}")
#             else:
#                 raise Exception("Unknown API error occurred.")

#         return data['choices'][0]['message']['content']

#     except requests.exceptions.RequestException as e:
#         print(f"Network Error: {e}")
#         return "Network error occurred. Please try again later."

#     except Exception as e:
#         print(f"Unexpected Error: {e}")
#         return f"An error occurred: {e}"




from google import genai
from google.genai import types

GEMINI_API_KEY = settings.GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def extract_themes(context: str) -> str:
    prompt = f"""
You are an AI assistant analyzing excerpts from multiple documents.

Your task:
1. Extract key recurring themes across the text.
2. Summarize each theme clearly.
3. List which document IDs contributed to each theme.

Context:
{context}

Format:
Theme 1 – [Title]:
Summary of the theme...
Documents: [doc1, doc3, doc7]

Theme 2 – [Title]:
Summary of the theme...
Documents: [doc2, doc5]
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text





# # google's model

# from google import genai
# from app.config import settings


# GOOGLE_API_KEY = settings.GOOGLE_API_KEY
# client = genai.Client(api_key=GOOGLE_API_KEY)

# def ask_llm(question: str, context: str) -> str:
#     prompt = f"""
# You are a research assistant. Given the following context from multiple documents, answer the user accurately with references.

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
#     try:
#         response = client.models.generate_content(
#             model = "gemini-2.0-flash",
#             messages=[{"role": "user", "content": prompt}])
#         if response and response.messages:
#             return response.messages[-1]['content']
#         else:
#             return "No response received from the model."
    
#     except Exception as e:
#         print(f"Error: {e}")
#         return f"An error occurred: {e}"


# def extract_themes(context: str) -> str:
#     prompt = f"""
# You are a professional analyst. The following excerpts come from many documents.

# Your task:
# 1. Analyze the context and extract key recurring **themes** (e.g., Regulatory Compliance, Legal Penalties, Financial Risk).
# 2. Group relevant documents under each theme (use doc_id from the references).
# 3. Be concise and structured. Keep themes distinct.

# Context:
# {context}

# Output Format:
# Theme 1 - [Title]:
# Summary of the theme...
# Documents: [doc1, doc2, doc3]

# Theme 2 - [Title]:
# Summary of the theme...
# Documents: [doc4, doc7]
# """
#     try:
#         response = palm.chat(messages=[{"role": "user", "content": prompt}])
#         if response and response.messages:
#             return response.messages[-1]['content']
#         else:
#             return "No response received from the model."
    
#     except Exception as e:
#         print(f"Error: {e}")
#         return f"An error occurred: {e}"
