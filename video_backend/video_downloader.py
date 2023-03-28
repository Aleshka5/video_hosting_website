from pytube import YouTube

def download_from_youtube(link, file_name):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        path = youtubeObject.download(output_path='./app/videos', filename=file_name)
        return path
    except:
        return None
