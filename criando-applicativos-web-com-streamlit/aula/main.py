import streamlit as st
import pandas as pd 

st.set_page_config(
    layout="wide",
    page_title="Spotify Song"
)
# como definir o ttl desse cache
@st.cache_data
def load_data():
  dataframe = pd.read_csv("Spotify.csv")
  return dataframe

dataframe = load_data()
st.session_state["dataframe"]=dataframe


dataframe.set_index("Track", inplace=True)
artists = dataframe["Artist"].value_counts().index

artist = st.sidebar.selectbox("Artista", artists)
dataframe_filtered_by_artist = dataframe[dataframe["Artist"] == artist]

albuns = dataframe_filtered_by_artist["Album"].value_counts().index

album = st.sidebar.selectbox("Album", albuns)
dataframe_filtered_by_artist_and_album = dataframe_filtered_by_artist[dataframe_filtered_by_artist["Album"] == album]

display = st.sidebar.checkbox("Display chart")
if display:
  column_left, column_right = st.columns([0.7, 0.3])
  column_left.bar_chart(dataframe_filtered_by_artist_and_album["Stream"])
  column_right.line_chart(dataframe_filtered_by_artist_and_album["Danceability"])

dataframe_filtered_by_artist_and_album
