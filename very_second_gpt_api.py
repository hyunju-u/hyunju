
import openai
#여기다 API키 넣을것
def send_message(message_log):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        temperature=0.5,
    )
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    return response.choices[0].message.content
def main():
    message_log=[
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    while True:
        user_input=input("You:")
        if user_input.lower()=="quit":
            print("Goodbye!")
            break
        message_log.append({"role":"user", "content":user_input})
        response=send_message(message_log)
        message_log.append({"role":"assistant", "content":response})
        print(f"assistant:{response}")

if __name__=="__main__":
    main()
