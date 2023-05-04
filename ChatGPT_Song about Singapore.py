# Hello ChatGPT
# Please create a song about Singapore's national day
# A catchy one that rhymes that everybody will love

import openai
from keys import API_Key
openai.api_key  = (API_Key)


completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages =[{"role":"user", "content": "Write a short song about Singapore. Praise its landmarks. Couplets should rhyme. It should contain a one verse and one chorus."}])
print(completion.choices[0].message.content)
