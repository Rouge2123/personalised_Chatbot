from ytmusicapi import YTMusic
from pytube import YouTube
import os


def create_cache():
    """Create cache directory if it doesn't exist."""
    try:
        os.makedirs("cache")
    except FileExistsError:
        pass


def get_audio(file_name: str = None):
    """
    This function returns an audio file or URL. If there are files in the 'cache' directory,
    it returns the first file found. If the 'cache' directory is empty, it returns the
    default audio file URL.
    """
    path = os.path.join(os.getcwd(), "cache")

    if file_name is None:
        print("get_audio: default")
        return "https://luan.xyz/files/audio/ambient_c_motion.mp3"
    else:
        for file in os.listdir(path):
            if file_name.lower() in file.lower():
                print(f"get_audio: {file}")
                return file


def reset_cache():
    """Delete/Remove all the files in the cache directory."""
    path = os.path.join(os.getcwd(), "cache")
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))


def search_song(name):
    # Get search results
    result = YTMusic().search(query=name, filter="songs")

    # Create dict of songs with necessary keys
    songs_dict = {'songs': []}

    for song in result:
        current_song_dict = {}

        current_song_dict.update({'name': song['title']})
        current_song_dict.update({'artists': song['artists'][0]['name']})
        current_song_dict.update({'videoId': song['videoId']})
        current_song_dict.update({'duration': song['duration']})
        current_song_dict.update({'isExplicit': "(Explicit) - " if song['isExplicit'] else ""})

        songs_dict['songs'].append(current_song_dict)

    return songs_dict


def download_music(video_id, file_name: str):
    video_url = 'http://youtube.com/watch?v=' + str(video_id)
    yt = YouTube(video_url)

    # search and get the first stream - with audio only
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    # Download and save music
    stream.download(
        output_path="cache/",
        filename=f"{file_name}.mp4"
    )
