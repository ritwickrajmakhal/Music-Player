# ---------------------- Included packages -------------
from time import sleep
from tkinter import messagebox
from tkinter import filedialog
import os
from modules import *
from pygame import mixer
mixer.init()

# -------------------------- Function definitions -------------------
def setSongIndex(songIndex):
    """Stores index of currently playing audio file.

    Args:
        songIndex (int): songIndex value
    """
    with open('resources\songIndexFile.txt', 'w') as songIndexFile:
        songIndexFile.write(str(songIndex))


def find_songs(path):
    """Finds all the .mp3 and .wav files from a folder path and stores it in a list

    Args:
        path (Str): Folder path

    Returns:
        list: list of file paths
    """
    list_of_song = list()
    try:
        for file in os.listdir(path):
            if file.endswith(".mp3") or file.endswith(".wav"):
                list_of_song.append(path+"\\"+file)
    except:
        messagebox.showerror(
            "Try to Restart me", "Please give me valid folder :(", icon='error')
        os.remove('resources\pathFile.txt')
        exit(-1)
    return list_of_song


def setPos(pos):
    """Sets in which position the music player has stopped

    Args:
        pos (float): pos value
    """
    with open('resources\posFile.txt', 'w') as posFile:
        posFile.write(str(pos))


def setPath():
    """opens resources\pathFile.txt in write mode and stores the path of
    the folder in which all the mp3 files present.

    Returns:
        Str: Folder path
    """
    path = filedialog.askdirectory()
    with open("resources\pathFile.txt", "w") as pathFile:
        pathFile.write(path)
    with open("resources\songIndexFile.txt", 'w') as songIndexFile:
        songIndexFile.write("0")
    return path


def isContainsAudioFile(songs):
    """songs (list): This function check whether a list contains at least one
        file or not. If it is empty then it will show a popup with an error message

    Args:
        songs (list): list of songs
    """
    if len(songs) == 0:
        messagebox.showerror(
            "Try to Restart me", "Make sure your folder has at least one audio file", icon="error")
        with open('resources\pathFile.txt', 'w') as pathFile:
            pathFile.write('')
        exit(-1)


def askForPath():
    """This function tries to open the pathFile.txt if fails then again it will call
        the setPah method
    Returns:
        Str: Folder path
    """
    try:
        with open("resources\pathFile.txt") as pathFile:
            path = pathFile.read()
    except:
        path = setPath()
    return path


def askForSongIndexFile():
    """This function tries to open the songIndexFile.txt if fails then again it will call
        the setSongIndex method with default argument

    Returns:
        int: songIndex
    """
    try:
        with open("resources\songIndexFile.txt") as songIndexFile:
            songIndex = int(songIndexFile.read())
    except:
        setSongIndex(0)
    return songIndex


def askForPos():
    """This function tries to open the posFile.txt if fails then it will call
        the setPos method with default argument

    Returns:
        float: pos value
    """
    try:
        with open('resources\posFile.txt') as posFile:
            pos = float(posFile.read())
    except:
        pos = 0.0
        setPos(0.0)
    return pos


def storePos(root, pos, songIndex):
    """Saves the current state of the music player by saving pos and songIndex value

    Args:
        root (Tk): Root variable of the music player
        pos (float): current pos value
        songIndex (int): current songIndex
    """
    try:
        root.winfo_exists()
    except:
        setPos(pos+mixer.music.get_pos()/1000)
        setSongIndex(songIndex)
