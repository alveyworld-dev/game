from source.sound import Sound, Music
from random import randint
from os import listdir
from os.path import isfile, join


class Jukebox:

    """
    This here class is for the random playing of background music.  Basically,
    we will pick a random music track from the avalible ones, and play them
    randomly at game start
    """

    def __init__(self):
        self.songs = [
            "music/Game_Song.wav",
        ]

    def play(self):
        randomSong = Music(self.songs[randint(0, len(self.songs)) - 1])
        randomSong.play(-1)
