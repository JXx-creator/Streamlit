import os
import streamlit as st
from openai import OpenAI

#from google.colab import userdata
#from IPython.display import Image

client = OpenAI(api_key =
#os.environ['OPENAI_API_KEY'])
st.secrets['OPENAI_API_KEY'])

#Story
def story_gen(prompt):
  system_prompt = """
You are a world renowned author for young adults fiction short stories.
Given a concept, generate a short story in the style of that concept.
The total length of the story should be within around 100 word
  """

  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role':'system', 'content':system_prompt} ,
          {'role':'user', 'content':prompt}
      ],
      temperature = 1.3,
      max_tokens = 2000

  )
  return response.choices[0].message.content



prompt = "A dog's journey across the ocean"
print(story_gen(prompt))

#cover art
def art_gen(prompt):
  response = client.images.generate(
      model = 'dall-e-2',
      prompt = prompt,
       size = '1024x1024',
      n =1
  )
  return response.data[0].url

#Cover prompt design
def design_gen(prompt):
  system_prompt = """
You will be given a short story. Generate a prompt for a cover art that is suitable for the story.
The prompt is for dall-e-2.
  """
  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages =[
          {'role':'system', 'content':system_prompt} ,
          {'role':'user', 'content':prompt}
      ],
       temperature = 1.3,
      max_tokens = 2000
  )
  return response.choices[0].message.content
  
#UI
prompt = st.text_input("Enter a prompt")
if st.button("Generate"):
 story = story_gen(prompt)
 design = design_gen(story)
 art = art_gen(design)

 st.caption(design)
 st.divider()
 st.write(story)
 st.divider()
 st.image(art)