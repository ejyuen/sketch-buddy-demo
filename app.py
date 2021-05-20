import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

import pandas as pd
import numpy as np
import tensorflow as tf
import cv2 
from header import *
from classifier import *
from response import *
from canvas_size import *

create_header()
width, height = get_canvas_size()

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
# bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color= bg_color,
    # background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    width = width,
    height=height,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Do something interesting with the image data and paths

if canvas_result.json_data:
  if canvas_result.json_data["objects"]:
    if canvas_result.image_data is not None:
      img = canvas_result.image_data
      classification, probability = get_image_classification(img)
      st.subheader("Classification: " + classification)
      get_app_response(classification, probability)
    st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))
  else:
    st.subheader("Draw Something!")   


# if canvas_result.image_data is not None:

#     img = canvas_result.image_data
#     classification, probability = get_image_classification(img)
#     st.subheader("Classification: " + classification)
#     get_app_response(classification, probability)

# else:
  

# if canvas_result.json_data is not None:
#     if canvas_result.json_data["objects"]:
#       st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))    