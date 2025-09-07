from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# will pick up env variable key
client = OpenAI()

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

    response = client.responses.create(
        model="gpt-4o",
        input=prompt
    )
    
    return response.output_text


def main():
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print(x_post)


if __name__ == "__main__":
    main()
