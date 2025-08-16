# ---------------------- Included packages -------------
import tkinter as tk
import stagger
import modules
import os
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
# --------------- Function definitions -----------------


def get_duration(file_path):
    """Get the duration of an audio file in minutes:seconds format"""
    try:
        if file_path.lower().endswith('.mp3'):
            audio = MP3(file_path)
        elif file_path.lower().endswith('.wav'):
            audio = WAVE(file_path)
        else:
            return "??:??"

        seconds = int(audio.info.length)
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    except:
        return "??:??"


def SongsView(root, songs, nextSong, theme):
    main_frame = tk.Frame(root, bg=theme)

    # Create a frame for the list with padding
    f0 = tk.Frame(main_frame, bg=theme, padx=10, pady=10)
    f0.pack(fill=tk.BOTH, expand=True)

    # Configure scrollbar
    scrollBar = tk.Scrollbar(f0, bg=theme)
    scrollBar.pack(fill=tk.Y, side=tk.RIGHT, pady=5)

    # Configure listbox with proportional column widths
    LISTBOX_WIDTH = 135  # Total width
    list_of_songs = tk.Listbox(
        f0,
        activestyle=tk.NONE,
        width=LISTBOX_WIDTH,
        height=21,
        # Using Consolas monospace font for perfect alignment
        font=("Consolas", 11),
        bd=0,
        bg=theme,
        fg="white" if theme == "black" else "black",
        selectbackground="#404040" if theme == "black" else "#0078D4",
        selectforeground="white",
        highlightthickness=0,
        yscrollcommand=scrollBar.set
    )
    scrollBar.config(command=list_of_songs.yview)

    def on_enter(event):
        if list_of_songs.curselection():
            return
        try:
            index = list_of_songs.nearest(event.y)
            if index % 2 == 0:  # Only highlight song entries, not separators
                list_of_songs.selection_clear(0, tk.END)
                list_of_songs.selection_set(index)
        except:
            pass

    def on_leave(event):
        if not list_of_songs.curselection():
            list_of_songs.selection_clear(0, tk.END)

    def playSelected(event):
        if not list_of_songs.curselection():
            return
        selected_index = list_of_songs.curselection()[0]
        if selected_index % 2 == 0:  # Only play if a song is selected, not a separator
            modules.setSongIndex(selected_index // 2 - 1)
            nextSong()

    # Bind mouse events for hover effect
    list_of_songs.bind('<Motion>', on_enter)
    list_of_songs.bind('<Leave>', on_leave)
    list_of_songs.bind('<<ListboxSelect>>', playSelected)

    if len(songs) == 0:
        list_of_songs.insert(tk.END, "Empty List")
    else:
        alternate = False
        for song in songs:
            try:
                tag = stagger.read_tag(song)
                title = tag.title if tag.title else os.path.basename(song)
                artist = tag.artist if hasattr(
                    tag, 'artist') and tag.artist else "Unknown Artist"
                duration = get_duration(song)

                # Format song info with monospace-optimized widths
                # Truncate and pad title and artist, including ellipsis within the width limit
                title_display = (
                    title[:47] + "...").ljust(54) if len(title) > 47 else title.ljust(54)
                artist_display = (
                    artist[:22] + "...").ljust(25) if len(artist) > 22 else artist.ljust(30)

                # Create fixed-width columns with monospace font alignment
                song_info = f"{title_display:<50} {artist_display:<25} {duration:>6}"

                # Set alternating background colors
                if alternate:
                    list_of_songs.insert(tk.END, song_info)
                    if theme == "black":
                        list_of_songs.itemconfig(tk.END, bg="#1E1E1E")
                    else:
                        list_of_songs.itemconfig(tk.END, bg="#F0F0F0")
                else:
                    list_of_songs.insert(tk.END, song_info)

            except:
                list_of_songs.insert(
                    tk.END, f"{'Invalid file':<50} • {'Error':<30} • {'??:??':>5}")

            # Add a subtle separator
            separator = "─" * 95
            list_of_songs.insert(tk.END, separator)
            list_of_songs.itemconfig(tk.END, fg="#666666")

            alternate = not alternate

    list_of_songs.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    return main_frame
