import streamlit as st
from PIL import Image
img=Image.open("Iris Plot.png")
st.header("Here is the visualization of the Iris dataset!")
st.image(img)