import streamlit as st

#Set the app title
st.title('My first streamlit app')

#streamlit run [file name].py

#Dsiplay text output
st.write('Welcome to my first streamlit app')

#Display a button
st.button("Reset", type="primary")#primary return to button,nothing happenning
if st.button("Say Hello"):
  st.write("Why hello there")
else:
  st.write("Goodbye")