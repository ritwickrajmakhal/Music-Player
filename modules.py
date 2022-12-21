# ---------------------- Included packages -------------
from time import sleep
from tkinter import messagebox
from tkinter import filedialog
import os
from modules import *
from pygame import mixer
mixer.init()


def setSongIndex(songIndex):
    '''
    Stores index of currently playing audio file.
    '''
    with open('resources\songIndexFile.txt', 'w') as songIndexFile:
        songIndexFile.write(str(songIndex))


def getPos():
    '''
    Returns the position of music player
    '''
    with open('resources\posFile.txt') as posFile:
        return posFile.read()


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
        with open('resources\pathFile.txt', 'w') as pathFile:
            pathFile.write('')
        exit(-1)
    return list_of_song


def setPos(pos):
    '''
    Sets in which position the has stopped
    '''
    with open('resources\posFile.txt', 'w') as posFile:
        posFile.write(str(pos))


def setPath():
    '''
    opens resources\pathFile.txt in write mode and stores the path of
    the folder in which all the mp3 files present.
    '''
    path = filedialog.askdirectory()
    with open("resources\pathFile.txt", "w") as pathFile:
        pathFile.write(path)
    with open("resources\songIndexFile.txt", 'w') as songIndexFile:
        songIndexFile.write("0")
        sleep(1)
    return path


def isContainsAudioFile(songs):
    if len(songs) == 0:
        messagebox.showerror(
            "Try to Restart me", "Make sure your folder has at least one audio file", icon="error")
        with open('resources\pathFile.txt', 'w') as pathFile:
            pathFile.write('')
        exit(-1)


def askForPath():
    try:
        with open("resources\pathFile.txt") as pathFile:
            path = pathFile.read()
    except:
        path = setPath()
    return path


def askForSongIndexFile():
    try:
        with open("resources\songIndexFile.txt") as songIndexFile:
            songIndex = int(songIndexFile.read())
    except:
        setSongIndex(0)
    return songIndex


def askForPos():
    try:
        pos = float(getPos())
    except:
        pos = 0.0
        setPos(pos)
    return pos


def storePos(root, pos, songIndex):
    try:
        root.winfo_exists()
    except:
        setPos(pos+mixer.music.get_pos()/1000)
        setSongIndex(songIndex)
