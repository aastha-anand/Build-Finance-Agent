import streamlit as st
from youtubeanalyser import build_youtube_agent 

st.set_page_config(
    page_title="YouTube Video Analyzer", 
    layout="centered"
)
st.title("YouTube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

video_url = st.text_input("Enter YouTube Video URL:", "")
button = st.button("Analyze Video")

print(video_url)
print(button)

if video_url and button:
    with st.spinner("Analyzing video..."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )
    st.markdown("### Analysis Result")
    st.markdown(response.content)
        