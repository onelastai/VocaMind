from ollama import Client

def analyze_text(text):
    client = Client()
    prompt = f"Analyze this call transcript for sentiment, abuse, and key facts:\\n{text}"
    response = client.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
