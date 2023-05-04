

import openai
from keys import API_Key
openai.api_key  = (API_Key)
import gradio


messages = [{"role" : "system", "content" : " You are personal financial planner"}]

def fin_advice(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn = fin_advice, inputs = "text", outputs = "text", title = "Your personal financial planner")
demo.launch()