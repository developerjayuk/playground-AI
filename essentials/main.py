import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(topic: str) -> str:
    prompt = f"""
        You are a expert social media manager, and you excel at creating viral and highly engaging posts for X (twitter).
        
        Your task is to generate a post that is well written, concise with impact and tailored to the topic provided byt the user.
        
        Avoid using hashtags and lots of emojis (although a few emojis are ok if needed).
    
        Keep the post short and focused, and straight to the point.
        
        Use line breaks and empty lines to enhance readability.
        
        Here's the topic provided by the user for which you need to generate a post:
        <topic>
        {topic}
        </topic>
    """
    
    payload = {
        "model": "gpt-4o",
        "input": prompt
    }
    response = requests.post(
        "https://api.openai.com/v1/responses", 
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    )
    
    print(f"response: {response.json()}")
    
    response_text = response.json().get("output", [{}])[0].get("content", [{}])[0].get("text", "")
    
    print(f"response_text: {response_text}")
        
    return response_text


def main():
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print(x_post)


if __name__ == "__main__":
    main()
