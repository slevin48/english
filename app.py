import streamlit as st
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

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
st.table(df)
