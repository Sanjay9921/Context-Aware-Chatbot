import requests
from config.settings import TOGETHER_API_URL, TOGETHER_API_KEY

def get_prompt(context, question):
    prompt = f"""You are an assistant. Use the context below to answer the question:

Context:
{context}

Question:
{question}

Answer:"""
    return prompt

def generate_answer(context, question, model):
    
    _url = TOGETHER_API_URL
    _headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type":"application/json"
    }

    prompt = get_prompt(context, question)

    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.5,
        "top_p": 0.9,
    }

    # Sending the POST request to the API
    response = requests.post(
        _url,
        headers=_headers,
        json=payload
    )

    # print("Status:", response.status_code)

    # Log the response text to understand its structure
    # print("Response Text:", response.text)

    if response.status_code != 200:
        if response.status_code == 401:
            return "Unauthorized: Check your API Key"
        elif response.status_code == 403:
            return "Forbidden: The API Key may not have sufficient permissions."
        else:
            return "Response failed. Details:", response.text
    
    try:
        result = response.json()
        # return f"Full API Response: {result}" # to debug the json output
        return result["output"]['choices'][0]['text'].strip()
        # return result[0]["answer"]
    except Exception as e:
        return f"Request failed: {str(e)}"