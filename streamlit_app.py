import streamlit as st
import requests

# page config
st.set_page_config(
    page_title = "sentimaent Analysis",
    page_icon="🎬",
    layout = "centered"
)

st.title("🎬 Movie Review Sentiment Analyzer")
st.write("Enter a movie review and get a instant sentiment prediction!")

review =st.text_area("Enter your movie review here: ",height= 150)

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            # call your Flask backend
            response = requests.post(
                "https://sentiment-analysis-1-fbqy.onrender.com/predict",
                json = {"reviews":review}
            )
            result = response.json()

        sentiment = result['prediction']

        if "pos" in sentiment or "neg" in sentiment:
            st.success(f"sentiment : {sentiment}")
        else:
            st.error(f"Sentiment : {sentiment}")

