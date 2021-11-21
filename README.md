# English teacher web app
Practice english with movie quotes

## Retrieve movie quotes from Youtube

https://pytube.io/en/latest/user/quickstart.html

![bond](bond.png)

N°90: "A martini. Shaken, not stirred." Goldfinger

https://www.youtube.com/watch?v=UUI65HYqQw0

- Search
```python
from pytube import Search
s = Search(df.Quotation[89] + " " + df.Film[89])
yt89 = s.results[89]
yt89.watch_url
```
- Download from URL
```python
from pytube import YouTube
url = "https://www.youtube.com/watch?v=UUI65HYqQw0"
yt = YouTube(url)
video = yt.streams.first()
video.download('downloads/video_'+str(89))
```
