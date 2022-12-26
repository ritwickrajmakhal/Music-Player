# ---------------------- Included packages -------------
import tkinter as tk
from SongsView import SongsView
# -------------------------- Function definitions -------------------
def MenuBar(root, playerView, changePath, songs, nextSong):
    songsView = SongsView(root, songs, nextSong)

    def viewPlayer():
        playerView.pack(fill=tk.X)
        songsView.pack_forget()

    def viewSongs():
        songsView.pack(fill=tk.X)
        playerView.pack_forget()

    mainMenu = tk.Menu(root)
    root.config(menu=mainMenu)

    list1 = tk.Menu(mainMenu, tearoff=0, bg="black", fg="white")
    list1.add_command(label="Open Folder...", command=changePath)
    mainMenu.add_cascade(label="File", menu=list1)

    list1 = tk.Menu(mainMenu, tearoff=0, bg="black", fg="white")
    list1.add_command(label="Player", command=viewPlayer)
    list1.add_separator()
    list1.add_command(label="Songs", command=viewSongs)
    mainMenu.add_cascade(label="View", menu=list1)