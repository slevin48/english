import os
import streamlit as st
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

st.title('English teacher')

st.write('🎥 Learn with movie quotes 🎬')

URL = "https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movie_Quotes"

r = rq.get(URL)
html = r.text

soup = BeautifulSoup(html, 'html.parser')

# st.write(soup.prettify())
# https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
# https://stackoverflow.com/questions/15724034/how-to-convert-wikipedia-wikitable-to-python-pandas-dataframe
table = soup.find("table", attrs={"class":"wikitable"})
tbody = table.find('tbody')
rows = tbody.find_all('tr')

# First row contains header
header = [i.text.replace("\n","") for i in rows[0].find_all('th')]

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# st.write(data)
df = pd.DataFrame(data,columns=header)
# st.table(df)

st.markdown("Source: [AFI's 100 Years...100 Movie Quotes - wikipedia](https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movie_Quotes)")


# https://discuss.streamlit.io/t/data-frame-question-in-selectbox/1916/3
values = df['Quotation'].tolist()
options = df.index.tolist()
dic = dict(zip(options, values))

id = st.selectbox("Movie Quote",options,format_func=lambda x: dic[x])
# st.write(type(id))
l = os.listdir("downloads/video_"+str(id))
# st.write(l)
video_file = open("downloads/video_"+str(id)+"/"+l[0], 'rb')
video_bytes = video_file.read()
st.video(video_bytes,'video/3gpp')