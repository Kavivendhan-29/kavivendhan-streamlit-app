# app.py
import streamlit as st
import base64
import os

st.set_page_config(page_title="Kavivendhan App", layout="wide")

def add_bg_from_local(image_file):
    """Embed local image as CSS background via base64."""
    if not os.path.exists(image_file):
        return False
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
      background-image: url("data:image/jpg;base64,{encoded}");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}
    /* Optional: make header/footer transparent/small */
    header {{background: rgba(0,0,0,0);}}
    footer {{visibility: hidden;}}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    return True

# Path to image (put your image at assets/bg.jpg)
IMG_PATH = "bg.jpg"
ok = add_bg_from_local(IMG_PATH)
if not ok:
    st.warning("Background image not found at 'assets/bg.jpg'. Upload it or change IMG_PATH.")

# Page content
st.markdown(
    "<h1 style='text-align:center; color: white; text-shadow: 0 0 12px rgba(0,0,0,0.9);'>Hey!!! This is Kavivendhan</h1>",
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align:center; color:#ffd580;'>🤖 Dreamer | Explorer | Builder of AI & Data Stories</h3>", unsafe_allow_html=True)

# Add a two-column interactive section
col1, col2 = st.columns([1, 2])

with col1:
    st.image(IMG_PATH, caption="Background preview", use_column_width=True)
    if st.button("Inspire me ✨"):
        st.balloons()
        st.success("Keep going — your projects matter!")

with col2:
    st.subheader("Quick links & widgets")
    st.write("- Upload dataset, run EDA, and preview outputs.")
    file = st.file_uploader("Upload CSV (optional)", type=["csv"])
    if file:
        import pandas as pd
        df = pd.read_csv(file)
        st.write("Preview:")
        st.dataframe(df.head())
        st.write("Shape:", df.shape)
        if st.checkbox("Show descriptive stats"):
            st.write(df.describe())

# Footer / Quote
st.markdown("---")
st.info("“The best way to predict the future is to create it.” — Start building today.")
