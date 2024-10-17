import google.generativeai as genai
from google.colab import userdata
import PIL.Image
#gemini API cannot connect to Internet, use an library to access the image

#set the API KEY
genai.configure(api_key = userdata.get('GEMINI_API_KEY'))

#Text model
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content('Who are Donald Trump?')

#model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Write a story about a magic backpack.")
print(response)
print(response.text)

image=PIL.Image.open('/content/mouse2.jpg')

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(['Identify and describe the product in the images uploaded.'
  'Would be better to know the specfic brand and model.', image])
print(response.text) 