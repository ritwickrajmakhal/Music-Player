# All features will be written here
from datetime import datetime
from datetime import timedelta
import os
import stagger
from playsound import playsound
os.chdir("songs")  # path needs to change by the user !!IMPORTANT


class Song:
    isPlaying = False
    def __init__(self, path):
        self.path = path
        mp3 = stagger.read_tag(path)
        self.album = mp3.album
        self.artist = mp3.artist
        self.picture = mp3.picture

    def display(self):
        print("Album", self.album)
        print("Artist", self.artist)
        print("Picture", self.picture)

    def playSong(self):
        try:
            self.isPlaying = True
            playsound(self.path)
        except:
            print("Error!")

def sleep_time(time):
    # write your code here
    time = int(time)
    current_time = datetime.now()
    future_time = current_time + timedelta(minutes=time)
    return future_time


def find_songs(path):
    # write your code here
    list_of_song = list()
    for file in os.listdir():
        if file.endswith(".mp3") or file.endswith(".wav"):
            list_of_song.append(file)
    return list_of_song


songs = find_songs("songs")

for song in songs:
    s = Song(song)
    s.display()
    s.playSong()
