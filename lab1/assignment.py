from openai import OpenAI

EXIT_COMMAND = "/exit"

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Required by SDK format; ignored by Ollama
)

def initialize_history():
    return [
        {
            "role": "system",
            "content": "You are an academic mentor. Respond in 2 sentences maximum."
        }
    ]

def send_prompt(history):
    response = client.chat.completions.create(
        model="qwen2.5:1.5b",
        temperature=0.2,
        messages=history
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    history = initialize_history()
    send_prompt(history)
    print("Welcome to the academic mentor chat. Type '/exit' to quit.")
    
    while True:
        user_input = input(">>>")
        if user_input.strip().lower() == EXIT_COMMAND:
            break
        history.append({
            "role": "user",
            "content": user_input
        })
        response = send_prompt(history)
        history.append({
            "role": "assistant",
            "content": response
        })
        print(f"Assistant: {response}")

