# ---------------------- Included packages -------------
import io
from time import sleep
import tkinter as tk
from tkinter import messagebox
import stagger
from modules import *
from pygame import mixer
from PIL import Image, ImageTk
mixer.init()
# --------------- Global variables ---------------------
volume = 0.5
# --------------- Function definitions -----------------
def changePath(e):
    """Changes the folder path in which all the mp3 files are present.

    Args:
        e (event): event variable for mouse click
    """
    global pos
    pos = 0.0
    setPos(0.0)
    path = setPath()
    songs = find_songs(path)
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Play")


def changeVolume(event):
    """Increases volume when mouse wheel scrolls in forward direction and
    decreases volume when mouse wheel scrolls in backward direction.

    Args:
        event (event): event variable for mouse wheel
    """
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
    """Loads a mp3 files present in the path and displays meta data
    into the GUI

    Args:
        path (Str): exact path of a mp3 file
    """
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
            "resources\images\defaultImage.jpg").resize((400, 400)))
        img.configure(image=photo)
        img.image = photo
    try:
        mixer.music.load(path)
        mixer.music.play(start=pos)
    except:
        messagebox.showerror(
            "Invalid file", icon='error')
        songIndex = (songIndex + 1) % len(songs)
        loadSong(songs[songIndex])
    mixer.music.pause()


def prevSong():
    """Plays the previous song
    """
    global songIndex
    global pos
    songIndex = (songIndex - 1 + len(songs)) % len(songs)
    pos = 0.0
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Pause")
    mixer.music.play()


def nextSong():
    """Plays the next song
    """
    global songIndex
    global pos
    songIndex = (songIndex + 1) % len(songs)
    pos = 0.0
    loadSong(songs[songIndex])
    play_pauseBtn.config(text="Pause")
    mixer.music.play()


def play_Pause():
    """Play and pause toggler
    """
    if(mixer.music.get_busy()):
        mixer.music.pause()
        play_pauseBtn.config(text="Play")
    else:
        play_pauseBtn.config(text="Pause")
        mixer.music.unpause()


# ------------------- Design statements -------------------
root = tk.Tk()
root.title("Music Player")
root.geometry("800x410")
root.maxsize(800, 410)
root.minsize(800, 410)
# ------------------------ Design statements for menu bar ------------------
menuBar = tk.Frame(root, bg="black")
menuBar.pack(side=tk.TOP, fill=tk.X)

btn1 = tk.Button(menuBar, text="Songs", width=10)
btn1.pack(side=tk.LEFT, fill=tk.Y)
btn2 = tk.Button(menuBar, text="Player", width=10)
btn2.pack(side=tk.LEFT, fill=tk.Y)

f0 = tk.Frame(root)
f0.pack(fill=tk.X, side=tk.LEFT)

f1 = tk.Frame(f0, bg="black")
f1.pack(side=tk.LEFT, fill=tk.Y)

photo = ImageTk.PhotoImage(Image.open(
    "resources\images\defaultImage.jpg").resize((400, 400)))
img = tk.Label(f1, image=photo)
img.pack(fill=tk.X)
img.bind("<Button>", changePath)

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

tk.Button(f2, text="<<", padx=20, pady=10,
          command=prevSong).pack(side=tk.LEFT, padx=30)

play_pauseBtn = tk.Button(f2, text="Play", padx=20,
                          pady=10, command=play_Pause)
play_pauseBtn.pack(side=tk.LEFT, padx=30)

tk.Button(f2, text=">>", padx=20, pady=10,
          command=nextSong).pack(side=tk.LEFT, padx=30)


root.bind('<MouseWheel>', changeVolume)
# ---------------------- Entry Point ------------------
path = askForPath()
songs = find_songs(path)
isContainsAudioFile(songs)
songIndex = askForSongIndexFile()
pos = askForPos()
loadSong(songs[songIndex])

root.mainloop()
storePos(root, pos, songIndex)