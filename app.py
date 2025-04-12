import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

st.title("🖼️ Text To Image Generation using Stable Diffusion ")

prompt = st.text_input("Enter a prompt:", "A cat reading a book")

if st.button("Generate"):
    with st.spinner("Contacting remote generator..."):
        res = requests.post("https://99b2-104-199-141-166.ngrok-free.app/generate", json={"prompt": prompt})
        img_base64 = res.json()["image"]
        img_data = base64.b64decode(img_base64)
        img = Image.open(BytesIO(img_data))
        st.image(img, caption="Generated via Colab GPU", use_column_width=True)
