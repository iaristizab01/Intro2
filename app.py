import streamlit as st
from PIL import Image 

st.title("Mi primera App!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente piuedo desarrollar backend y frontend.")
image=Image.open("Hello-Kitty.jpg")

st.image(image, caption='Interfaces multimodales')
