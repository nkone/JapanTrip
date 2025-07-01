import streamlit as st

st.set_page_config(page_title="Day 1")
st.title("Day 1")
st.header("Morning", divider="grey")
st.header("Noon", divider="grey")
st.write("3:00 PM: Check in Park Hotel Ginza")
st.link_button("Hotel Address", "https://www.google.com/maps/place/Park+Hotel+Tokyo/@35.6630586,139.7568766,17z/data=!3m1!5s0x60188bc25045dc55:0xa4de8ac467ac6350!4m10!3m9!1s0x60188bc250f3b1a9:0x292e5bc02d390d7!5m3!1s2025-07-16!4m1!1i2!8m2!3d35.6630543!4d139.7594515!16s%2Fg%2F122jr5yb?entry=ttu&g_ep=EgoyMDI1MDYyOS4wIKXMDSoASAFQAw%3D%3D")
st.header("Evening", divider="grey")
st.badge("Note: Sleep early for early departure tomorrow", icon=":material/exclamation:", color="red")