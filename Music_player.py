# ---------------------- Included packages -------------
import io
from time import sleep
import tkinter as tk
from tkinter import messagebox
import stagger
from MenuBar import MenuBar
from modules import *
from pygame import mixer
from PIL import Image, ImageTk
mixer.init()
# --------------- Global variables ---------------------
volume = 0.5
songs = list()
theme = askForThemeFile()
# --------------- Function definitions -----------------


def changePath():
    """Changes the folder path in which all the mp3 files are present.

    Args:
        e (event): event variable for mouse click
    """
    global pos
    pos = 0.0
    setPos(0.0)
    path = setPath()
    setSongIndex(0)
    songs = find_songs(path)
    loadSong(songs[askForSongIndexFile()])
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
        setSongIndex((askForSongIndexFile() + 1) % len(songs))
        loadSong(songs[askForSongIndexFile()])
    mixer.music.pause()


def prevSong():
    """Plays the previous song
    """
    global pos
    setSongIndex((askForSongIndexFile() - 1 + len(songs)) % len(songs))
    pos = 0.0
    loadSong(songs[askForSongIndexFile()])
    play_pauseBtn.config(text="Pause")
    mixer.music.play()


def nextSong():
    """Plays the next song
    """
    global pos
    setSongIndex((askForSongIndexFile() + 1) % len(songs))
    pos = 0.0
    loadSong(songs[askForSongIndexFile()])
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
root.geometry("800x430")
root.maxsize(800, 430)
root.minsize(800, 430)
# ------------------------ Design statements for menu bar ------------------
f0 = tk.Frame(root)
f0.pack(fill=tk.X)


f1 = tk.Frame(f0, bg=f"{theme}")
f1.pack(side=tk.LEFT, fill=tk.BOTH)

photo = ImageTk.PhotoImage(Image.open(
    "resources\images\defaultImage.jpg").resize((400, 400)))
img = tk.Label(f1, image=photo)
img.pack(fill=tk.BOTH)
img.bind('<MouseWheel>',changeVolume)

f2 = tk.Frame(f0, bg=f"{theme}")
f2.pack(side=tk.LEFT, fill=tk.BOTH)
f2.bind('<MouseWheel>',changeVolume)
name = tk.Label(f2, bg=f"{theme}", fg=f"{'white' if theme == 'black' else 'black'}", font=("Bahnschrift Condensed", 12))
name.pack(side=tk.TOP, pady=40, fill=tk.X)
album = tk.Label(f2, bg=f"{theme}", fg=f"{'white' if theme == 'black' else 'black'}",
                 font=("Bahnschrift Condensed", 12))
album.pack(side=tk.TOP, pady=40, fill=tk.X)
artist = tk.Label(f2, bg=f"{theme}", fg=f"{'white' if theme == 'black' else 'black'}",
                  font=("Bahnschrift Condensed", 12))
artist.pack(side=tk.TOP, pady=40, fill=tk.X)

tk.Button(f2, text="<<", padx=20, pady=10,
          command=prevSong,bg=f"{theme}",fg=f"{'white' if theme == 'black' else 'black'}").pack(side=tk.LEFT, padx=30)

play_pauseBtn = tk.Button(f2, text="Play", padx=20,
                          pady=10, command=play_Pause,bg=f"{theme}",fg=f"{'white' if theme == 'black' else 'black'}")
play_pauseBtn.pack(side=tk.LEFT, padx=30)

tk.Button(f2, text=">>", padx=20, pady=10,
          command=nextSong,bg=f"{theme}",fg=f"{'white' if theme == 'black' else 'black'}").pack(side=tk.LEFT, padx=30)
statusBar = tk.Label(root, text="Made with 💟 by Ritwick",
                     relief=tk.SUNKEN, font=("Bahnschrift Condensed", 12))
statusBar.pack(side=tk.BOTTOM, fill=tk.X)
# ---------------------- Entry Point ------------------
path = askForPath()
songs = find_songs(path)
pos = askForPos()
try:
    loadSong(songs[askForSongIndexFile()])
except:
    messagebox.showerror(
            "Try to Restart me", "Somthing went wrong", icon="error")
    os.remove('resources\pathFile.txt')
    os.remove('resources\posFile.txt')
    os.remove('resources\songIndexFile.txt')
    exit(-1)
MenuBar(root, f0, changePath, songs, nextSong, theme)
root.mainloop()
storePos(root, pos, askForSongIndexFile())
