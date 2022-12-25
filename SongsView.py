import tkinter as tk
import stagger
import modules

    


def SongsView(root, songs,nextSong):

    f0 = tk.Frame(root)
    list_of_songs = tk.Listbox(f0, activestyle=tk.NONE, width=135, height=21, font=(
        "Lucida Sans Typewriter", 12), bd=0, bg="black", fg="white")
    
    def playSelected(event):
        selected_indices = list_of_songs.curselection()[0]
        modules.setSongIndex(selected_indices//2-1)
        # print(selected_indices//2)
        nextSong()
        # print(modules.askForSongIndexFile())

    
    list_of_songs.pack(side=tk.LEFT)
    if len(songs) == 0:
        list_of_songs.insert(tk.ACTIVE, "Empty List")
    else:
        for song in songs:
            try:
                name = stagger.read_tag(song).title
                if name == '':
                    list_of_songs.insert(tk.END, "Unknown Title")
                else:
                    list_of_songs.insert(tk.END, f"{name}")
            except:
                list_of_songs.insert(tk.END, "Invalid file")
            list_of_songs.insert(tk.END, "-"*80)
    list_of_songs.bind('<<ListboxSelect>>', playSelected)
    return f0
