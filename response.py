import streamlit as st
import streamlit.components.v1 as components

def get_app_response(classification, probability):
  if classification == "Default": 
    st.write("Draw something!") 
  elif classification == "Circle": 
    st.write("This is object is a round Circle!") 
  elif classification == "Triangle": #FILL SECOND CLASS NAME HERE!
    st.write("This object triangle with 3 sides!")
  elif classification == "Square":
    st.write("This object is a Square with 4 sides!")
  else:
    st.write("Oops! Might be a typo in the class name")