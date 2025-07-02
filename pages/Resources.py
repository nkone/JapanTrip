import streamlit as st
from streamlit_card import card
import base64
from pages.utilities import *

# st.image("assets/chocola.png")
# with open("assets/chocola.webp", "rb") as f:
#     data = f.read()
#     encoded = base64.b64encode(data)
# data = "data:image/webp;base64," + encoded.decode("utf-8")

st.title("🌄 Scenic Cards: Hover & Click Demo")

col1, col2 = st.columns(2)

with col1:
    click1 = card(
        title="Sunset Over Hills",
        text="Click to explore more sunsets",
        # image="https://images.unsplash.com/photo-1501785888041-af3ef285b470?&w=800",
        image=get_local_img("assets/testcardbg.webp"),
        url=None
    )

with col2:
    click2 = card(
        title="Forest Morning Mist",
        text="Click to discover forest scenes",
        image="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?&w=800",
        url=None
    )
