#%%
import openai
import os 


#%%

openai.api_key = os.getenv('OAI_key')

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the football team that won more champions leagues"}
]

# Make the API request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Extract and print the response
output_text = response.choices[0].message['content']
print(output_text)





# %%
