import pytube  
from pytube import YouTube  
video_url = 'https://www.youtube.com/watch?v=nfNc0XJdZWk'   
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first()  
video.download('F:/')   
