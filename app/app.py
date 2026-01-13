import streamlit as st
from pipeline.pipeline import AnimeRecomendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender",layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecomendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender")

query = st.text_input("Enter your anime preference eg : light hearted anime with school set")

if query:
    with st.spinner("Fetching Recommendation for you...."):
        response = pipeline.recommend(query)
        st.markdown("### recommedndations")
        st.write(response)