import os
import streamlit as st
import requests as rq
import pandas as pd
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from pytube import Search
from PIL import Image


# page_bg_img = '''
# <style>
#       .stApp {
#   background-image: url("https://payload.cargocollective.com/1/11/367710/13568488/MOVIECLASSICSerikweb_2500_800.jpg");
#   background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('English teacher')

st.write('🎥 Learn with movie quotes 🎬')

st.markdown("Source: [AFI's 100 Years...100 Movie Quotes - wikipedia](https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movie_Quotes)")


df = pd.read_csv("movie_quotes_list.csv",index_col="Unnamed: 0")
# st.table(df)

# https://discuss.streamlit.io/t/data-frame-question-in-selectbox/1916/3
values = df['Quotation'].tolist()
options = df.index.tolist()
dic = dict(zip(options, values))

id = st.selectbox("Movie Quote",options,format_func=lambda x: dic[x])

image = Image.open("posters/"+str(id+1))
st.sidebar.image(image, caption=dic[id])
st.dataframe(df.iloc[[id]].drop("Quotation", axis=1))

## Try Speech to Text
# stt_button = Button(label="Repeat Quote", width=100)

# stt_button.js_on_event("button_click", CustomJS(code="""
#     var recognition = new webkitSpeechRecognition();
#     recognition.continuous = true;
#     recognition.interimResults = true;
 
#     recognition.onresult = function (e) {
#         var value = "";
#         for (var i = e.resultIndex; i < e.results.length; ++i) {
#             if (e.results[i].isFinal) {
#                 value += e.results[i][0].transcript;
#             }
#         }
#         if ( value != "") {
#             document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
#         }
#     }
#     recognition.start();
#     """))

# result = streamlit_bokeh_events(
#     stt_button,
#     events="GET_TEXT",
#     key="listen",
#     refresh_on_update=False,
#     override_height=75,
#     debounce_time=0)

# if result:
#     if "GET_TEXT" in result:
#         st.write(result.get("GET_TEXT"))


## Watch Quote

try:
    os.mkdir("downloads")
except OSError as error:
    print(error)

b = st.button("Watch Extract")
if b:
    s = Search(df.Quotation[id] + " " + df.Film[id])
    yt = s.results[0]
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
    video.download('downloads/video_'+str(id))
        
    l = os.listdir("downloads/video_"+str(id))
    video_file = open("downloads/video_"+str(id)+"/"+l[0], 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes,'video/mp4')