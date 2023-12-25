import google.generativeai as genai

# SECRET KEY
genai.configure(api_key='SECRET_KEY')

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?", stream=True)

for chunk in response:
  print(chunk.text)  
  
 