import streamlit as st
from streamlit_card import card
from pages.utilities import *
from annotated_text import annotated_text

st.set_page_config(page_title="Day 2", page_icon="🦈")
st.title("Day 2")
st.header("Morning", divider="grey")
st.write("5:00 AM: Depart for Toyosu Fish Market")
with st.expander("See recommended route"):
    st.markdown('''
    - 10 mins walk to 浜離宮前 (Hamarikyu bus station) (600m)
    - 5:19 AM: Onboard :violet[Toei Bus 1 (市01) purple line] heading for Shijo-Mae Station (6 stops)
    - 3 mins walk to Daiwa Sushi (250m)
    ''')
st.write("5:40 AM: Arrive at Daiwa Sushi")
st.write("6:00 AM: Breakfast at Daiwa Sushi (Omakase + A la Carte)")
st.write("7:00 AM: Explore around the area + commerative photos")
st.write("8:00 AM: Go back to hotel")
with st.expander("See recommended route"):
    st.markdown('''
    - 5 mins walk to Shijo-Mae Station from Daiwa Sushi (300m)
    - 8:06 AM: Take :blue[Yurikamome (Local Shimbashi)] to Shiodome Station (27 mins)(12 stops)
    - 8:33 AM: Arrive at Park Hotel
    ''')
st.write("9:00 AM: Check out hotel and leave luggage at reception")
st.write("9:30: Free time till lunch (2h30m)")

annotated_text("Recommending nearby activities are", ("Akihabara", "30 mins"), ("Pokemon Cafe", "20 mins"))
col1, col2 = st.columns(2)
with col1:
    click1 = card(
        title="Akihabara",
        text="25 mins",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Akihabara_Night.jpg/1599px-Akihabara_Night.jpg?20160816142429",
        url=None
    )
with col2:
    click2 = card(
        title="Pokemon Cafe",
        text="22 mins",
        image="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/7a/6f/b0/pokemon-cafe.jpg?w=1400&h=800&s=1",
        url=None
    )

st.header("Noon", divider="grey")
st.write("12:00 PM: Meet at Bills Ginza")

st.header("Evening", divider="grey")

st.write("5:00 PM: Head back to hotel to pick up luggage then depart for Nagoya (2hrs+)")
with st.expander("See recommended route"):
    st.markdown('''
    - 2 min walk to Shiodome Station
    - 5:06 PM: Take :blue[Yurikamome line] and head for Shimbashi
    - 5 mins walk to :green[Yamanote Line] Local for Tokyo / Ueno(Counter Clockwise)
    - 5:13 PM: Head for Tokyo Station (Platform 5) (4 mins)
    - 5:17 PM: Arrive at Tokyo Station
    - 5 mins walk to :blue[Tokaido Shinkansen] Nozomi 55 Nozomi Hakata
    - 5:30 PM: Onboard the Shinkansen on Platform 18 (3 stops)
    - 7:09 PM: Arrive at Nagoya station
    - 11 mins walk to Hotel
    - 7:20 PM: Check in at Royal Park Canvas
    ''')

st.badge("Note: Sleep early for early departure tomorrow", icon=":material/exclamation:", color="red")