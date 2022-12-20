# ---------------------- Included packages -------------
import io
from time import sleep
import tkinter as tk
from tkinter import messagebox
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
pos = 0.0
volume = 0.5
flag = True
# --------------- Function definitions -----------------


def setSongIndex(songIndex):
    '''
    Stores index of currently playing audio file.
    '''
    with open('songIndexFile.txt', 'w') as songIndexFile:
        songIndexFile.write(str(songIndex))


def getPos():
    '''
    Returns the position of music player
    '''
    with open('posFile.txt') as posFile:
        return posFile.read()


def setPos(pos):
    '''
    Sets in which position the has stopped
    '''
    with open('posFile.txt', 'w') as posFile:
        posFile.write(str(pos))


def setPath():
    '''
    opens pathFile.txt in write mode and stores the path of
    the folder in which all the mp3 files present.
    '''
    path = filedialog.askdirectory()
    with open("pathFile.txt", "w") as pathFile:
        pathFile.write(path)
    with open("songIndexFile.txt", 'w') as songIndexFile:
        songIndexFile.write("0")
        sleep(1)
    return path


def changePath(e):
    '''
    Changes the folder path in which all the mp3 files are present.
    '''
    global path
    global songs
    global pos
    pos = 0.0
    setPos(0.0)
    path = setPath()
    songs = find_songs(path)
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Play")


def changeVolume(event):
    '''
    Increases volume when mouse wheel scrolls in forward direction and
    decreases volume when mouse wheel scrolls in backward direction.
    '''
    global volume
    if event.delta < 0 and volume >= 0.0:
        volume -= 0.05
        mixer.music.set_volume(volume)
    if event.delta > 0 and volume <= 1.0:
        volume += 0.05
        mixer.music.set_volume(volume)
    root.title("Volume: "+str(int(volume*10)))
    sleep(0.5)
    root.title("Music Player")


def loadSong(path):
    '''
    Loads all the mp3 files present in a folder and displays meta data
    into the GUI
    '''
    global songIndex
    try:
        audio = stagger.read_tag(path)
        name.config(text=audio.title)
        album.config(text=audio.album)
        artist.config(text=audio.artist)
        by_data = audio[stagger.id3.APIC][0].data
        im = io.BytesIO(by_data)
        photo = ImageTk.PhotoImage(Image.open(im).resize((400, 400)))
        img.configure(image=photo)
        img.image = photo
    except:
        name.config(text='title unavailable')
        album.config(text='album unavailable')
        artist.config(text='artist unavailable')
        photo = ImageTk.PhotoImage(Image.open(
            "images/logo.jpg").resize((400, 400)))
        img.configure(image=photo)
        img.image = photo
    try:
        mixer.music.load(path)
        mixer.music.play()
    except:
        messagebox.showerror(
            "Invalid file", icon='error')
        songIndex = (songIndex + 1) % len(songs)
        setSongIndex(songIndex)
        loadSong(songs[songIndex])
    mixer.music.pause()


def prevSong():
    '''
    Plays the previous song
    '''
    global songIndex
    global pos
    songIndex = (songIndex - 1 + len(songs)) % len(songs)
    pos = 0.0
    setSongIndex(songIndex)
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Pause")
    mixer.music.play()


def nextSong():
    '''
    Plays the next song
    '''
    global songIndex
    global pos
    songIndex = (songIndex + 1) % len(songs)
    pos = 0.0
    setSongIndex(songIndex)
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Pause")
    mixer.music.play()


def play_Pause():
    '''
    Play and pause toggler
    '''
    global flag
    if(mixer.music.get_busy()):
        mixer.music.pause()
        play_pauseBtn.config(text="Play")
    else:
        if flag:
            mixer.music.set_pos(pos)
            flag = False
        play_pauseBtn.config(text="Pause")
        mixer.music.unpause()


# ------------------- Design statements -------------------

root = tk.Tk()
root.title("Music Player")
root.geometry("800x400")
root.maxsize(800, 400)
root.minsize(800, 400)

menuBar = tk.Frame(root,bg="black")
menuBar.pack(side=tk.TOP, fill=tk.X)

btn1 = tk.Button(menuBar, text="Songs", width=10)
btn1.pack(side=tk.LEFT, fill=tk.Y)
btn2 = tk.Button(menuBar, text="Player", width=10)
btn2.pack(side=tk.LEFT, fill=tk.Y)

f0 = tk.Frame(root)
f0.pack(fill=tk.X,side=tk.LEFT)

f1 = tk.Frame(f0, bg="black")
f1.pack(side=tk.LEFT, fill=tk.Y)

photo = ImageTk.PhotoImage(Image.open("images/logo.jpg").resize((400, 400)))
img = tk.Label(f1, image=photo)
img.pack(fill=tk.X)


f2 = tk.Frame(f0, bg="black")
f2.pack(side=tk.RIGHT, fill=tk.Y)

name = tk.Label(f2, bg="black", fg="white", font=("Bahnschrift Condensed", 12))
name.pack(side=tk.TOP, pady=40, fill=tk.X)
album = tk.Label(f2, bg="black", fg="white",
                 font=("Bahnschrift Condensed", 12))
album.pack(side=tk.TOP, pady=40, fill=tk.X)
artist = tk.Label(f2, bg="black", fg="white",
                  font=("Bahnschrift Condensed", 12))
artist.pack(side=tk.TOP, pady=40, fill=tk.X)

prevBtn = tk.Button(f2, text="<<", padx=20, pady=10, command=prevSong)
prevBtn.pack(side=tk.LEFT, padx=30)

play_pauseBtn = tk.Button(f2, text="Play", padx=20,
                          pady=10, command=play_Pause)
play_pauseBtn.pack(side=tk.LEFT, padx=30)

nextBtn = tk.Button(f2, text=">>", padx=20, pady=10, command=nextSong)
nextBtn.pack(side=tk.LEFT, padx=30)

img.bind("<Button>", changePath)
root.bind('<MouseWheel>', changeVolume)
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
    try:
        for file in os.listdir(path):
            if file.endswith(".mp3") or file.endswith(".wav"):
                list_of_song.append(path+"\\"+file)
    except:
        messagebox.showerror(
            "Try to Restart me", "Please give me valid folder :(", icon='error')
        with open('pathFile.txt', 'w') as pathFile:
            pathFile.write('')
        exit(-1)
    return list_of_song


songs = find_songs(path)
if len(songs) == 0:
    messagebox.showerror(
        "Try to Restart me", "Make sure your folder has at least one audio file", icon="error")
    with open('pathFile.txt', 'w') as pathFile:
        pathFile.write('')
    exit(-1)
sleep(1)
try:
    with open("songIndexFile.txt") as songIndexFile:
        songIndex = int(songIndexFile.read())
except:
    setSongIndex(0)
loadSong(songs[songIndex])
try:
    pos = float(getPos())
except:
    pos = 0.0
    setPos(pos)


root.mainloop()
try:
    root.winfo_exists()
except:
    setPos(pos+mixer.music.get_pos()/1000)
