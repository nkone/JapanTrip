import streamlit as st


st.set_page_config(page_title="Day 2", page_icon="🦈")
st.title("Day 2")
st.header("Morning", divider="grey")
st.header("Noon", divider="grey")

st.write("12:00 PM: Head out for lunch")

with st.expander("See lunch options", width=200):
    lunch1, lunch2 = st.tabs(["Curry", "Sushi"])
    with lunch1:
        st.subheader("Coco Ichibanya")
        st.markdown("![Curry](https://ichibanyausa.com/cdn/shop/files/Q9A8784.jpg?v=1712705336&width=3840)")
    with lunch2:
        st.subheader("Kura Sushi Global Flagship Store Asakusa")
        st.markdown("![Sushi](https://lh3.googleusercontent.com/p/AF1QipPtLF1O6gRyaBWrb_9Gk25ezL4bt-ugAKuMppFd=w408-h272-k-no)")


st.write("3:00 PM: Check in Park Hotel Ginza")
st.link_button("Hotel Address", "https://www.google.com/maps/place/Park+Hotel+Tokyo/@35.6630586,139.7568766,17z/data=!3m1!5s0x60188bc25045dc55:0xa4de8ac467ac6350!4m10!3m9!1s0x60188bc250f3b1a9:0x292e5bc02d390d7!5m3!1s2025-07-16!4m1!1i2!8m2!3d35.6630543!4d139.7594515!16s%2Fg%2F122jr5yb?entry=ttu&g_ep=EgoyMDI1MDYyOS4wIKXMDSoASAFQAw%3D%3D")
st.header("Evening", divider="grey")

with st.expander("See dinner options", width=200):
    dinner1, dinner2 = st.tabs(["Sukiyaki", "Ramen"])
    with dinner1:
        st.subheader("Senrena")
    with dinner2:
        st.subheader("Ramen")


st.badge("Note: Sleep early for early departure tomorrow", icon=":material/exclamation:", color="red")