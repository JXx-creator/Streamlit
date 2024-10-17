import os
import streamlit as st 
from openai import OpenAI
import PIL.Image
import google.generativeai as genai

client = OpenAI(api_key = os.environ['OPENAI_API_KEY'])
#set the API KEY
genai.configure(api_key = userdata.get('GEMINI_API_KEY'))

#Text model
model = genai.GenerativeModel('gemini-1.5-flash')

# Upload the image file
uploaded = files.upload()

# Open the uploaded image file
image_path = next(iter(uploaded))  # Get the file name
image = Image.open(image_path)
image.show()  # Display the image in Colab

def design_gen(prompt):
  system_prompt = """
  You are a IT device identifier.
  Identify and describe the product in the images uploaded.
  Your objective is to identify the product in the image and describe the details information about the specific brand and model to assist users—especially those lacking technical knowledge—in.
  Would be better to know the specfic brand and model.
  """

  response =client.chat.completions.create(
      model="gemini-1.5-flash",
      messages=[
          {"role": "system","content":system_prompt},
          {"role": "user", "content": prompt}
      ],
  )
  return response.choices[0].message.content

image = PIL.Image.open('/content/earphone (1).jpg')

print(design_gen(image_path))

import PIL.Image #gemini API cannot connect to Internet, use an library to access the image
#why dall-e can direct open the image(no need the PILLOW library) because dall-e can read the binary(rb) file

image = PIL.Image.open('/content/mouse2.jpg')

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(['Identify and describe the product in the images uploaded.Would be better to know the specfic brand and model', image])
print(response.text)






