# ---------------------- Included packages -------------
import io
from time import sleep
from tkinter import *
from tkinter import filedialog
import stagger
import os
from pygame import mixer
from PIL import Image, ImageTk
mixer.init()
# --------------- Global variables ---------------------
path = ""
songs = []
songIndex = 0
# --------------- Function definitions -----------------


def setPath():
    '''
    opens pathFile.txt in write mode and stores the path of
    the folder in which all the mp3 files present.
    '''
    path = filedialog.askdirectory()
    with open("pathFile.txt", "w") as pathFile:
        pathFile.write(path)
    return path


def changePath(e):
    '''
    Changes the folder path in which all the mp3 files are present.
    '''
    global path
    global songs
    path = setPath()
    songs = find_songs(path)
    loadSong(songs[0])
    play_pauseBtn.config(text="Play")


def loadSong(path):
    '''
    Loads all the mp3 files present in a folder and displays meta data
    into the GUI
    '''
    audio = stagger.read_tag(path)
    name.config(text=audio.title)
    album.config(text=audio.album)
    artist.config(text=audio.artist)
    mixer.music.load(path)
    mixer.music.play()
    mixer.music.pause()


def prevSong():
    '''
    Plays the previous song
    '''
    global songIndex
    songIndex = (songIndex - 1 + len(songs)) % len(songs)
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Pause")
    mixer.music.play()


def nextSong():
    '''
    Plays the next song
    '''
    global songIndex
    songIndex = (songIndex + 1) % len(songs)
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Pause")
    mixer.music.play()


def play_Pause():
    '''
    Play and pause toggler
    '''
    if(mixer.music.get_busy()):
        mixer.music.pause()
        play_pauseBtn.config(text="Play")
    else:
        play_pauseBtn.config(text="Pause")
        mixer.music.unpause()


# ------------------- Design statements -------------------

root = Tk()
root.title("Music Player")
root.geometry("800x400")
root.maxsize(800, 400)
root.minsize(800, 400)
f1 = Frame(root, bg="black")
f1.pack(side=LEFT, fill=Y)

photo = ImageTk.PhotoImage(Image.open("images/logo.jpg").resize((400, 400)))
img = Label(f1, image=photo)
img.pack(fill=X)


f2 = Frame(root, bg="black")
f2.pack(side=RIGHT, fill=Y)

name = Label(f2, bg="black", fg="white", font=("Bahnschrift Condensed", 12))
name.pack(side=TOP, pady=40, fill=X)
album = Label(f2, bg="black", fg="white", font=("Bahnschrift Condensed", 12))
album.pack(side=TOP, pady=40, fill=X)
artist = Label(f2, bg="black", fg="white", font=("Bahnschrift Condensed", 12))
artist.pack(side=TOP, pady=40, fill=X)

prevBtn = Button(f2, text="<<", padx=20, pady=10, command=prevSong)
prevBtn.pack(side=LEFT, padx=30)

play_pauseBtn = Button(f2, text="Play", padx=20, pady=10, command=play_Pause)
play_pauseBtn.pack(side=LEFT, padx=30)

nextBtn = Button(f2, text=">>", padx=20, pady=10, command=nextSong)
nextBtn.pack(side=LEFT, padx=30)

img.bind("<Button>", changePath)

try:
    with open("pathFile.txt") as pathFile:
        path = pathFile.read()
    if path == "":
        path = setPath()
except:
    path = setPath()


def find_songs(path):
    '''
    Finds all the .mp3 and .wav files from a folder path and stores it in a list
    '''
    list_of_song = list()
    for file in os.listdir(path):
        if file.endswith(".mp3") or file.endswith(".wav"):
            list_of_song.append(path+"\\"+file)
    return list_of_song


songs = find_songs(path)
loadSong(songs[0])
root.mainloop()
