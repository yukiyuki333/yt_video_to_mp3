import yt_dlp

class Fetch_video_and_turn_to_mp3():
    def __init__(self,videoURL,filename):
        self.filename = filename + ".mp3"
        self.videoURL=videoURL
    def downloadmp3(self):
        #檔案命名
        ydl_opts={
            'format':'bestaudio',
            'outtmpl':self.filename
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.videoURL])


if __name__=='__main__':
    videoURL=input("input video URL: ")
    videoName=input("input file name: ")
    x=Fetch_video_and_turn_to_mp3(videoURL,videoName)
    x.downloadmp3()