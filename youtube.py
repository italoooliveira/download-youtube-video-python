from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been a eror in dowloading your youtube video")
    print("The dowload has completed")

link = input("Put your youtube link here!! URL: ")
Download(link)