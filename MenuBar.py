# ---------------------- Included packages -------------
import tkinter as tk
from SongsView import SongsView
import modules
# -------------------------- Function definitions -------------------


def MenuBar(root, playerView, changePath, songs, nextSong, theme):
    songsView = SongsView(root, songs, nextSong, theme)

    def viewPlayer():
        playerView.pack(fill=tk.X)
        songsView.pack_forget()

    def viewSongs():
        songsView.pack(fill=tk.X)
        playerView.pack_forget()

    def updateTheme(newTheme):
        nonlocal songsView
        modules.setThemeFile(newTheme)
        # Update menus
        list1.configure(bg=newTheme, fg="white" if newTheme ==
                        "black" else "black")
        list2.configure(bg=newTheme, fg="white" if newTheme ==
                        "black" else "black")
        list3.configure(bg=newTheme, fg="white" if newTheme ==
                        "black" else "black")
        # Update player view components
        for widget in playerView.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=newTheme)
                for subwidget in widget.winfo_children():
                    if isinstance(subwidget, (tk.Label, tk.Button)):
                        subwidget.configure(
                            bg=newTheme, fg="white" if newTheme == "black" else "black")
        # Update songs view
        was_visible = songsView.winfo_ismapped()  # Check if songs view was visible
        songsView.destroy()
        songsView = SongsView(root, songs, nextSong, newTheme)
        if was_visible:  # If songs view was visible, show it again
            playerView.pack_forget()
            songsView.pack(fill=tk.X)

    def enableDarkMode():
        updateTheme("black")

    def enableLightMode():
        updateTheme("white")

    mainMenu = tk.Menu(root)
    root.config(menu=mainMenu)

    list1 = tk.Menu(mainMenu, tearoff=0,
                    bg=f"{theme}", fg=f"{'white' if theme == 'black' else 'black'}")
    list1.add_command(label="Open Folder...", command=changePath)
    mainMenu.add_cascade(label="File", menu=list1)

    list2 = tk.Menu(mainMenu, tearoff=0,
                    bg=f"{theme}", fg=f"{'white' if theme == 'black' else 'black'}")
    list2.add_command(label="Player", command=viewPlayer)
    list2.add_separator()
    list2.add_command(label="Songs", command=viewSongs)
    mainMenu.add_cascade(label="View", menu=list2)

    list3 = tk.Menu(mainMenu, tearoff=0,
                    bg=f"{theme}", fg=f"{'white' if theme == 'black' else 'black'}")
    list3.add_command(label="Dark", command=enableDarkMode)
    list3.add_separator()
    list3.add_command(label="Light", command=enableLightMode)
    mainMenu.add_cascade(label="Theme", menu=list3)
