from locale import DAY_1
import streamlit as st

# Page setups

information_pg = st.Page(
    page="pages/Information.py",
    title="Information"

)
home_pg = st.Page(
    page="pages/Home.py",
    title="Home"
)
day1_pg = st.Page(
    page="pages/itinerary/day_1.py",
    title="Day 1"
)

st.set_page_config(page_title="Japan 2026")
pg = st.navigation(
    {
        "Main": [home_pg, information_pg],
        "Iternary": [day1_pg]
    }
)
pg.run()