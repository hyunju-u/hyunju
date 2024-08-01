import tkinter as tk
import openai

#여기다 API키 넣을것

def send_message(message_log):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        temperature=0.5,
    )
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    return response.choices[0].message.content

def on_send():
    user_input = user_input_entry.get()
    if user_input.lower() == "quit":
        chat_log_text.insert(tk.END, "You: " + user_input + "\n")
        chat_log_text.insert(tk.END, "Goodbye!\n")
        user_input_entry.delete(0, tk.END)
    else:
        chat_log_text.insert(tk.END, "You: " + user_input + "\n")
        message_log.append({"role": "user", "content": user_input})
        response = send_message(message_log)
        message_log.append({"role": "assistant", "content": response})
        chat_log_text.insert(tk.END, "Assistant: " + response + "\n")
        user_input_entry.delete(0, tk.END)

message_log = [{"role": "system", "content": "You are a helpful assistant."}]

root = tk.Tk()
root.title("Chatbot")

chat_log_text = tk.Text(root, width=50, height=20)
chat_log_text.pack()

user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack()

send_button = tk.Button(root, text="Send", command=on_send)
send_button.pack()

root.mainloop()
