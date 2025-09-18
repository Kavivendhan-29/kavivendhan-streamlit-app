# app.py
import streamlit as st
import random

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(page_title="Kavivendhan App", layout="centered")

# ------------------------------
# Title & Intro
# ------------------------------
st.title("Hey!! This is Kavivendhan V S")
st.write("🚀 I'm a dreamer, explorer, and someone who loves tech & anime. Always learning, always building cool stuff!")

# ------------------------------
# Button + Quotes
# ------------------------------
quotes = [
    "🌊 “Inherited Will, the swelling of the changing times, and the dreams of people — these are things that cannot be stopped.” — Gol D. Roger",
    "☠️ “When do you think people die? When they are shot with a bullet? No! ... It’s when they are forgotten!” — Dr. Hiluluk",
    "🔥 “I don’t want to conquer anything. I just think the guy with the most freedom in this whole ocean… is the Pirate King!” — Monkey D. Luffy",
    "⚔️ “I don’t care what the society says. I’ve never regretted doing anything. I will survive and do what I want to.” — Roronoa Zoro",
]

if st.button("Click me"):
    quote = random.choice(quotes)
    st.markdown(
        f"""
        <div style="background-color:yellow; padding:15px; border-radius:10px; font-size:16px;">
            {quote}
        </div>
        """,
        unsafe_allow_html=True
    )

